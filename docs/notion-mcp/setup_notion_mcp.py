#!/usr/bin/env python3
"""
Interactive setup script for Notion MCP integration
"""

import os
import json
import sys
from pathlib import Path


def get_user_input(prompt: str, default: str = None) -> str:
    """Get input from user with optional default"""
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "

    value = input(prompt).strip()
    return value if value else default


def setup_notion_integration():
    """Interactive setup for Notion integration"""
    print("\n" + "=" * 60)
    print("NOTION MCP INTEGRATION SETUP")
    print("=" * 60 + "\n")

    # Step 1: Notion API Key
    print("Step 1: Notion Internal Integration Secret")
    print("-" * 60)
    print("Get this from: https://www.notion.so/my-integrations")
    api_key = get_user_input("Enter NOTION_API_KEY (starts with 'secret_')")
    if not api_key.startswith("secret_"):
        print("⚠️  Warning: API key should start with 'secret_'")

    # Step 2: Database ID
    print("\nStep 2: Notion Database ID")
    print("-" * 60)
    print("Get this from your database URL: https://notion.so/workspace/[DATABASE_ID]")
    database_id = get_user_input("Enter NOTION_DATABASE_ID (32 characters)")

    # Step 3: Workspace Root
    print("\nStep 3: Workspace Root")
    print("-" * 60)
    default_workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    workspace_root = get_user_input("Enter WORKSPACE_ROOT path", default_workspace)

    # Step 4: Confirm and setup
    print("\n" + "=" * 60)
    print("CONFIGURATION SUMMARY")
    print("=" * 60)
    print(f"API Key: {api_key[:20]}...")
    print(f"Database ID: {database_id[:8]}...")
    print(f"Workspace: {workspace_root}")

    confirm = input("\nProceed with setup? (y/n): ").lower().strip()
    if confirm != "y":
        print("Setup cancelled.")
        return

    # Create MCP configuration
    mcp_config = {
        "mcpServers": {
            "notion": {
                "command": "python",
                "args": [str(Path(__file__).parent / "notion_mcp_server.py")],
                "env": {
                    "NOTION_API_KEY": api_key,
                    "NOTION_DATABASE_ID": database_id,
                    "WORKSPACE_ROOT": workspace_root,
                },
            }
        }
    }

    # Determine MCP config path
    if sys.platform == "darwin":  # macOS
        mcp_path = Path.home() / "Library" / "Application Support" / "Code" / "User" / "mcp.json"
    elif sys.platform == "linux":
        mcp_path = Path.home() / ".config" / "Code" / "User" / "mcp.json"
    elif sys.platform == "win32":
        mcp_path = Path.home() / "AppData" / "Roaming" / "Code" / "User" / "mcp.json"
    else:
        mcp_path = None

    if mcp_path:
        # Merge with existing config if present
        existing_config = {}
        if mcp_path.exists():
            try:
                with open(mcp_path) as f:
                    existing_config = json.load(f)
            except Exception as e:
                print(f"Warning: Could not read existing config: {e}")

        # Merge configs
        existing_config.setdefault("mcpServers", {})
        existing_config["mcpServers"]["notion"] = mcp_config["mcpServers"]["notion"]

        # Write config
        mcp_path.parent.mkdir(parents=True, exist_ok=True)
        with open(mcp_path, "w") as f:
            json.dump(existing_config, f, indent=2)

        print(f"\n✅ Configuration saved to: {mcp_path}")
    else:
        print("\n⚠️  Could not determine MCP config path for your OS")
        print("Please manually add this to your mcp.json:")
        print(json.dumps(mcp_config, indent=2))

    # Create .env file as backup
    env_file = Path(workspace_root) / ".env"
    env_content = f"""# Notion MCP Integration
NOTION_API_KEY={api_key}
NOTION_DATABASE_ID={database_id}
WORKSPACE_ROOT={workspace_root}
"""

    with open(env_file, "w") as f:
        f.write(env_content)

    print(f"✅ Environment backup saved to: {env_file}")

    print("\n" + "=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Restart VS Code")
    print("2. Try the MCP tools:")
    print("   - Ask Claude: 'Scan my documentation'")
    print("   - Ask Claude: 'Check Notion status'")
    print("   - Ask Claude: 'Sync to Notion'")


if __name__ == "__main__":
    try:
        setup_notion_integration()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
