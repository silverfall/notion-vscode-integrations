# Project Documentation

Add your project documentation here.

This folder syncs to Notion automatically.
   ```

3. **Restart VS Code**

4. **Sync Documentation**
   - In Claude/Copilot: "Sync to Notion"
   - Your docs appear in Notion database

### Using in Claude/Copilot

```
"Scan my documentation"
→ Find all .md files

"Sync to Notion"
→ Push docs to Notion database

"Check Notion status"
→ Verify configuration
```

## File Organization

```
docs/
├── README.md                    ← You are here
├── HOW_TO_*.md                 ← How-to guides
├── GUIDE_*.md                  ← Comprehensive guides
├── STEP_BY_STEP_*.md           ← Step-by-step tutorials
├── SETUP_*.md                  ← Setup instructions
├── NOTION_SETUP.md             ← Notion integration guide
└── notion-mcp/                 ← Notion MCP server (keep as is)
    ├── notion_mcp_server.py
    ├── setup_notion_mcp.py
    └── requirements-mcp.txt
```

## Adding Documentation

1. Create new `.md` file in `docs/` folder
2. Use pattern: `HOW_TO_name.md`, `GUIDE_name.md`, etc.
3. Write your documentation
4. In Claude: "Sync to Notion"
5. Your doc appears in Notion automatically

## Benefits

✅ **Single Source of Truth** - Docs in code, view in Notion
✅ **Team Collaboration** - Share Notion database with team
✅ **Always Updated** - Sync whenever you make changes
✅ **Searchable** - Full-text search in Notion
✅ **Organized** - Auto-categorized by type

## Notion Database

Your Notion database includes:
- **Title** - Document name
- **File Path** - Source location
- **Documentation Type** - Auto-categorized (README, How-To, Guide, etc.)
- **Updated** - Sync timestamp

## Next Steps

1. Update the documentation files for your project
2. Run the Notion setup: `python notion-mcp/setup_notion_mcp.py`
3. Sync your docs: "Sync to Notion"
4. Share Notion database with your team
5. Keep docs updated with code changes

## Support

For detailed Notion integration guide, see `NOTION_SETUP.md`
