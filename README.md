# Universal Project Template with Notion Integration

## Overview

This template automatically syncs **ALL project files** (not just documentation) to Notion's Documentation wiki.

Works with any language: Python, JavaScript, TypeScript, JSON, YAML, and more!

## Quick Start

1. **Copy this template** to your new project location
2. **Run setup wizard**:
   ```bash
   python docs/notion-mcp/setup_notion_mcp.py
   ```
3. **Provide credentials**:
   - Notion API Key
   - Notion Parent Page ID (Documentation wiki page ID)
4. **Restart VS Code**
5. **In Claude/Copilot**: "Sync to Notion"

## What Gets Synced

ALL files from `docs/` and `src/` folders:
- Markdown (*.md)
- Python (*.py)
- JavaScript/TypeScript (*.js, *.ts, *.tsx)
- Config files (*.json, *.yaml, *.yml)
- Text files (*.txt)

## Project Structure

```
project-root/
├── src/              # Source code (ALL synced to Notion)
├── docs/             # Documentation (ALL synced to Notion)
│   └── notion-mcp/   # Notion integration (DO NOT DELETE)
├── .env.template     # Configuration template
└── README.md         # This file
```

## Notion Integration

Files are synced as child pages under your Documentation wiki page:

- **[docs/README.md](docs/README.md)** - Documentation overview
- **[docs/NOTION_SETUP.md](docs/NOTION_SETUP.md)** - Notion integration guide
- **[docs/GUIDE_ProjectStructure.md](docs/GUIDE_ProjectStructure.md)** - Project structure guide
- **[docs/HOW_TO_AddDocumentation.md](docs/HOW_TO_AddDocumentation.md)** - How to add documentation

## Notion Integration

This project includes automatic documentation sync to Notion:

### Setup (5 minutes)
```bash
cd docs/notion-mcp
python setup_notion_mcp.py
```

### Sync Documentation
In Claude/Copilot chat:
```
"Sync my documentation to Notion"
```

### Features
✅ Auto-discovers documentation files
✅ Syncs to Notion with one command
✅ Team collaboration ready
✅ Full-text searchable

## Next Steps

1. Update `.env.template` with your project settings
2. Copy to `.env` and fill with actual values
3. Add your code to `src/` folder
4. Create documentation in `docs/` folder
5. Set up Notion integration (see docs/NOTION_SETUP.md)
6. Sync your docs: "Sync to Notion"

## For More Information

See the documentation files in `/docs` folder for detailed guides and instructions.
