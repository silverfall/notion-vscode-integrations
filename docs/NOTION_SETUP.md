# Notion Integration Setup Guide

## Complete Setup Instructions

### Prerequisites
- Notion account
- VS Code with Copilot/Claude extension
- Python 3.9+

### Step 1: Create Notion Internal Integration

1. Go to https://www.notion.so/my-integrations
2. Click "Create new integration"
3. Name: `Project Files Sync`
4. Select your workspace
5. **Copy the API Key** (starts with `ntn_`)

### Step 2: Create Notion Wiki Page (Parent Page)

1. In Notion, open your Documentation wiki
2. Create a new page for your project (e.g., "My Project")
3. Share the page with your integration:
   - Click **Share** (top right)
   - Add your integration
4. **Copy the Page ID** from the URL:
   - URL format: `notion.so/workspace/PAGE_ID`
   - Example: `2e6b88d55b3a81beb1bafb2cced13317`

**Note**: Files will be synced as child pages under this parent page.

### Step 3: Run Setup Wizard

```bash
cd docs/notion-mcp
python setup_notion_mcp.py
```

Enter:
- **Notion API Key**: Your integration key (ntn_...)
- **Notion Parent Page ID**: The page ID you copied
- **Workspace Root**: Leave default or enter custom path

### Step 4: Verify Configuration

Check `docs/notion-mcp/.env`:
```env
NOTION_API_KEY=ntn_xxxxxxxxxxxxx
NOTION_PARENT_PAGE_ID=2e6b88d55b3a81beb1bafb2cced13317
```
   - DATABASE_ID is the 32-character string

### Step 3: Run Setup Script

```bash
cd docs/notion-mcp
python setup_notion_mcp.py
```

When prompted:
- Enter your Notion API Key (secret_...)
- Enter your Database ID
- Enter your workspace root path

### Step 4: Restart VS Code

Close and reopen VS Code to activate MCP server.

### Step 5: Verify Setup

In Claude/Copilot chat:
```
"Check Notion status"
```

Should show:
- `configured: true`
- `api_key_set: true`
- Database ID shown

### Step 6: First Sync

```
"Scan my documentation"
```

Shows all .md files found. Then:

```
"Sync to Notion"
```

Check your Notion database - pages should appear!

## Supported Files

Automatically discovered and synced:
- `README.md`
- `HOW_TO_*.md`
- `GUIDE_*.md`
- `STEP_BY_STEP_*.md`
- `SETUP_*.md`
- Any `.md` file in docs/ folder

## Notion Database Schema

| Field | Type | Purpose |
|-------|------|---------|
| Title | Text | Document name |
| File Path | Rich Text | Source file location |
| Documentation Type | Select | README, How-To, Guide, etc. |
| Updated | Date | Last sync timestamp |

## Workflow

1. **Create/Edit Documentation**
   - Create `.md` files in `docs/` folder
   - Use naming patterns: HOW_TO_*.md, GUIDE_*.md, etc.

2. **Sync to Notion**
   - In Claude: "Sync to Notion"
   - Files pushed to Notion database

3. **Share with Team**
   - Copy Notion database link
   - Share with teammates
   - They can view and reference

4. **Keep Updated**
   - Edit docs locally
   - Sync changes to Notion
   - Team always sees latest

## Troubleshooting

**Setup script fails:**
- Verify Python 3.9+ installed
- Check all paths are correct
- Run again with same credentials

**"Credentials not configured":**
- Run setup script again
- Verify API key starts with `secret_`
- Check Database ID is 32 characters

**Files not found:**
- Ensure files end in `.md`
- Check file names match patterns
- Verify files are in `docs/` folder

**Sync fails:**
- Verify API key and Database ID
- Check integration is shared with database
- Restart VS Code

**Tools not showing:**
- Restart VS Code
- Check MCP server in settings
- Verify setup completed

## Configuration Files

After setup, your configuration is stored in:
- MCP Config: `~/.config/Code/User/mcp.json` (or platform equivalent)
- Backup: `.env` file in project root

## Next Steps

1. ✅ Complete setup above
2. ✅ Create/update documentation files
3. ✅ Sync to Notion
4. ✅ Share database link with team
5. ✅ Keep docs updated

## Support Resources

- Notion API: https://developers.notion.com/
- MCP Protocol: https://modelcontextprotocol.io/
- VS Code Copilot: https://code.visualstudio.com/docs/copilot/mcp
