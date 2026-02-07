#!/usr/bin/env python3
"""恢复被错误处理的翻译文件到原始英文状态。"""

import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
EN_DOCS_DIR = PROJECT_ROOT / "docs" / "lsf-script" / "en"
CN_DOCS_DIR = PROJECT_ROOT / "docs" / "lsf-script" / "cn"


def analyze_problem_files() -> List[Tuple[str, str]]:
    """分析有问题的文件。"""
    problem_files = []
    
    if not CN_DOCS_DIR.exists():
        print("中文文档目录不存在")
        return problem_files
    
    cn_files = list(CN_DOCS_DIR.glob("*.md"))
    
    for cn_file in cn_files:
        try:
            with open(cn_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否有乱码字符
            weird_chars = ['在', '到', '和', '是', '从', '这', '将', '以', '而', '但']
            weird_count = sum(1 for char in content if char in weird_chars)
            chinese_char_count = sum(1 for char in content if '\u4e00' <= char <= '\u9fff')
            
            # 检查文件头是否被修改
            header_modified = "Translation completed:" in content
            
            # 如果有大量乱码字符或标题被修改，标记为问题文件
            if weird_count > 10 or header_modified:
                problem_files.append((cn_file.stem, "需要恢复"))
                
        except Exception as e:
            print(f"分析文件失败 {cn_file.name}: {e}")
    
    return problem_files


def restore_file(command: str, backup: bool = True) -> bool:
    """恢复单个文件到原始英文状态。
    
    Args:
        command: 命令名称
        backup: 是否创建备份
        
    Returns:
        是否成功
    """
    en_file = EN_DOCS_DIR / f"{command}.md"
    cn_file = CN_DOCS_DIR / f"{command}.md"
    
    if not en_file.exists():
        print(f"英文文件不存在: {en_file}")
        return False
    
    if not cn_file.exists():
        print(f"中文文件不存在: {cn_file}")
        return False
    
    try:
        # 读取英文内容
        with open(en_file, 'r', encoding='utf-8') as f:
            en_content = f.read()
        
        # 如果需要，创建备份
        if backup:
            backup_file = CN_DOCS_DIR / f"{command}.backup.md"
            with open(cn_file, 'r', encoding='utf-8') as f:
                cn_content = f.read()
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(cn_content)
            print(f"已创建备份: {backup_file.name}")
        
        # 创建新的中文文件（只包含翻译头信息）
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"""<!--
待翻译文档
原始命令: {command}
恢复日期: {timestamp}
需要手动翻译
-->

# {command}

"""
        
        # 写入恢复后的文件
        with open(cn_file, 'w', encoding='utf-8') as f:
            f.write(header)
            f.write(en_content)
        
        print(f"已恢复: {command}")
        return True
        
    except Exception as e:
        print(f"恢复文件失败 {command}: {e}")
        return False


def restore_all_problem_files(backup: bool = True) -> None:
    """恢复所有有问题的文件。"""
    problem_files = analyze_problem_files()
    
    if not problem_files:
        print("未发现需要恢复的问题文件")
        return
    
    print(f"发现 {len(problem_files)} 个需要恢复的文件")
    
    restored_count = 0
    failed_count = 0
    
    for i, (command, reason) in enumerate(problem_files, 1):
        print(f"恢复 ({i}/{len(problem_files)}): {command} - {reason}")
        
        if restore_file(command, backup):
            restored_count += 1
        else:
            failed_count += 1
    
    print(f"\n恢复完成:")
    print(f"成功恢复: {restored_count}")
    print(f"恢复失败: {failed_count}")
    print(f"总计: {len(problem_files)}")


def restore_specific_files(commands: List[str], backup: bool = True) -> None:
    """恢复指定的文件。"""
    restored_count = 0
    failed_count = 0
    
    for command in commands:
        print(f"恢复: {command}")
        
        if restore_file(command, backup):
            restored_count += 1
        else:
            failed_count += 1
    
    print(f"\n恢复完成:")
    print(f"成功恢复: {restored_count}")
    print(f"恢复失败: {failed_count}")


def main() -> None:
    """主入口函数。"""
    parser = argparse.ArgumentParser(
        description="恢复被错误处理的翻译文件",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 分析问题文件
  python scripts/restore_files.py --analyze
  
  # 恢复所有问题文件
  python scripts/restore_files.py --restore-all
  
  # 恢复指定文件
  python scripts/restore_files.py --restore addcustom addjob
  
  # 恢复但不创建备份
  python scripts/restore_files.py --restore-all --no-backup
        """
    )
    
    # 操作参数
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument(
        "--analyze",
        action="store_true",
        help="分析问题文件但不恢复"
    )
    action_group.add_argument(
        "--restore-all",
        action="store_true",
        help="恢复所有问题文件"
    )
    action_group.add_argument(
        "--restore",
        nargs="+",
        metavar="COMMAND",
        help="恢复指定的命令文件"
    )
    
    # 可选参数
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="不创建备份文件"
    )
    
    args = parser.parse_args()
    
    # 确保目录存在
    CN_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    if args.analyze:
        problem_files = analyze_problem_files()
        if problem_files:
            print(f"发现 {len(problem_files)} 个问题文件:")
            for i, (cmd, reason) in enumerate(problem_files[:50], 1):
                print(f"{i:3d}. {cmd} - {reason}")
            if len(problem_files) > 50:
                print(f"... 还有 {len(problem_files) - 50} 个")
        else:
            print("未发现问题文件")
    
    elif args.restore_all:
        restore_all_problem_files(backup=not args.no_backup)
    
    elif args.restore:
        restore_specific_files(args.restore, backup=not args.no_backup)
    
    else:
        # 默认操作：分析问题文件
        problem_files = analyze_problem_files()
        if problem_files:
            print(f"发现 {len(problem_files)} 个问题文件")
            print("使用 --restore-all 恢复所有文件，或使用 --restore <命令> 恢复指定文件")
        else:
            print("未发现问题文件")


if __name__ == "__main__":
    main()