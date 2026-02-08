#!/usr/bin/env python3
"""
测试文档优化功能
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.optimize_documentation import (
    Config,
    CommandMapper,
    DocumentProcessor,
    FilenameEncoder,
    LinkConverter,
    LinkRecognizer,
)


def test_filename_encoding():
    """测试文件名编码/解码"""
    print("测试文件名编码/解码...")

    test_cases = [
        ("abs", "abs.md"),
        ("addmaterial", "addmaterial.md"),
        ("dot", "dot_cmd.md"),
        (".", "dot.md"),
        ("addport (FDTD)", "addport_lparenFDTDrparen.md"),
        ("!=", "exclamationequals.md"),
        ("<=", "lte.md"),
        (">=", "gte.md"),
        ("==", "equalsequals.md"),
    ]

    for command, expected_filename in test_cases:
        filename = FilenameEncoder.command_to_filename(command) + ".md"
        decoded = FilenameEncoder.filename_to_command(filename[:-3])  # 去掉.md

        status = "[OK]" if filename == expected_filename else "[FAIL]"
        print(f"  {status} {command:20} -> {filename:35} (解码: {decoded})")

        if filename != expected_filename:
            print(f"    预期: {expected_filename}")


def test_link_recognition():
    """测试链接识别"""
    print("\n测试链接识别...")

    recognizer = LinkRecognizer()

    test_links = [
        ("/hc/en-us/articles/360034925553-abs", "命令链接"),
        ("/hc/en-us/articles/360037228834", "命令列表链接"),
        ("/hc/en-us/articles/360034394634-Material-Permittivity-Models", "文章链接"),
        ("https://optics.ansys.com/hc/en-us/articles/360034925553-abs", "完整命令链接"),
        ("./real.md", "本地链接"),
        ("#example", "锚点链接"),
        ("https://example.com", "外部链接"),
    ]

    for url, description in test_links:
        link_type = recognizer.identify_link(url)
        print(f"  {url:60} -> {link_type.value:15} ({description})")


def test_command_mapping():
    """测试命令映射"""
    print("\n测试命令映射...")

    mapper = CommandMapper()
    if not mapper.build_from_index():
        print("  错误: 无法构建命令映射")
        return

    test_commands = ["abs", "addmaterial", "dot", "addport (FDTD)"]

    for cmd in test_commands:
        info = mapper.get_command_info(cmd)
        if info:
            print(f"  [OK] {cmd:20} -> {info.filename}")
            print(f"     官方URL: {info.official_url[:50]}...")
            print(f"     本地路径: {info.local_path}")
        else:
            print(f"  [FAIL] {cmd:20} -> 未找到映射")


def test_single_file(filepath: Path):
    """测试处理单个文件"""
    print(f"\n测试处理文件: {filepath.name}")

    if not filepath.exists():
        print(f"  文件不存在: {filepath}")
        return

    # 构建命令映射
    mapper = CommandMapper()
    if not mapper.build_from_index():
        print("  错误: 无法构建命令映射")
        return

    # 处理文件
    processor = DocumentProcessor(mapper)
    result = processor.process_file(filepath)

    print(f"  命令: {result.command_name}")
    print(f"  找到链接: {result.links_found}")
    print(f"  转换链接: {result.links_converted}")
    print(f"  格式化: {'成功' if result.formatting_success else '失败'}")

    if result.error:
        print(f"  错误: {result.error}")

    # 显示文件前几行
    content = filepath.read_text(encoding="utf-8")
    lines = content.splitlines()[:10]
    print(f"  文件前10行:")
    for i, line in enumerate(lines, 1):
        print(f"    {i:2}: {line[:80]}{'...' if len(line) > 80 else ''}")


def main():
    """主测试函数"""
    print("=" * 60)
    print("文档优化功能测试")
    print("=" * 60)

    # 测试文件名编码
    test_filename_encoding()

    # 测试链接识别
    test_link_recognition()

    # 测试命令映射
    test_command_mapping()

    # 测试处理特定文件
    test_files = [
        Config.DOCS_EN_DIR / "abs.md",
        Config.DOCS_EN_DIR / "addmaterial.md",
        Config.DOCS_EN_DIR / "dot_cmd.md",
        Config.DOCS_EN_DIR / "addport_lparenFDTDrparen.md",
        Config.DOCS_EN_DIR / "real.md",
    ]

    for filepath in test_files:
        test_single_file(filepath)

    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
