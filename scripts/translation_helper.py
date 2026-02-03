#!/usr/bin/env python3
"""
Translation helper for Lumerical LSF script documentation.
Manages the translation workflow from English to Chinese documentation.
"""

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


# Paths
PROJECT_ROOT = Path(__file__).parent.parent
EN_DOCS_DIR = PROJECT_ROOT / "docs" / "lsf-script" / "en"
CN_DOCS_DIR = PROJECT_ROOT / "docs" / "lsf-script" / "cn"
PROGRESS_FILE = PROJECT_ROOT / "docs" / "translation-progress.json"


def get_translation_status() -> Dict[str, Dict[str, int]]:
    """Get current translation status statistics.
    
    Returns:
        Dictionary with statistics about translation progress.
    """
    if not EN_DOCS_DIR.exists():
        logger.error(f"English docs directory not found: {EN_DOCS_DIR}")
        return {}
    
    # Count English documents
    en_files = list(EN_DOCS_DIR.glob("*.md"))
    total_en = len(en_files)
    
    # Count Chinese documents
    cn_files = []
    if CN_DOCS_DIR.exists():
        cn_files = list(CN_DOCS_DIR.glob("*.md"))
    total_cn = len(cn_files)
    
    # Get filenames for comparison
    en_filenames = {f.stem for f in en_files}
    cn_filenames = {f.stem for f in cn_files}
    
    # Find untranslated files
    untranslated = en_filenames - cn_filenames
    translated = en_filenames & cn_filenames
    
    return {
        "total": {
            "english": total_en,
            "chinese": total_cn,
            "translated": len(translated),
            "untranslated": len(untranslated),
        },
        "progress": {
            "percentage": round((len(translated) / total_en * 100), 1) if total_en > 0 else 0,
            "translated_count": len(translated),
            "total_count": total_en,
        },
        "directories": {
            "english": str(EN_DOCS_DIR),
            "chinese": str(CN_DOCS_DIR),
        }
    }


def list_untranslated_commands(limit: int = 20) -> List[str]:
    """List commands that need translation.
    
    Args:
        limit: Maximum number of commands to display.
    
    Returns:
        List of command names that need translation.
    """
    if not EN_DOCS_DIR.exists():
        logger.error(f"English docs directory not found: {EN_DOCS_DIR}")
        return []
    
    # Create Chinese directory if it doesn't exist
    CN_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Get file lists
    en_files = {f.stem: f for f in EN_DOCS_DIR.glob("*.md")}
    cn_files = {f.stem for f in CN_DOCS_DIR.glob("*.md")}
    
    # Find untranslated files
    untranslated = sorted(en_files.keys() - cn_files)
    
    if not untranslated:
        logger.info("All commands are already translated!")
        return []
    
    logger.info(f"Found {len(untranslated)} untranslated commands")
    
    # Display limited number
    display_count = min(limit, len(untranslated))
    for i, command in enumerate(untranslated[:display_count], 1):
        print(f"{i:3d}. {command}")
    
    if len(untranslated) > display_count:
        print(f"... and {len(untranslated) - display_count} more")
    
    return untranslated


def prepare_template_for_translation(command: str, overwrite: bool = False) -> bool:
    """Copy English template to Chinese directory for translation.
    
    Args:
        command: Command name (without .md extension).
        overwrite: Whether to overwrite existing Chinese file.
    
    Returns:
        True if successful, False otherwise.
    """
    # Construct file paths
    en_file = EN_DOCS_DIR / f"{command}.md"
    cn_file = CN_DOCS_DIR / f"{command}.md"
    
    # Check if English file exists
    if not en_file.exists():
        logger.error(f"English document not found: {en_file}")
        return False
    
    # Check if Chinese file already exists
    if cn_file.exists() and not overwrite:
        logger.warning(f"Chinese document already exists: {cn_file}")
        logger.info("Use --overwrite flag to replace existing file")
        return False
    
    # Create Chinese directory if it doesn't exist
    CN_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    try:
        # Read English content
        with open(en_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Add translation notice at the top
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        translation_notice = (
            f"<!--\n"
            f"Translation from English documentation\n"
            f"Original command: {command}\n"
            f"Translation date: {timestamp}\n"
            f"-->\n\n"
        )
        
        # Write to Chinese file
        with open(cn_file, "w", encoding="utf-8") as f:
            f.write(translation_notice)
            f.write(content)
        
        logger.info(f"Template created: {cn_file}")
        logger.info(f"Ready for translation. Edit the file to add Chinese content.")
        return True
        
    except Exception as e:
        logger.error(f"Failed to create template: {e}")
        return False


def generate_progress_report() -> Dict:
    """Generate detailed translation progress report.
    
    Returns:
        Dictionary with detailed progress information.
    """
    status = get_translation_status()
    
    if not status:
        return {}
    
    # Get detailed file lists
    en_files = {f.stem: f for f in EN_DOCS_DIR.glob("*.md")}
    cn_files = {f.stem: f for f in CN_DOCS_DIR.glob("*.md")} if CN_DOCS_DIR.exists() else {}
    
    translated = sorted(en_files.keys() & cn_files.keys())
    untranslated = sorted(en_files.keys() - cn_files.keys())
    
    # Save progress to file
    progress_data = {
        "generated": datetime.now().isoformat(),
        "statistics": status,
        "translated_commands": translated,
        "untranslated_commands": untranslated,
        "total_commands": len(en_files),
    }
    
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(progress_data, f, indent=2, ensure_ascii=False)
        logger.info(f"Progress report saved to: {PROGRESS_FILE}")
    except Exception as e:
        logger.error(f"Failed to save progress report: {e}")
    
    return progress_data


def show_statistics() -> None:
    """Display translation statistics."""
    status = get_translation_status()
    
    if not status:
        return
    
    stats = status["total"]
    progress = status["progress"]
    
    print("\n" + "=" * 50)
    print("LSF 脚本文档翻译进度统计")
    print("=" * 50)
    print(f"英文文档总数: {stats['english']}")
    print(f"中文文档总数: {stats['chinese']}")
    print(f"已翻译命令: {stats['translated']}")
    print(f"待翻译命令: {stats['untranslated']}")
    print(f"翻译进度: {progress['percentage']}%")
    print("-" * 50)
    
    if stats['untranslated'] > 0:
        print("下一步建议:")
        print("1. 运行 'python scripts/translation_helper.py --list' 查看待翻译命令")
        print("2. 运行 'python scripts/translation_helper.py --prepare <command>' 创建翻译模板")
        print("3. 编辑生成的中文文档文件进行翻译")
    else:
        print("🎉 所有命令已完成翻译！")
    
    print("=" * 50)


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="LSF script documentation translation helper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
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
        """
    )
    
    # Action arguments
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument(
        "--stats",
        action="store_true",
        help="Show translation statistics"
    )
    action_group.add_argument(
        "--list",
        action="store_true",
        help="List untranslated commands"
    )
    action_group.add_argument(
        "--prepare",
        metavar="COMMAND",
        type=str,
        help="Prepare translation template for a command"
    )
    action_group.add_argument(
        "--report",
        action="store_true",
        help="Generate detailed progress report"
    )
    
    # Optional arguments
    parser.add_argument(
        "--all",
        action="store_true",
        help="Show all untranslated commands (use with --list)"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing Chinese file (use with --prepare)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Limit number of commands shown (default: 20)"
    )
    
    args = parser.parse_args()
    
    # Ensure Chinese directory exists
    CN_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Execute requested action
    if args.stats:
        show_statistics()
    
    elif args.list:
        limit = None if args.all else args.limit
        if limit is None:
            # Show all untranslated commands
            untranslated = list_untranslated_commands(limit=1000000)
            if untranslated:
                print(f"\nTotal untranslated commands: {len(untranslated)}")
        else:
            list_untranslated_commands(limit=limit)
    
    elif args.prepare:
        success = prepare_template_for_translation(args.prepare, args.overwrite)
        if success:
            print(f"\nTemplate ready for translation:")
            print(f"  Chinese file: {CN_DOCS_DIR / args.prepare}.md")
            print(f"\nEdit the file to add Chinese translation.")
        else:
            sys.exit(1)
    
    elif args.report:
        report = generate_progress_report()
        if report:
            print(f"\nDetailed progress report generated:")
            print(f"  File: {PROGRESS_FILE}")
            print(f"  Translated: {len(report['translated_commands'])} commands")
            print(f"  Untranslated: {len(report['untranslated_commands'])} commands")
    
    else:
        # Default action: show statistics
        show_statistics()


if __name__ == "__main__":
    main()