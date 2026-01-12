# Universal Project Template with Notion Integration

## Project Overview
This is a universal project template that works with any project type (Python, Node.js, TypeScript, etc.). It comes pre-configured with:
- Flexible project structure
- Automatic sync for ALL file types (not just documentation)
- Notion MCP integration built-in
- Auto-sync to Notion Documentation wiki

## What Auto-Syncs to Notion
ALL files in `/docs` and `/src` folders are automatically synced to your Notion Documentation wiki as child pages:
- Markdown files (*.md)
- Python files (*.py)
- JavaScript/TypeScript files (*.js, *.ts, *.tsx)
- Config files (*.json, *.yaml, *.yml)
- Text files (*.txt)

## Setup Instructions

### Step 1: Configure Notion Credentials
```bash
cd docs/notion-mcp
python setup_notion_mcp.py
```

Enter:
- Your Notion API Key (ntn_...)
- Your Notion Parent Page ID (from Documentation wiki)
- Workspace root path

### Step 2: Restart VS Code

### Step 3: Start Using Notion Integration
In Claude/Copilot chat:
- "Scan files" → Find all syncable files
- "Sync to Notion" → Push files to Notion as child pages
- "Check Notion status" → Verify setup

## Project Structure
```
project-root/
├── docs/                          # All documentation here (syncs to Notion)
│   ├── README.md                  # Project overview
│   ├── HOW_TO_*.md               # How-to guides
│   ├── GUIDE_*.md                # Project guides
│   ├── notion-mcp/               # Notion integration (DO NOT DELETE)
│   │   ├── notion_mcp_server.py
│   │   ├── setup_notion_mcp.py
│   │   └── requirements-mcp.txt
│   └── NOTION_SETUP.md           # Notion setup instructions
│
├── src/                           # Your code here (any language)
│   └── main.py (or .js, .ts, etc.)
│
├── tests/                         # Your tests here
│
├── .env.template                  # Copy to .env and fill
├── README.md                       # Project overview
└── .github/                        # GitHub config
    └── copilot-instructions.md    # This file
```


## Adding New Documentation

1. Create a new `.md` file in `/docs` folder
2. Name it with pattern: README.md, HOW_TO_*.md, GUIDE_*.md, STEP_BY_STEP_*.md
3. In Claude: "Sync to Notion"
4. Your docs appear in Notion automatically

## Notion Database
Your Notion database will have these fields:
- **Title** (Text)
- **File Path** (Rich Text)
- **Documentation Type** (Select)
- **Updated** (Date)

## Features
✅ Works with any project type
✅ Auto-discovers documentation
✅ One-command sync to Notion
✅ Team collaboration ready
✅ Full-text searchable in Notion
✅ No code disruption

## For More Information
See `/docs/NOTION_SETUP.md` for complete Notion integration guide.

---

**Status:** ✅ Ready to use
**Next:** Run `python docs/notion-mcp/setup_notion_mcp.py`
