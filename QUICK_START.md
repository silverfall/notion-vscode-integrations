# 🚀 QUICK START - Using the Universal Template

## For a New Project (10 minutes)

### 1. Copy the Template
```bash
cp -r /Users/idang/Documents/workspaces/notion-mcp ~/my-new-project
cd ~/my-new-project
```

### 2. Get Notion Credentials (2 min)
- Go to https://www.notion.so/my-integrations
- Create integration → copy API key
- Create database → copy Database ID

### 3. Setup Notion Integration (1 min)
```bash
cd docs/notion-mcp
python setup_notion_mcp.py
```
- Enter API key
- Enter Database ID
- Confirm workspace path

### 4. Restart VS Code
Close and reopen VS Code

### 5. Test (instant)
In Claude/Copilot:
```
"Check Notion status"
```

### 6. Start Working
- Add code to `src/` folder
- Add docs to `docs/` folder (use patterns: HOW_TO_*, GUIDE_*, etc.)
- In Claude: "Sync to Notion"

### 7. Share with Team
- Copy Notion database link
- Send to team
- Done! ✅

---

## Documentation File Patterns

| Pattern | Type | Example |
|---------|------|---------|
| README*.md | README | README.md |
| HOW_TO_*.md | How-To | HOW_TO_Setup.md |
| GUIDE_*.md | Guide | GUIDE_Architecture.md |
| STEP_BY_STEP_*.md | Tutorial | STEP_BY_STEP_Deploy.md |
| SETUP_*.md | Setup | SETUP_Development.md |
| Any .md | Documentation | notes.md |

---

## Template Contents

```
notion-mcp/           (Template folder)
├── docs/             (Documentation - syncs to Notion)
│   ├── README.md
│   ├── NOTION_SETUP.md
│   ├── HOW_TO_AddDocumentation.md
│   ├── GUIDE_ProjectStructure.md
│   └── notion-mcp/   (Notion MCP server - keep as is)
├── src/              (Your code - any language)
│   └── main.py
├── tests/            (Your tests)
├── .env.template     (Copy to .env)
├── .gitignore
├── README.md
└── .github/
    └── copilot-instructions.md
```

---

## What Each Folder Does

| Folder | Purpose |
|--------|---------|
| docs/ | All documentation (auto-syncs to Notion) |
| docs/notion-mcp/ | Notion MCP server (don't modify) |
| src/ | Your source code (any language) |
| tests/ | Your test files |
| .github/ | GitHub and VS Code config |

---

## Claude/Copilot Commands

```
"Scan my documentation"
→ Find all .md files

"Sync to Notion"
→ Push docs to Notion

"Check Notion status"
→ Verify setup
```

---

## Best Practices

✅ Keep code in `src/` folder
✅ Keep docs in `docs/` folder
✅ Use naming patterns (HOW_TO_*, GUIDE_*, etc.)
✅ Sync after updating documentation
✅ Never modify files in `docs/notion-mcp/`
✅ Keep `.env` out of version control

---

## Troubleshooting

**Setup fails?**
- Verify Python 3.9+ installed
- Check API key starts with `secret_`
- Run setup again

**Docs not syncing?**
- Ensure files are in `docs/` folder
- Check files end in `.md`
- Verify naming pattern is correct

**Notion not accessible?**
- Check API key is correct
- Verify database is shared with integration
- Restart VS Code

---

## Template Ready for Use ✅

Location: `/Users/idang/Documents/workspaces/notion-mcp`

Copy this folder anytime you start a new project!
