#!/usr/bin/env python3
"""
MCP Server for Notion Integration
Scans ALL project files and syncs them to Notion Documentation wiki
"""

import os
import json
import asyncio
from pathlib import Path
from typing import Any
import re
from datetime import datetime

import requests
from mcp.server import Server
from mcp.types import Resource, TextContent, Tool
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration - load from environment variables
NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
NOTION_PARENT_PAGE_ID = os.environ.get("NOTION_PARENT_PAGE_ID")
WORKSPACE_ROOT = os.environ.get("WORKSPACE_ROOT", os.getcwd())

# Notion API endpoints
NOTION_API_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2025-09-03"

# File patterns - scan all file types
FILE_PATTERNS = [
    "*.md",
    "*.py",
    "*.js",
    "*.ts",
    "*.tsx",
    "*.json",
    "*.yaml",
    "*.yml",
    "*.txt",
]

# Folders to scan
SCAN_FOLDERS = ["docs", "src"]

server = Server("notion-mcp")


class NotionClient:
    """Client for interacting with Notion API"""

    def __init__(self, api_key: str, parent_page_id: str):
        self.api_key = api_key
        self.parent_page_id = parent_page_id
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }

    def create_page(self, title: str, content: str, file_path: str) -> dict:
        """Create a child page under Documentation wiki"""
        if not self.api_key or not self.parent_page_id:
            logger.warning("Notion API key or parent page ID not configured")
            return {"success": False, "message": "Notion credentials not set"}

        # Convert content to Notion blocks
        blocks = []
        for line in content.split("\n")[:50]:  # Limit to 50 lines
            if line.strip():
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": line[:2000]}}]
                    }
                })

        payload = {
            "parent": {"page_id": self.parent_page_id},
            "properties": {
                "title": [{"text": {"content": title}}]
            },
            "children": blocks[:100],  # Notion limit
        }

        try:
            response = requests.post(
                f"{NOTION_API_URL}/pages",
                headers=self.headers,
                json=payload,
                timeout=10,
            )
            response.raise_for_status()
            return {"success": True, "page_id": response.json().get("id"), "page_url": response.json().get("url")}
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to create Notion page: {e}")
            return {"success": False, "error": str(e)}


class FileScanner:
    """Scans workspace for all project files"""

    def __init__(self, root_path: str):
        self.root_path = Path(root_path)

    def find_files(self) -> list[dict]:
        """Find all files in docs and src folders"""
        files = []

        for folder_name in SCAN_FOLDERS:
            folder_path = self.root_path / folder_name
            if not folder_path.exists():
                continue

            for pattern in FILE_PATTERNS:
                # Use rglob for recursive search (searches all subdirectories)
                matches = folder_path.rglob(pattern)

                for match in matches:
                    if match.is_file():
                        # Get relative path
                        relative_path = match.relative_to(self.root_path)
                        
                        # Skip notion-mcp subfolder and hidden files
                        if "notion-mcp" in relative_path.parts or match.name.startswith("."):
                            continue
                        
                        files.append({
                            "path": str(relative_path),
                            "abs_path": str(match),
                            "name": match.stem,
                            "extension": match.suffix,
                        })

        return files

    def read_file(self, abs_path: str) -> str:
        """Read file content"""
        try:
            with open(abs_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            logger.error(f"Failed to read file {abs_path}: {e}")
            return ""


# Initialize clients
scanner = FileScanner(WORKSPACE_ROOT)
notion_client = NotionClient(NOTION_API_KEY, NOTION_PARENT_PAGE_ID)


@server.list_resources()
async def list_resources() -> list[Resource]:
    """List all project files in docs and src folders"""
    files = scanner.find_files()
    resources = []

    for file in files:
        resources.append(
            Resource(
                uri=f"file://{file['abs_path']}",
                name=file["name"],
                mimeType="text/plain",
            )
        )

    return resources


@server.read_resource()
async def read_resource(uri: str) -> str:
    """Read file content"""
    path = uri.replace("file://", "")
    content = scanner.read_file(path)
    return content


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools"""
    return [
        Tool(
            name="scan_files",
            description="Scan docs and src folders for all project files",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="sync_to_notion",
            description="Sync all project files to Notion Documentation wiki",
            inputSchema={
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to specific file to sync (optional, syncs all if not provided)",
                    },
                },
            },
        ),
        Tool(
            name="get_notion_status",
            description="Check Notion integration status and configuration",
            inputSchema={"type": "object", "properties": {}},
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> str:
    """Handle tool calls"""
    if name == "scan_files":
        files = scanner.find_files()

        return json.dumps(
            {
                "success": True,
                "count": len(files),
                "files": files,
            }
        )

    elif name == "sync_to_notion":
        file_path = arguments.get("file_path")

        if not NOTION_API_KEY or not NOTION_PARENT_PAGE_ID:
            return json.dumps(
                {
                    "success": False,
                    "error": "Notion credentials not configured. Set NOTION_API_KEY and NOTION_PARENT_PAGE_ID environment variables.",
                }
            )

        if file_path:
            # Sync specific file
            abs_path = Path(WORKSPACE_ROOT) / file_path
            if not abs_path.exists():
                return json.dumps({"success": False, "error": f"File not found: {file_path}"})

            content = scanner.read_file(str(abs_path))
            result = notion_client.create_page(
                title=abs_path.name,
                content=content,
                file_path=file_path,
            )
            return json.dumps(result)
        else:
            # Sync all files
            files = scanner.find_files()
            results = []

            for file in files:
                content = scanner.read_file(file["abs_path"])
                result = notion_client.create_page(
                    title=f"{file['name']}{file['extension']}",
                    content=content,
                    file_path=file["path"],
                )
                results.append({"file": file["path"], "result": result})

            return json.dumps(
                {
                    "success": True,
                    "synced": len(results),
                    "results": results,
                }
            )

    elif name == "get_notion_status":
        return json.dumps(
            {
                "configured": bool(NOTION_API_KEY and NOTION_PARENT_PAGE_ID),
                "api_key_set": bool(NOTION_API_KEY),
                "parent_page_id": NOTION_PARENT_PAGE_ID[:8] + "..."
                if NOTION_PARENT_PAGE_ID
                else "Not set",
                "workspace_root": WORKSPACE_ROOT,
                "scan_folders": SCAN_FOLDERS,
            }
        )

    return json.dumps({"error": f"Unknown tool: {name}"})


async def main():
    """Main entry point"""
    async with server:
        logger.info("Notion MCP Server started")
        logger.info(f"Workspace: {WORKSPACE_ROOT}")
        logger.info(f"Notion configured: {bool(NOTION_API_KEY and NOTION_PARENT_PAGE_ID)}")


if __name__ == "__main__":
    asyncio.run(main())
