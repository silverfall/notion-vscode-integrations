# Project Structure Guide

## Overview

This is a universal project template that works with any project type. All documentation automatically syncs to your Notion database.

## Folder Organization

```
project-root/
│
├── docs/                          # All documentation (auto-syncs to Notion)
│   ├── README.md                  # Project overview
│   ├── HOW_TO_*.md               # How-to guides
│   ├── GUIDE_*.md                # Project guides
│   ├── STEP_BY_STEP_*.md         # Tutorials
│   ├── SETUP_*.md                # Setup instructions
│   ├── NOTION_SETUP.md           # Notion integration guide
│   ├── GUIDE_ProjectStructure.md # This file
│   ├── HOW_TO_AddDocumentation.md
│   └── notion-mcp/               # Notion integration (KEEP AS IS)
│       ├── notion_mcp_server.py
│       ├── setup_notion_mcp.py
│       └── requirements-mcp.txt
│
├── src/                           # Your source code here
│   ├── main.py                    # Entry point (or main.js, main.ts, etc.)
│   ├── config.py
│   └── utils/
│
├── tests/                         # Unit and integration tests
│   ├── test_main.py
│   └── test_utils.py
│
├── .env.template                  # Environment variables template
├── .env                           # Local environment variables (in .gitignore)
├── .gitignore                     # Git ignore rules
├── README.md                       # Quick project overview
└── .github/                        # GitHub configuration
    └── copilot-instructions.md    # Copilot instructions
```

## Key Folders

### `/docs` - Documentation
Store all your documentation here. Everything is automatically discovered and synced to Notion.

**Use these naming patterns:**
- `README*.md` - Overview and getting started
- `HOW_TO_*.md` - Step-by-step how-to guides
- `GUIDE_*.md` - Comprehensive guides
- `STEP_BY_STEP_*.md` - Detailed tutorials
- `SETUP_*.md` - Installation and setup guides
- Any `.md` file is discovered

### `/src` - Source Code
Your actual project code goes here. Choose your language:

**Python project example:**
```
src/
├── main.py
├── config.py
├── utils.py
└── models/
```

**Node.js/TypeScript project example:**
```
src/
├── index.js (or index.ts)
├── config.ts
├── utils.ts
└── controllers/
```

**Multi-language project:**
```
src/
├── backend/
│   └── main.py
├── frontend/
│   └── index.js
└── shared/
```

### `/tests` - Tests
Test files for your project.

```
tests/
├── test_main.py
├── test_utils.py
└── integration/
    └── test_api.py
```

### `/docs/notion-mcp` - Notion Integration
**⚠️ DO NOT MODIFY THIS FOLDER**

This contains the Notion MCP integration files. Keep them as is.

## Configuration Files

### `.env.template`
Template for environment variables. Copy to `.env` and fill with actual values.

```
NOTION_API_KEY=your_key_here
NOTION_DATABASE_ID=your_db_id_here
DATABASE_URL=your_db_url_here
DEBUG=false
```

### `.env`
Your actual environment variables. **Keep out of version control** (.gitignore).

### `.gitignore`
Files to exclude from Git:
```
.env
__pycache__/
node_modules/
.DS_Store
*.pyc
.vscode/
```

## Adding New Files

### Adding Code
1. Create in `src/` folder
2. Follow your language conventions
3. Add corresponding test in `tests/`

### Adding Documentation
1. Create in `docs/` folder
2. Use naming pattern: `HOW_TO_*.md`, `GUIDE_*.md`, etc.
3. In Claude: "Sync to Notion"

### Adding Tests
1. Create in `tests/` folder
2. Name: `test_*.py` or `*.test.js`, etc.
3. Follow test conventions

## Syncing Documentation

### Automatic Discovery
All `.md` files in `docs/` folder are automatically discovered.

### Sync to Notion
In Claude/Copilot chat:
```
"Sync my documentation to Notion"
```

### Check What Will Be Synced
In Claude/Copilot chat:
```
"Scan my documentation"
```

## Working with Notion

### Database Fields
Your Notion database has:
- **Title** - Document name
- **File Path** - Where file is stored
- **Documentation Type** - Auto-categorized
- **Updated** - Sync timestamp

### Sharing with Team
1. Get Notion database link
2. Share with team members
3. Set access level (View/Edit)
4. Team can reference documentation

### Keeping Up-to-Date
1. Edit documentation files locally
2. Sync to Notion
3. Team sees latest version
4. No manual copy-paste needed

## Project Types

This template works with any project type. Examples:

### Python Project
```
src/
├── main.py
├── requirements.txt
└── app/
```

### Node.js Project
```
src/
├── index.js
├── package.json
└── lib/
```

### TypeScript Project
```
src/
├── index.ts
├── tsconfig.json
└── controllers/
```

### Full-Stack Project
```
src/
├── backend/ (Python/Node)
├── frontend/ (React/Vue)
└── shared/
```

## Best Practices

✅ **Keep documentation in `/docs`**
- Easy to sync
- Version controlled
- Always up-to-date

✅ **Use naming patterns**
- HOW_TO_*, GUIDE_*, STEP_BY_STEP_*
- Auto-categorized in Notion
- Clear intent

✅ **Keep code in `/src`**
- Organized structure
- Easy to scale
- Clear separation

✅ **Test everything**
- Store tests in `/tests`
- Write tests before code
- Keep coverage high

✅ **Use environment variables**
- Copy .env.template to .env
- Fill with actual values
- Keep .env out of git

❌ **Avoid**
- Mixing code and docs
- Putting tests in src/
- Hardcoding configuration
- Ignoring .env properly

## Next Steps

1. ✅ Copy `.env.template` to `.env` and fill values
2. ✅ Add your code to `src/` folder
3. ✅ Create documentation in `docs/` folder
4. ✅ Run Notion setup: `python docs/notion-mcp/setup_notion_mcp.py`
5. ✅ Sync docs: "Sync to Notion"

## Related Documentation

- [README.md](README.md) - Project overview
- [HOW_TO_AddDocumentation.md](HOW_TO_AddDocumentation.md) - How to add docs
- [NOTION_SETUP.md](NOTION_SETUP.md) - Notion integration guide
