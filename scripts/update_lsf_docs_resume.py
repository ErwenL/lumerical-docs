#!/usr/bin/env python3
"""
恢复版本的LSF脚本命令文档抓取脚本。
支持从上次中断处继续抓取。
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
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "lsf-script" / "en"
COMMANDS_LIST_FILE = (
    Path(__file__).parent.parent / "docs" / "lsf-script-commands-alphabetical.md"
)
SLEEP_TIME = 30.0  # 增加等待时间，避免请求过载

# Markdown formatting configuration
ENABLE_MARKDOWN_FORMAT = True  # 是否启用Markdown格式化

# 恢复配置
RESUME_FROM_LETTER = "P"  # 从字母P开始
RESUME_SKIP_UNTIL_COMMAND = None  # 不跳过任何命令
SKIP_EXISTING_FILES = True  # 跳过已存在的文件


def fetch_page_selenium(url: str) -> Optional[str]:
    """Fetch page using Selenium WebDriver."""
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # 添加更多选项避免检测
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    try:
        driver.get(url)
        # 增加等待时间，使用隐式等待
        driver.implicitly_wait(10)
        # 额外固定等待
        time.sleep(5)
        html = driver.page_source
        return html
    except Exception as e:
        print(f"Selenium error fetching {url}: {e}")
        return None
    finally:
        driver.quit()


def fetch_page(url: str) -> Optional[str]:
    """Fetch a web page and return its HTML content, bypassing Cloudflare."""
    # 重试逻辑
    max_retries = 5
    for attempt in range(max_retries):
        # First try cloudscraper
        try:
            scraper = cloudscraper.create_scraper()
            # 增加超时时间
            timeout = 30 * (attempt + 1)  # 30, 60, 90, 120, 150 seconds
            print(
                f"Cloudscraper attempt {attempt + 1}/{max_retries} with timeout {timeout}s..."
            )
            response = scraper.get(url, timeout=timeout)
            response.raise_for_status()
            print(f"Successfully fetched {url}")
            return response.text
        except Exception as e:
            print(
                f"Cloudscraper attempt {attempt + 1}/{max_retries} failed for {url}: {e}"
            )
            if attempt < max_retries - 1:
                wait_time = 10 * (attempt + 1)  # 10, 20, 30, 40 seconds
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
            else:
                print(
                    "All cloudscraper attempts failed, trying selenium as fallback..."
                )
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


def sanitize_filename(name: str) -> str:
    """将命令名转换为安全的文件名。"""
    original_name = name  # 保存原始名称用于哈希

    # 多字符组合替换 - 先执行，避免被单字符替换拆散
    multi_char_replacements = {
        "<=": "lte",
        ">=": "gte",
        "==": "equalequal",
        "!=": "notequal",
        "+=": "plusequals",
        "-=": "minusequals",
        "*=": "asteriskequals",
        "/=": "slashequals",
    }
    for combo, replacement in multi_char_replacements.items():
        name = name.replace(combo, replacement)

    # 替换其他可能有问题字符 - 先执行这个，确保特殊字符被正确替换
    replacements = {
        "!": "exclamation",
        '"': "quote",
        "#": "hash",
        "$": "dollar",
        "%": "percent",
        "&": "ampersand",
        "'": "apostrophe",
        "(": "lparen",
        ")": "rparen",
        "*": "asterisk",
        "+": "plus",
        ",": "comma",
        "-": "minus",
        ".": "dot",
        "/": "slash",
        ":": "colon",
        ";": "semicolon",
        "<": "lt",
        "=": "equals",
        ">": "gt",
        "?": "question",
        "@": "at",
        "[": "lbracket",
        "\\": "backslash",
        "]": "rbracket",
        "^": "caret",
        "`": "backtick",
        "{": "lbrace",
        "|": "pipe",
        "}": "rbrace",
        "~": "tilde",
        " ": "_",
    }

    for char, replacement in replacements.items():
        name = name.replace(char, replacement)

    # 然后替换Windows文件名中的非法字符（可能已被替换）
    illegal_chars = r'<>:"/\\|?*'
    for char in illegal_chars:
        name = name.replace(char, "_")

    # 如果文件名仍然以点开头，添加前缀
    if name.startswith("."):
        name = "dot" + name

    # 如果文件名为空或太长，使用哈希
    if not name:
        import hashlib

        name = hashlib.md5(original_name.encode()).hexdigest()[:8]

    return name


def format_markdown_file(filepath: Path) -> bool:
    """Format a markdown file using mdformat with tables plugin.
    
    Returns True if formatting succeeded or was skipped, False on error.
    """
    if not ENABLE_MARKDOWN_FORMAT:
        return True
    try:
        import subprocess
        import sys
        
        # 使用mdformat命令行工具格式化文件
        result = subprocess.run(
            [sys.executable, "-m", "mdformat", str(filepath), "--wrap", "88"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            print(f"mdformat failed for {filepath}: {result.stderr}")
            return False
        print(f"Formatted {filepath}")
        return True
    except Exception as e:
        print(f"Error formatting {filepath}: {e}")
        return False


def save_command_markdown(command_name: str, content: str):
    """Save command documentation as a markdown file."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Sanitize filename
    filename = sanitize_filename(command_name)
    filepath = OUTPUT_DIR / f"{filename}.md"
    filepath.write_text(content, encoding="utf-8")
    print(f"Saved {command_name} -> {filepath}")
    
    # 格式化Markdown文件
    format_markdown_file(filepath)


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


def file_exists_for_command(command_name: str) -> bool:
    """检查命令对应的文件是否已存在。"""
    filename = sanitize_filename(command_name)
    filepath = OUTPUT_DIR / f"{filename}.md"
    return filepath.exists()


def main():
    dry_run = False  # Set to False to fetch all command pages
    test_mode = False  # If True, only fetch first 3 commands per letter
    max_commands_per_letter = 3 if test_mode else None

    print("=" * 60)
    print("LSF Script 文档恢复抓取")
    print(f"恢复配置: 从字母 '{RESUME_FROM_LETTER}' 开始")
    if RESUME_SKIP_UNTIL_COMMAND:
        print(f"跳过命令直到: '{RESUME_SKIP_UNTIL_COMMAND}'")
    print(f"跳过已存在文件: {SKIP_EXISTING_FILES}")
    print("=" * 60)

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

    # 统计已存在的文件
    existing_count = 0
    if SKIP_EXISTING_FILES:
        for letter, commands in commands_by_letter.items():
            for cmd_name, _ in commands:
                if file_exists_for_command(cmd_name):
                    existing_count += 1
        print(f"发现 {existing_count} 个已存在的文档文件。")

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

    # 恢复逻辑：找到起始字母
    started = False
    if RESUME_FROM_LETTER is None:
        started = True  # 从头开始

    # Fetch each command page and save documentation
    for letter, commands in commands_by_letter.items():
        # 检查是否到达起始字母
        if not started:
            if letter == RESUME_FROM_LETTER:
                started = True
                print(f"到达起始字母: {letter}")
            else:
                print(f"跳过字母: {letter} ({len(commands)} commands)")
                continue

        print(f"处理字母 {letter} ({len(commands)} 个命令)...")

        if max_commands_per_letter:
            commands = commands[:max_commands_per_letter]

        # 在字母内跳过直到指定命令
        skip_in_letter = RESUME_SKIP_UNTIL_COMMAND is not None

        for cmd_name, cmd_url in commands:
            # 检查是否需要跳过该命令
            if skip_in_letter:
                if (
                    RESUME_SKIP_UNTIL_COMMAND
                    and cmd_name.lower() == RESUME_SKIP_UNTIL_COMMAND.lower()
                ):
                    print(f"  到达起始命令: {cmd_name}")
                    skip_in_letter = False
                else:
                    print(f"  跳过命令: {cmd_name}")
                    continue

            # 检查文件是否已存在
            if SKIP_EXISTING_FILES and file_exists_for_command(cmd_name):
                print(f"  跳过已存在的文件: {cmd_name}")
                continue

            print(f"  抓取 {cmd_name}...")
            cmd_html = fetch_command_page(cmd_url)
            if cmd_html:
                content = extract_command_content(cmd_html, cmd_name)
                save_command_markdown(cmd_name, content)
            else:
                print(f"    抓取失败: {cmd_name}")

            time.sleep(SLEEP_TIME)  # be polite

    # Generate the updated commands list file
    generate_commands_list_file(commands_by_letter)

    # 最终统计
    print("=" * 60)
    print("抓取完成!")
    if SKIP_EXISTING_FILES:
        final_count = sum(1 for _ in OUTPUT_DIR.glob("*.md"))
        print(f"文档总数: {final_count}")
        print(f"本次新增: {final_count - existing_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
