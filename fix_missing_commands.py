#!/usr/bin/env python3
"""修复因文件名冲突而缺失的命令文档"""

import re
import time
from pathlib import Path
from typing import List, Tuple
import cloudscraper
from bs4 import BeautifulSoup
import html2text

# 配置文件
INDEX_FILE = Path(__file__).parent / "docs" / "lsf-script-commands-alphabetical.md"
OUTPUT_DIR = Path(__file__).parent / "docs" / "lsf-script"
SLEEP_TIME = 10  # 每次请求间隔10秒

# 冲突命令列表（根据分析结果）
# 格式: (命令名, URL, 当前文件名, 新文件名)
CONFLICT_COMMANDS = [
    # dot.md 冲突
    (
        "dot",
        "https://optics.ansys.com/hc/en-us/articles/360034925773-dot",
        "dot.md",
        "dot_cmd.md",
    ),
    # _.md 冲突（除了已存在的 " 命令）
    (
        "*",
        "https://optics.ansys.com/hc/en-us/articles/360034930833--",
        "_.md",
        "asterisk.md",
    ),
    (
        "/",
        "https://optics.ansys.com/hc/en-us/articles/360034930853--",
        "_.md",
        "slash.md",
    ),
    (
        ":",
        "https://optics.ansys.com/hc/en-us/articles/360034929533--",
        "_.md",
        "colon.md",
    ),
    ("<", "https://optics.ansys.com/hc/en-us/articles/360034410334--", "_.md", "lt.md"),
    (">", "https://optics.ansys.com/hc/en-us/articles/360034930953--", "_.md", "gt.md"),
    (
        "?",
        "https://optics.ansys.com/hc/en-us/articles/360034410434--",
        "_.md",
        "question.md",
    ),
    (
        "|",
        "https://optics.ansys.com/hc/en-us/articles/360034410374--",
        "_.md",
        "pipe.md",
    ),
    # _equals.md 冲突
    (
        ">=",
        "https://optics.ansys.com/hc/en-us/articles/360034930933--",
        "_equals.md",
        "gte.md",
    ),
]


def fetch_page(url: str) -> str:
    """使用cloudscraper获取页面内容"""
    scraper = cloudscraper.create_scraper()
    for attempt in range(1, 6):
        try:
            print(f"Cloudscraper attempt {attempt}/5 with timeout 30s...")
            response = scraper.get(url, timeout=30)
            response.raise_for_status()
            print(f"Successfully fetched {url}")
            return response.text
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < 5:
                time.sleep(5)
            else:
                print(f"All cloudscraper attempts failed for {url}")
                raise

    raise Exception("Failed to fetch page")


def extract_command_content(html: str, command_name: str) -> str:
    """从HTML中提取命令文档内容并转换为Markdown"""
    soup = BeautifulSoup(html, "lxml")

    # 查找文章内容
    article = soup.find("article")
    if not article:
        article = soup.find("div", class_="article-body")

    if not article:
        # 尝试其他选择器
        article = soup.find("div", class_="article-content")

    if not article:
        # 作为后备，使用整个body
        article = soup.body

    # 转换HTML为Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_tables = False
    h.body_width = 0

    markdown = h.handle(str(article))

    # 清理多余的空白行
    markdown = re.sub(r"\n\s*\n\s*\n", "\n\n", markdown)

    # 添加标题
    return f"# {command_name}\n\n{markdown}"


def save_command_markdown(command_name: str, content: str, filename: str):
    """保存命令文档到文件"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filepath = OUTPUT_DIR / filename
    filepath.write_text(content, encoding="utf-8")
    print(f"Saved {command_name} -> {filepath}")


def main():
    print("开始修复因文件名冲突而缺失的命令文档...")
    print("=" * 60)

    total = len(CONFLICT_COMMANDS)
    success_count = 0
    failed_commands = []

    for idx, (cmd_name, cmd_url, current_file, new_filename) in enumerate(
        CONFLICT_COMMANDS, 1
    ):
        print(f"\n处理命令 {idx}/{total}: {cmd_name}")
        print(f"URL: {cmd_url}")
        print(f"当前文件: {current_file}, 新文件: {new_filename}")

        # 检查是否已存在新文件（避免重复抓取）
        new_filepath = OUTPUT_DIR / new_filename
        if new_filepath.exists():
            print(f"文件 {new_filename} 已存在，跳过")
            success_count += 1
            continue

        try:
            # 抓取页面
            html = fetch_page(cmd_url)

            # 提取内容
            content = extract_command_content(html, cmd_name)

            # 保存文档
            save_command_markdown(cmd_name, content, new_filename)

            success_count += 1
            print(f"成功抓取并保存 {cmd_name}")

            # 等待一段时间，避免请求过载
            if idx < total:
                print(f"等待 {SLEEP_TIME} 秒后处理下一个命令...")
                time.sleep(SLEEP_TIME)

        except Exception as e:
            print(f"处理命令 {cmd_name} 时出错: {e}")
            failed_commands.append((cmd_name, str(e)))

    print("\n" + "=" * 60)
    print("修复任务完成")
    print(f"成功: {success_count}/{total}")
    print(f"失败: {len(failed_commands)}/{total}")

    if failed_commands:
        print("\n失败的命令:")
        for cmd_name, error in failed_commands:
            print(f"  - {cmd_name}: {error}")

    # 更新验证结果
    print("\n验证修复后的完整性...")
    existing_files = list(OUTPUT_DIR.glob("*.md"))
    print(f"修复后文档总数: {len(existing_files)}")

    # 检查冲突是否已解决
    conflict_files = ["dot.md", "_.md", "_equals.md"]
    for cf in conflict_files:
        cf_path = OUTPUT_DIR / cf
        if cf_path.exists():
            print(f"注意: 冲突文件 {cf} 仍然存在，但已为其他命令创建了新文件")


if __name__ == "__main__":
    main()
