# LSF Command Documentation Scraping Workflow

## Project Overview
This project scrapes Lumerical Scripting Language (LSF) command documentation from the Ansys Optics knowledge base (https://optics.ansys.com). The goal is to build a complete local documentation repository for all 727 LSF commands.

**Source**: Ansys Optics Knowledge Base  
**Target**: Local Markdown documentation in `docs/lsf-script/`  
**Total Commands**: 727  
**Current Progress**: 102 commands scraped, 88 remaining (as of 2026-02-02)

## System Architecture

### Core Scripts
1. **`scrape_one_command.py`** - Single-command scraper with progress tracking
   - `--next` - Scrape next missing command
   - `--list` - List missing commands
   - `--stats` - Show statistics
   - `"command_name"` - Scrape specific command

2. **`sleep_script.py`** - Interval controller for safe scraping
   - Default: 60 seconds between successful scrapes
   - 120 seconds after failures
   - Configurable wait times

3. **`scrape_missing_lsf_docs.py`** - Batch scraper with configurable limits
   - Processes multiple commands sequentially
   - Configurable batch size and intervals

### Supporting Files
- **`docs/missing-lsf-script-docs.md`** - Auto-updated list of remaining commands
- **`docs/scrape-progress.json`** - Progress tracking (processed commands, last command)
- **`docs/scrape-single.log`** - Log file with timestamped operations
- **`docs/lsf-script/`** - Output directory (642 Markdown files created)

### Dependencies
```python
# Core scraping dependencies
cloudscraper==1.2.71      # Cloudflare bypass
beautifulsoup4==4.14.3    # HTML parsing
html2text==2025.4.15      # HTML to Markdown conversion
selenium==4.28.1          # Fallback browser automation
webdriver-manager==4.0.2  # Chrome driver management

# Standard libraries
requests==2.32.3
lxml==5.3.2
```

## Current State (2026-02-02)

### Statistics
- **Total commands**: 727
- **Successfully scraped**: 102 commands (14.0%)
- **Remaining missing**: 88 commands (91 commands in missing list)
- **Markdown files created**: 642 files in `docs/lsf-script/`
- **Success rate**: 100% (no failures in current session)
- **Average time per command**: ~60 seconds (including wait time)

### Progress Tracking
- **Progress file**: `docs/scrape-progress.json`
- **Last processed command**: `setconnectionrouting`
- **Next command**: `seteigensolver`

### Missing Commands Overview
```
S: selectpartial, set, setactivesolver, setanalysis, setconnectionrouting, 
   setdevice, seteigensolver, setemeanalysis, setexpansion, setexpression,
   setfield, setglobalmonitor, setglobalsource, seticon, setlayer, setmaterial,
   setname, setnamed, setpersistcheckouts, setplot, setposition, setpsfoutput,
   setrectangle, setresource, setresult, setsetting, setsourcesignal,
   setsweep, setvalue, setview, shiftselect, shiftselectpartial, show,
   showmenubar, sign, simulation, simulationdiverged, sin, size, smithchart,
   solar, sort, sortmap, sourceintensity, sourceintensity_avg, sourceintensity_pavg,
   sourcenorm, sourcenorm2_avg, sourcenorm2_pavg, sourcepower, sourcepower_avg,
   sourcepower_pavg, spline, splitstring, sqrt, sroughness, stackdipole,
   stackfield, stackpurcell, stackrt, std, stepimport, stlimport, str2num,
   struct, substring, sum, svd, switchtodesign, switchtolayout, system

T: touchstoneload, transmission, transmission_avg, transmission_pavg,
   transpose, try

V: vectorplot, version, versionfile, visualize, vtksave

W: wizardgetdata, wizardoption, wizardwidget, workspace, write

Z: zbfwrite, zeros
```

## Configuration

### Rate Limiting Settings
```python
# scrape_one_command.py implicit settings
SLEEP_SUCCESS = 60    # Seconds between successful scrapes
SLEEP_FAILURE = 120   # Seconds after failed attempts
MAX_RETRIES = 3       # Maximum retry attempts per command
```

### Cloudflare Bypass Strategy
1. **Primary**: `cloudscraper` with exponential backoff (30-150s timeout)
2. **Fallback**: Selenium WebDriver with Chrome in headless mode
3. **User-Agent rotation**: Automatic through cloudscraper
4. **Request spacing**: Minimum 60 seconds between requests

### File Structure
```
packages/lumpy/
├── scripts/
│   ├── scrape_one_command.py     # Main single-command scraper
│   ├── sleep_script.py           # Interval controller
│   ├── scrape_missing_lsf_docs.py # Batch scraper
│   └── update_lsf_docs_resume.py  # Original batch scraper
├── docs/
│   ├── lsf-script/               # Generated Markdown files (*.md)
│   ├── missing-lsf-script-docs.md # Auto-updated missing commands
│   ├── scrape-progress.json      # Progress tracking
│   └── scrape-single.log         # Log file
└── requirements.txt              # Dependencies
```

## Operation Guide

### Starting Fresh
```bash
# 1. Install dependencies
uv venv lsf-scraping-env
source lsf-scraping-env/Scripts/activate  # Windows: lsf-scraping-env\Scripts\activate
pip install cloudscraper beautifulsoup4 html2text selenium webdriver-manager

# 2. Check current status
python scripts/scrape_one_command.py --stats

# 3. List missing commands
python scripts/scrape_one_command.py --list
```

### Continuing from Current State
```bash
# Single command mode (recommended - safest)
python scripts/scrape_one_command.py --next
python scripts/sleep_script.py
# Repeat these two commands for each command

# Batch mode (risky - may trigger Cloudflare)
python scripts/scrape_missing_lsf_docs.py --limit 5
```

### Monitoring Progress
```bash
# Check statistics
python scripts/scrape_one_command.py --stats

# View log file
tail -f docs/scrape-single.log

# Count generated files
ls docs/lsf-script/ | wc -l

# Check last processed commands
tail -5 docs/scrape-single.log
```

### Manual Commands
```bash
# Scrape specific command
python scripts/scrape_one_command.py "seteigensolver"

# Wait custom time
python scripts/sleep_script.py 90  # Wait 90 seconds
python scripts/sleep_script.py --minutes 2  # Wait 2 minutes
```

## Safety Guidelines

### Critical Rules
1. **Never reduce wait time below 60 seconds** - Will trigger Cloudflare blocking
2. **Always use `--next` for single commands** - Maintains alphabetical order
3. **Monitor log file regularly** - Check for Cloudflare errors
4. **Stop immediately if errors appear** - Switch to longer intervals

### Cloudflare Triggers
- **Signs of blocking**: HTTP 403, 429, or Cloudflare challenge pages
- **Recovery**: Increase wait time to 120+ seconds, use Selenium fallback
- **Prevention**: Maintain 60-second minimum between requests

### Session Management
- Progress is automatically saved after each successful scrape
- Missing command list auto-updates after each success
- No manual file editing required

## Troubleshooting

### Common Issues

**1. Cloudflare Blocking**
```bash
# Symptoms: HTTP 403/429, "Checking your browser" messages
# Solution: Increase wait time
python scripts/sleep_script.py 120  # Wait 2 minutes
# Then retry with Selenium fallback (automatic)
```

**2. Missing Chrome Driver**
```bash
# Install Chrome and ChromeDriver
# Or use cloudscraper-only mode by modifying fetch_page() to skip Selenium
```

**3. Network Timeouts**
```bash
# Increase timeout in update_lsf_docs_resume.py
timeout = 60 * (attempt + 1)  # Increase from 30 to 60
```

**4. Progress File Corruption**
```bash
# Backup and regenerate from missing commands list
cp docs/scrape-progress.json docs/scrape-progress.json.backup
# Manually edit if needed
```

### Debug Mode
To enable verbose logging, modify `scrape_one_command.py`:
```python
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    # ...
)
```

## Performance Metrics

### Time Estimates
- **Per command**: ~60 seconds (scrape + wait)
- **Remaining commands**: 88
- **Estimated completion**: ~1.5 hours (at current pace)
- **Total session time**: ~6 hours (including breaks)

### Success Metrics
- **Current session**: 88 commands scraped, 0 failures
- **Historical**: 14 commands scraped previously
- **Overall success rate**: 100%

## Future Enhancements

### Planned Improvements
1. **Parallel scraping** (with careful rate limiting)
2. **Resume from specific command** (enhanced `--from` option)
3. **HTML to Markdown conversion optimization**
4. **Automatic table formatting** for syntax sections
5. **Link validation** for cross-references

### Integration
- Convert to searchable documentation website
- Add command index with categories
- Generate API reference for IDE integration

---

## Quick Start for New Project

### Initial Setup
```bash
# Clone or create new project
git clone <repository> lsf-docs-scraping
cd lsf-docs-scraping

# Set up virtual environment
uv venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install cloudscraper beautifulsoup4 html2text selenium webdriver-manager requests

# Copy essential files
mkdir -p scripts docs/lsf-script
# Copy: scrape_one_command.py, sleep_script.py, scrape_missing_lsf_docs.py
# Copy: missing-lsf-script-docs.md, scrape-progress.json (if resuming)
```

### Resume Scraping
```bash
# 1. Check current status
python scripts/scrape_one_command.py --stats

# 2. Start scraping (recommended method)
while true; do
    python scripts/scrape_one_command.py --next
    python scripts/sleep_script.py
done

# Or use batch mode (limited to 5 commands)
python scripts/scrape_missing_lsf_docs.py --limit 5
```

### Verification
```bash
# Verify scraped content
ls docs/lsf-script/ | wc -l
head -20 docs/lsf-script/set.md

# Check progress
python scripts/scrape_one_command.py --stats
tail -10 docs/scrape-single.log
```

---

**Last Updated**: 2026-02-02  
**Next Action**: Continue with `seteigensolver` command  
**Estimated Completion**: ~1.5 hours remaining