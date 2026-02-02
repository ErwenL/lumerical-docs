#!/usr/bin/env python3
"""
Script to update Lumerical script command documentation from Ansys Optics website.
"""

import re
import time
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import cloudscraper
import html2text
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
BASE_URL = "https://optics.ansys.com"
INDEX_URL = (
    BASE_URL
    + "/hc/en-us/articles/360034923553-Lumerical-scripting-language-Alphabetical-list"
)
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "lsf-script"
COMMANDS_LIST_FILE = (
    Path(__file__).parent.parent / "docs" / "lsf-script-commands-alphabetical.md"
)
SLEEP_TIME = 1.0  # seconds between requests to be polite


def fetch_page_selenium(url: str) -> Optional[str]:
    """Fetch page using Selenium WebDriver."""
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    try:
        driver.get(url)
        # Wait for page to load
        time.sleep(3)
        html = driver.page_source
        return html
    except Exception as e:
        print(f"Selenium error fetching {url}: {e}")
        return None
    finally:
        driver.quit()


def fetch_page(url: str) -> Optional[str]:
    """Fetch a web page and return its HTML content, bypassing Cloudflare."""
    # First try cloudscraper
    try:
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Cloudscraper failed for {url}: {e}, falling back to selenium")
        return fetch_page_selenium(url)


def parse_index_page(html: str) -> Dict[str, List[Tuple[str, str]]]:
    """
    Parse the index page to extract commands grouped by letter.
    Returns a dict with keys like 'A', 'B', ..., 'Misc', each containing
    a list of (command_name, command_url) tuples.
    """
    soup = BeautifulSoup(html, "html.parser")
    commands_by_letter = {}
    # Find all h2 headings
    h2s = soup.find_all("h2")
    pattern = re.compile(r"/hc/en-us/articles/\d+-[a-zA-Z0-9_-]+")
    for i, h2 in enumerate(h2s):
        text = h2.get_text(strip=True)
        letter = None
        if len(text) == 1 and text.isalpha():
            letter = text.upper()
        elif "non alphanumeric" in text.lower():
            letter = "Misc"
        elif text.lower() == "misc":
            letter = "Misc"
        else:
            continue
        # Initialize list for this letter
        if letter not in commands_by_letter:
            commands_by_letter[letter] = []
        # Find links between this h2 and next h2
        next_h2 = h2s[i + 1] if i + 1 < len(h2s) else None
        # Collect all <a> tags that match pattern within the same parent container
        # We'll iterate through siblings until we hit next h2
        for sibling in h2.find_next_siblings():
            if sibling.name == "h2" and sibling == next_h2:
                break
            if sibling.name == "a" and sibling.get("href"):
                href = sibling.get("href")
                if pattern.match(href):
                    cmd_name = sibling.get_text(strip=True)
                    if cmd_name:
                        if not href.startswith("http"):
                            href = BASE_URL + href
                        commands_by_letter[letter].append((cmd_name, href))
            # Also look for <a> tags inside other elements like <p>
            for link in sibling.find_all("a", href=pattern):
                href = link.get("href")
                cmd_name = link.get_text(strip=True)
                if cmd_name:
                    if not href.startswith("http"):
                        href = BASE_URL + href
                    commands_by_letter[letter].append((cmd_name, href))
        # Remove duplicates by converting to set and back
        unique = list({(name, url) for name, url in commands_by_letter[letter]})
        unique.sort(key=lambda x: x[0].lower())
        commands_by_letter[letter] = unique
    # Also ensure all letters have entries (even if empty)
    # Sort letters
    return commands_by_letter


def fetch_command_page(url: str) -> Optional[str]:
    """Fetch a command detail page and return its HTML."""
    return fetch_page(url)


def extract_command_content(html: str, command_name: str) -> str:
    """
    Extract the main content of a command detail page and convert to Markdown.
    """
    soup = BeautifulSoup(html, "html.parser")
    # Find the main content area - likely a div with class 'article-body' or similar
    main_content = soup.find("div", class_="article-body")
    if not main_content:
        main_content = soup.find("article")
    if not main_content:
        main_content = soup.find("body")
    # Convert to markdown using html2text
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    markdown = h.handle(str(main_content))
    # Add header
    return f"# {command_name}\n\n{markdown}"


def save_command_markdown(command_name: str, content: str):
    """Save command documentation as a markdown file."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Sanitize filename
    filename = command_name.replace("/", "_").replace("\\", "_").replace(":", "_")
    filepath = OUTPUT_DIR / f"{filename}.md"
    filepath.write_text(content, encoding="utf-8")
    print(f"Saved {filepath}")


def generate_commands_list_file(commands_by_letter: Dict[str, List[Tuple[str, str]]]):
    """Generate the updated alphabetical list file with letter headings."""
    lines = []
    lines.append("# Lumerical Script Commands (Alphabetical)")
    lines.append("")
    lines.append(f"Source: {INDEX_URL}")
    lines.append("")
    # Sort letters alphabetically, with Misc at the end
    sorted_letters = sorted([l for l in commands_by_letter.keys() if l != "Misc"])
    if "Misc" in commands_by_letter:
        sorted_letters.append("Misc")
    for letter in sorted_letters:
        lines.append(f"## {letter}")
        lines.append("")
        for cmd_name, cmd_url in commands_by_letter[letter]:
            # Create a relative link to the local markdown file if exists
            # For now, just list the command with link to original URL
            lines.append(f"- [{cmd_name}]({cmd_url})")
        lines.append("")
    COMMANDS_LIST_FILE.parent.mkdir(parents=True, exist_ok=True)
    COMMANDS_LIST_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Updated {COMMANDS_LIST_FILE}")


def main():
    dry_run = False  # Set to False to fetch all command pages
    test_mode = False  # If True, only fetch first 3 commands per letter
    max_commands_per_letter = 3 if test_mode else None
    print("Fetching index page...")
    html = fetch_page(INDEX_URL)
    if not html:
        print("Failed to fetch index page.")
        return
    print("Parsing index page...")
    commands_by_letter = parse_index_page(html)
    # Print statistics
    total = sum(len(cmds) for cmds in commands_by_letter.values())
    print(f"Found {total} commands across {len(commands_by_letter)} letters.")
    if dry_run:
        # Debug: print first few commands per letter
        for letter, commands in commands_by_letter.items():
            print(f"{letter}: {len(commands)} commands")
            for cmd_name, cmd_url in commands[:3]:
                print(f"  - {cmd_name}: {cmd_url}")
            if len(commands) > 3:
                print(f"  ... and {len(commands) - 3} more")
        print("Dry run completed. Set dry_run=False to fetch command pages.")
        # Still generate commands list file
        generate_commands_list_file(commands_by_letter)
        return
    # Fetch each command page and save documentation
    for letter, commands in commands_by_letter.items():
        print(f"Processing letter {letter} ({len(commands)} commands)...")
        if max_commands_per_letter:
            commands = commands[:max_commands_per_letter]
        for cmd_name, cmd_url in commands:
            print(f"  Fetching {cmd_name}...")
            cmd_html = fetch_command_page(cmd_url)
            if cmd_html:
                content = extract_command_content(cmd_html, cmd_name)
                save_command_markdown(cmd_name, content)
            else:
                print(f"    Failed to fetch {cmd_name}")
            time.sleep(SLEEP_TIME)  # be polite
    # Generate the updated commands list file
    generate_commands_list_file(commands_by_letter)
    print("Done.")


if __name__ == "__main__":
    main()
