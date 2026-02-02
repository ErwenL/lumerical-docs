#!/usr/bin/env python3
"""
Setup script for LSF documentation scraping environment.
Run this script to configure a new project for scraping.
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: str, description: str) -> bool:
    """Run a shell command and return success status."""
    print(f"⏳ {description}...")
    print(f"   $ {cmd}")

    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed")
            if result.stdout.strip():
                print(f"   Output: {result.stdout[:200]}...")
            return True
        else:
            print(f"❌ {description} failed")
            print(f"   Error: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"❌ {description} failed with exception: {e}")
        return False


def check_prerequisites() -> bool:
    """Check if prerequisites are installed."""
    print("🔍 Checking prerequisites...")

    # Check Python version
    try:
        version_result = subprocess.run(
            [sys.executable, "--version"], capture_output=True, text=True
        )
        if (
            "Python 3.12" in version_result.stdout
            or "Python 3.13" in version_result.stdout
        ):
            print(f"✅ Python version: {version_result.stdout.strip()}")
        else:
            print(f"⚠️  Python version may be too old: {version_result.stdout.strip()}")
            print("   Python 3.12+ recommended")
    except:
        print("❌ Python not found or cannot check version")
        return False

    # Check pip
    if run_command("pip --version", "Check pip installation"):
        print("✅ pip is available")
    else:
        print("❌ pip not found")
        return False

    return True


def install_dependencies() -> bool:
    """Install required Python packages."""
    print("\n📦 Installing dependencies...")

    dependencies = [
        "cloudscraper",
        "beautifulsoup4",
        "html2text",
        "lxml",
        "selenium",
        "webdriver-manager",
        "requests",
    ]

    all_success = True
    for dep in dependencies:
        cmd = f"pip install {dep}"
        if not run_command(cmd, f"Install {dep}"):
            all_success = False

    return all_success


def create_directory_structure() -> bool:
    """Create necessary directories."""
    print("\n📁 Creating directory structure...")

    directories = [
        "docs",
        "docs/lsf-script",
        "scripts",
        "logs",
    ]

    for dir_path in directories:
        dir_obj = Path(dir_path)
        if not dir_obj.exists():
            dir_obj.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created directory: {dir_path}")
        else:
            print(f"📂 Directory already exists: {dir_path}")

    return True


def verify_chrome_installation() -> bool:
    """Check if Chrome is installed (required for Selenium fallback)."""
    print("\n🌐 Checking Chrome installation...")

    # Check common Chrome installation paths
    chrome_paths = [
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
    ]

    chrome_found = False
    for path in chrome_paths:
        if Path(path).exists():
            print(f"✅ Chrome found at: {path}")
            chrome_found = True
            break

    if not chrome_found:
        print("⚠️  Chrome not found in standard locations")
        print("   Selenium fallback may not work")
        print("   Download Chrome from: https://www.google.com/chrome/")

    return True


def create_config_files() -> bool:
    """Create example configuration files."""
    print("\n⚙️  Creating configuration files...")

    # Create example .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environment
.venv/
env/
venv/
ENV/
env.bak/
venv.bak/

# Logs and data
logs/
*.log
*.sql
*.sqlite

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
"""

    try:
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write(gitignore_content)
        print("✅ Created .gitignore")
    except Exception as e:
        print(f"❌ Failed to create .gitignore: {e}")

    return True


def print_next_steps():
    """Print instructions for next steps."""
    print("\n" + "=" * 60)
    print("🚀 SETUP COMPLETE!")
    print("=" * 60)

    print("\n📋 Next Steps:")
    print("1. Copy the scraping scripts to the scripts/ directory:")
    print("   - scrape_one_command.py")
    print("   - sleep_script.py")
    print("   - scrape_missing_lsf_docs.py")
    print("   - update_lsf_docs_resume.py (optional)")

    print("\n2. Copy data files to docs/ directory:")
    print("   - missing-lsf-script-docs.md")
    print("   - scrape-progress.json")

    print("\n3. Start scraping:")
    print("   $ python scripts/scrape_one_command.py --stats")
    print("   $ python scripts/scrape_one_command.py --next")
    print("   $ python scripts/sleep_script.py")
    print("   Repeat the last two commands for each command")

    print("\n4. Monitor progress:")
    print("   $ python scripts/scrape_one_command.py --stats")
    print("   $ tail -f docs/scrape-single.log")

    print("\n📚 Documentation:")
    print("   - See LSF-DOCUMENTATION-SCRAPING-WORKFLOW.md for details")
    print("   - See QUICK-START-SCRAPING.md for quick reference")

    print("\n⚠️  IMPORTANT:")
    print("   - Maintain 60-second intervals between requests")
    print("   - Never reduce wait time below 60 seconds")
    print("   - Monitor for Cloudflare blocking (403/429 errors)")
    print("=" * 60)


def main():
    """Main setup function."""
    print("=" * 60)
    print("LSF Documentation Scraping - Environment Setup")
    print("=" * 60)

    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites not met. Please install Python 3.12+ and pip.")
        sys.exit(1)

    # Install dependencies
    if not install_dependencies():
        print("\n⚠️  Some dependencies failed to install. Check manually.")

    # Create directories
    create_directory_structure()

    # Check Chrome
    verify_chrome_installation()

    # Create config files
    create_config_files()

    # Print next steps
    print_next_steps()

    return 0


if __name__ == "__main__":
    sys.exit(main())
