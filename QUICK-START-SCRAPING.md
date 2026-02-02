# LSF Documentation Scraping - Quick Start

## Overview
Scrape Lumerical Scripting Language (LSF) command documentation from Ansys Optics website. Total: 727 commands, 102 scraped, 88 remaining.

## Prerequisites
- Python 3.12+
- Chrome browser (for Selenium fallback)
- Virtual environment (recommended)

## Installation

### Option 1: Using uv (Recommended)
```bash
# Create virtual environment
uv venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Install dependencies
pip install cloudscraper beautifulsoup4 html2text selenium webdriver-manager requests
```

### Option 2: Using requirements.txt
```bash
pip install -r requirements.txt
```

## Essential Scripts

### 1. Single Command Scraper (`scrape_one_command.py`)
```bash
# Check status
python scrape_one_command.py --stats

# List missing commands
python scrape_one_command.py --list

# Scrape next command
python scrape_one_command.py --next

# Scrape specific command
python scrape_one_command.py "command_name"
```

### 2. Interval Controller (`sleep_script.py`)
```bash
# Wait 60 seconds (default)
python sleep_script.py

# Wait custom time
python sleep_script.py 90
python sleep_script.py --minutes 2
```

### 3. Batch Scraper (`scrape_missing_lsf_docs.py`)
```bash
# Scrape 5 commands with intervals
python scrape_missing_lsf_docs.py --limit 5
```

## Quick Start Commands

### Resume Scraping (Safest Method)
```bash
# One-time setup
python scrape_one_command.py --stats

# Continuous scraping (run these two commands repeatedly)
python scrape_one_command.py --next
python sleep_script.py
```

### Check Progress
```bash
# View statistics
python scrape_one_command.py --stats

# Count generated files
ls docs/lsf-script/ | wc -l

# Check log
tail -10 docs/scrape-single.log
```

## File Structure
```
project/
├── scripts/
│   ├── scrape_one_command.py     # Main scraper
│   ├── sleep_script.py           # Wait controller
│   └── scrape_missing_lsf_docs.py # Batch processor
├── docs/
│   ├── lsf-script/               # Generated Markdown (*.md)
│   ├── missing-lsf-script-docs.md # Remaining commands
│   ├── scrape-progress.json      # Progress tracking
│   └── scrape-single.log         # Operation log
└── requirements.txt              # Dependencies
```

## Critical Configuration

### Rate Limiting (DO NOT CHANGE)
- **Success interval**: 60 seconds minimum
- **Failure interval**: 120 seconds
- **Max retries**: 3 per command

### Cloudflare Bypass
- Primary: `cloudscraper` library
- Fallback: Selenium with Chrome
- Automatic retry with exponential backoff

## Current Status (2026-02-02)
- **Total commands**: 727
- **Scraped**: 102 commands
- **Remaining**: 88 commands
- **Next command**: `seteigensolver`
- **Estimated time**: ~1.5 hours

## Troubleshooting

### If Cloudflare Blocks
```bash
# Increase wait time
python sleep_script.py 120

# Check if Selenium is working
# Ensure Chrome is installed
```

### If Progress File Corrupts
```bash
# Restore from backup
cp docs/scrape-progress.json.backup docs/scrape-progress.json

# Or regenerate from missing commands
python scrape_one_command.py --stats
```

## Complete Workflow
For detailed information, see: [LSF-DOCUMENTATION-SCRAPING-WORKFLOW.md](LSF-DOCUMENTATION-SCRAPING-WORKFLOW.md)

---
**Next Action**: Run `python scrape_one_command.py --next` then `python sleep_script.py`  
**Completion**: ~88 iterations (~1.5 hours)