# Agent Guidelines for Lumerical Documentation Scraping Project

This document provides guidelines for AI agents working on this Python-based web scraping project. The project scrapes Lumerical scripting command documentation from the Ansys Optics website.

## Project Overview

- **Language**: Python 3.12+
- **Package Manager**: UV (via `pyproject.toml` and `uv.lock`)
- **Dependencies**: Cloudscraper, BeautifulSoup4, html2text, lxml, selenium, requests, tqdm
- **Development Dependencies**: pytest, ruff
- **Source Structure**: All Python scripts are in the `scripts/` directory; documentation output in `docs/`
- **No existing test suite** – tests should be added in a `tests/` directory following pytest conventions
- **Cursor/Copilot rules**: None currently; add to `.cursor/rules/` or `.github/copilot-instructions.md` if needed.

## Build, Lint, and Test Commands

### Dependency Management

```bash
# Install dependencies (uses uv.lock)
uv sync

# Add a new production dependency
uv add <package>

# Add a new development dependency
uv add --dev <package>
```

**Note**: The package currently fails to build due to missing `src/lumpy/__init__.py`. For development dependencies (ruff, pytest), you can install them directly via `pip install -r requirements.txt`.

### Linting and Formatting

The project uses **Ruff** for both linting and formatting. Configuration is currently minimal; you can add a `ruff.toml` if more rules are needed.

**Note**: The package currently fails to build due to missing `src/lumpy/__init__.py`. Use the direct `ruff` command (installed globally) or install dev dependencies with `pip install -r requirements.txt` and run ruff via the virtual environment.

```bash
# Run linting (check code for errors)
ruff check .

# Run linting with auto-fix
ruff check --fix .

# Format all Python files (Ruff's formatter)
ruff format .

# Check formatting without applying changes
ruff format --check .
```

If the package structure is fixed, you can use `uv run`:

```bash
uv run ruff check .
uv run ruff check --fix .
uv run ruff format .
uv run ruff format --check .
```

### Testing

The project includes **pytest** as a dev dependency. Currently there are no formal test files; create them in a `tests/` directory.

**Note**: Use direct `pytest` command (installed globally) or install dev dependencies with `pip install -r requirements.txt` and run pytest via the virtual environment.

```bash
# Run all tests
pytest

# Run tests in a specific file
pytest scripts/test_fetch.py -v

# Run tests matching a pattern
pytest -k "fetch"

# Run tests with coverage (install pytest-cov first)
pytest --cov=scripts --cov-report=html
```

If the package structure is fixed, you can use `uv run`:

```bash
uv run pytest
uv run pytest scripts/test_fetch.py -v
uv run pytest -k "fetch"
uv run pytest --cov=scripts --cov-report=html
```

### Running Scripts

All main scripts are in the `scripts/` directory. Use the Python module directly or via uv:

**Note**: `uv run` may fail due to the package build issue. Use direct `python` invocation if needed.

```bash
# Run a script with uv (may fail due to build)
uv run python scripts/scrape_one_command.py --list

# Or directly (if dependencies are installed)
python scripts/scrape_one_command.py --next
```

### Environment Setup

```bash
# Create a virtual environment (UV does this automatically)
uv venv

# Activate the virtual environment (Windows)
.venv\Scripts\activate

# Activate (Unix)
source .venv/bin/activate
```

### Translation Helper Script

A new script `translation_helper.py` has been added to manage the English-to-Chinese documentation translation workflow.

**Usage**:
```bash
# Show translation statistics
python scripts/translation_helper.py --stats

# List untranslated commands (first 20)
python scripts/translation_helper.py --list

# List all untranslated commands
python scripts/translation_helper.py --list --all

# Prepare template for a specific command
python scripts/translation_helper.py --prepare addmaterial

# Prepare template with overwrite
python scripts/translation_helper.py --prepare addmaterial --overwrite

# Generate detailed progress report
python scripts/translation_helper.py --report
```

**Features**:
- Tracks translation progress between `docs/lsf-script/en/` and `docs/lsf-script/cn/`
- Creates templates with translation metadata headers
- Generates JSON progress reports at `docs/translation-progress.json`
- Shows real-time statistics and recommendations

**Workflow**:
1. Use `--list` to identify untranslated commands
2. Use `--prepare <command>` to create a template
3. Edit the generated Chinese file in `docs/lsf-script/cn/`
4. Use `--stats` to track progress
5. Use `--report` to generate detailed progress data

## Code Style Guidelines

### General Principles

1. **Readability over cleverness** – Write code that is easy to understand and maintain.
2. **Consistency** – Follow existing patterns in the codebase.
3. **Defensive programming** – Assume network failures, missing data, and edge cases.
4. **Explicit error handling** – Use try/except blocks with specific exception types and log errors.

### Python Version

- Target Python 3.12 or higher (as specified in `pyproject.toml`).
- Use modern Python features (type hints, pathlib, f‑strings) where appropriate.

### Imports

- Group imports in the following order, with a blank line between groups:
  1. Standard library imports
  2. Third‑party imports
  3. Local application imports (none currently, but keep the pattern)
- Use absolute imports.
- Avoid wildcard imports (`from module import *`).
- Keep imports at the top of the file, after the module docstring.

Example:
```python
import json
import logging
import re
from pathlib import Path
from typing import Optional, Tuple

import requests
import cloudscraper
from bs4 import BeautifulSoup

# Local imports (if any)
# from .utils import helper
```

### Type Hints

- **Always** add type hints for function arguments and return values.
- Use the `typing` module for generic types (`List`, `Dict`, `Optional`, `Tuple`, etc.).
- For simple return types, use the built‑in `|` syntax (Python 3.10+) or `Union`.

Examples:
```python
def fetch_page(url: str) -> str | None:
    ...

def load_missing_commands() -> list[tuple[str, str]]:
    ...
```

### Naming Conventions

- **Variables & functions**: `snake_case`
- **Classes**: `CamelCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private module members**: prefix with `_` (e.g., `_internal_helper`)
- Use descriptive names that indicate purpose (e.g., `missing_commands_file` not `mcf`).

### String Quotes

- Use **double quotes** (`"`) for string literals and f‑strings.
- Use triple double quotes for docstrings.
- Single quotes may be used inside strings if needed to avoid escaping.

### Error Handling and Logging

- Use `try`/`except` blocks around operations that can fail (network requests, file I/O, parsing).
- Catch specific exceptions (`requests.exceptions.RequestError`, `FileNotFoundError`) rather than bare `except:`.
- Log errors with the standard `logging` module:
  - Each module should define `logger = logging.getLogger(__name__)`.
  - Use appropriate log levels: `debug` for detailed info, `info` for normal events, `warning` for recoverable issues, `error` for failures.
  - Include relevant context in log messages (command name, URL, file path).

Example:
```python
import logging

logger = logging.getLogger(__name__)

def scrape_command(command: str, url: str) -> bool:
    logger.info(f"Starting scrape for {command}")
    try:
        html = fetch_page(url)
        if not html:
            logger.error(f"Failed to fetch page for {command}")
            return False
        # ...
    except requests.exceptions.Timeout as e:
        logger.error(f"Request timeout for {command}: {e}")
        return False
```

### Docstrings

- Write docstrings for all public functions, classes, and modules.
- Use triple‑double‑quoted strings with a one‑line summary followed by a blank line and a more detailed description.
- Mention parameters, return values, and raised exceptions (Google‑style or reStructuredText are acceptable).

Example:
```python
def load_missing_commands() -> list[tuple[str, str]]:
    """Load the list of missing commands from the Markdown tracking file.

    Returns:
        A list of (command_name, url) tuples parsed from the missing‑commands file.
        Returns an empty list if the file cannot be read or parsed.
    """
```

### Line Length and Formatting

- Aim for a maximum line length of 88 characters (Ruff’s default).
- Let Ruff’s formatter handle line breaks and indentation.
- Use parentheses for implicit line continuation when needed.

### Path Handling

- Use `pathlib.Path` for all file‑system operations.
- Construct paths relative to `__file__` or the project root; avoid hard‑coded absolute paths.

Example:
```python
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "lsf-script"
```

### Main Block Pattern

- Every executable script should end with:
```python
if __name__ == "__main__":
    main()
```
- Use `argparse` for command‑line argument parsing.

## Workflow for Agents

1. **Before making changes**, run `ruff check .` to ensure the codebase passes linting.
2. **After implementing a feature**, run the relevant scripts to verify they still work.
3. **If adding new functionality**, consider writing tests in a `tests/` directory.
4. **Before finishing**, run `ruff format .` to keep the code style consistent.
5. **If the change affects documentation**, update the appropriate Markdown files in `docs/`.

## Notes for Future Development

- The project currently lacks a formal test suite; adding unit tests for scraping functions is highly encouraged.
- Consider adding a `ruff.toml` or `pyproject.toml` [tool.ruff] section to enforce stricter linting rules.
- The scraping logic relies on third‑party libraries that may break if the target website changes; keep fallback mechanisms (like Selenium) robust.

---

*This file was generated by an AI agent based on analysis of the existing codebase. Update it as the project evolves.*