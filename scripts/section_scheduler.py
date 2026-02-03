#!/usr/bin/env python3
"""
Section scheduler for parallel LSF documentation translation.
Allocates untranslated commands into multiple sections for parallel work.
"""

import argparse
import json
import logging
import sys
from collections import defaultdict
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
SCHEDULE_DIR = PROJECT_ROOT / "docs" / "translation-sections"


def get_untranslated_commands() -> List[str]:
    """Get all untranslated commands in alphabetical order.
    
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
    return untranslated


def analyze_command_distribution(commands: List[str]) -> Dict[str, Dict]:
    """Analyze command distribution by starting letter.
    
    Args:
        commands: List of command names.
        
    Returns:
        Dictionary with analysis results.
    """
    distribution = defaultdict(list)
    letter_counts = defaultdict(int)
    
    for cmd in commands:
        first_letter = cmd[0].upper() if cmd else ""
        distribution[first_letter].append(cmd)
        letter_counts[first_letter] += 1
    
    # Sort by letter
    sorted_letters = sorted(distribution.keys())
    
    return {
        "distribution": {letter: distribution[letter] for letter in sorted_letters},
        "counts": {letter: letter_counts[letter] for letter in sorted_letters},
        "total_commands": len(commands),
        "unique_letters": len(distribution),
    }


def create_sections_by_letter_range(
    commands: List[str], 
    num_sections: int,
    strategy: str = "balanced"
) -> Dict[int, List[str]]:
    """Create sections by dividing letter ranges.
    
    Args:
        commands: List of command names.
        num_sections: Number of sections to create.
        strategy: Allocation strategy: "balanced" (equal commands) or "letter" (by letter groups).
        
    Returns:
        Dictionary mapping section_id to list of commands.
    """
    if not commands:
        return {}
    
    # Sort commands
    sorted_commands = sorted(commands)
    
    if strategy == "balanced":
        # Balanced allocation: equal number of commands per section
        section_size = len(sorted_commands) // num_sections
        remainder = len(sorted_commands) % num_sections
        
        sections = {}
        start = 0
        for i in range(num_sections):
            # Add one extra command to first 'remainder' sections
            end = start + section_size + (1 if i < remainder else 0)
            sections[i + 1] = sorted_commands[start:end]
            start = end
        
        return sections
    
    elif strategy == "letter":
        # Group by first letter
        letter_groups = defaultdict(list)
        for cmd in sorted_commands:
            first_letter = cmd[0].upper() if cmd else ""
            letter_groups[first_letter].append(cmd)
        
        # Sort letter groups
        sorted_letters = sorted(letter_groups.keys())
        
        # Distribute letter groups among sections
        sections = {i + 1: [] for i in range(num_sections)}
        section_loads = [0] * num_sections
        
        for letter in sorted_letters:
            group_commands = letter_groups[letter]
            group_size = len(group_commands)
            
            # Find section with smallest load
            min_section = section_loads.index(min(section_loads))
            sections[min_section + 1].extend(group_commands)
            section_loads[min_section] += group_size
        
        return sections
    
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def create_sections_by_custom_ranges(
    commands: List[str],
    letter_ranges: List[Tuple[str, str]]
) -> Dict[str, List[str]]:
    """Create sections based on custom letter ranges.
    
    Args:
        commands: List of command names.
        letter_ranges: List of (start_letter, end_letter) tuples.
        
    Returns:
        Dictionary mapping section_name to list of commands.
    """
    sorted_commands = sorted(commands)
    sections = {}
    
    for start_letter, end_letter in letter_ranges:
        section_name = f"{start_letter}-{end_letter}"
        section_commands = []
        
        for cmd in sorted_commands:
            first_letter = cmd[0].upper() if cmd else ""
            if start_letter <= first_letter <= end_letter:
                section_commands.append(cmd)
        
        sections[section_name] = section_commands
    
    return sections


def save_sections_to_files(
    sections: Dict,
    section_type: str = "numbered"
) -> Dict[str, Path]:
    """Save sections to files in the schedule directory.
    
    Args:
        sections: Dictionary of sections.
        section_type: "numbered" for numeric sections, "letter" for letter-range sections.
        
    Returns:
        Dictionary mapping section_id to file path.
    """
    SCHEDULE_DIR.mkdir(parents=True, exist_ok=True)
    
    # Clear existing section files
    for file in SCHEDULE_DIR.glob("section_*.json"):
        file.unlink()
    
    saved_files = {}
    
    for section_id, commands in sections.items():
        if section_type == "numbered":
            filename = f"section_{section_id}.json"
        else:
            filename = f"section_{section_id}.json"
        
        filepath = SCHEDULE_DIR / filename
        
        section_data = {
            "section_id": str(section_id),
            "commands": commands,
            "command_count": len(commands),
            "created_date": datetime.now().isoformat(),
            "status": "pending",
            "completed_commands": [],
            "progress": 0.0,
        }
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(section_data, f, indent=2, ensure_ascii=False)
        
        saved_files[section_id] = filepath
        logger.info(f"Created section {section_id}: {len(commands)} commands -> {filepath}")
    
    # Create overview file
    overview = {
        "total_sections": len(sections),
        "total_commands": sum(len(cmds) for cmds in sections.values()),
        "sections": {sid: len(cmds) for sid, cmds in sections.items()},
        "created_date": datetime.now().isoformat(),
        "section_files": {sid: str(path) for sid, path in saved_files.items()},
    }
    
    overview_path = SCHEDULE_DIR / "sections_overview.json"
    with open(overview_path, "w", encoding="utf-8") as f:
        json.dump(overview, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Created sections overview: {overview_path}")
    return saved_files


def update_section_progress(section_id: str, completed_command: str) -> bool:
    """Update progress for a section when a command is completed.
    
    Args:
        section_id: Section identifier.
        completed_command: Command that was completed.
        
    Returns:
        True if update successful.
    """
    section_file = SCHEDULE_DIR / f"section_{section_id}.json"
    
    if not section_file.exists():
        logger.error(f"Section file not found: {section_file}")
        return False
    
    try:
        with open(section_file, "r", encoding="utf-8") as f:
            section_data = json.load(f)
        
        # Add to completed commands if not already there
        if completed_command not in section_data["completed_commands"]:
            section_data["completed_commands"].append(completed_command)
        
        # Update progress
        total = section_data["command_count"]
        completed = len(section_data["completed_commands"])
        section_data["progress"] = round(completed / total * 100, 2) if total > 0 else 0
        
        # Update status
        if completed == total:
            section_data["status"] = "completed"
        elif completed > 0:
            section_data["status"] = "in_progress"
        
        section_data["last_updated"] = datetime.now().isoformat()
        
        with open(section_file, "w", encoding="utf-8") as f:
            json.dump(section_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Updated section {section_id}: {completed}/{total} ({section_data['progress']}%)")
        return True
        
    except Exception as e:
        logger.error(f"Failed to update section {section_id}: {e}")
        return False


def get_section_progress() -> Dict:
    """Get overall progress across all sections.
    
    Returns:
        Dictionary with progress summary.
    """
    if not SCHEDULE_DIR.exists():
        return {"error": "Schedule directory not found"}
    
    section_files = list(SCHEDULE_DIR.glob("section_*.json"))
    
    total_commands = 0
    total_completed = 0
    sections_summary = {}
    
    for section_file in section_files:
        try:
            with open(section_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            section_id = data["section_id"]
            completed = len(data.get("completed_commands", []))
            total = data["command_count"]
            
            sections_summary[section_id] = {
                "completed": completed,
                "total": total,
                "progress": data.get("progress", 0.0),
                "status": data.get("status", "unknown"),
            }
            
            total_commands += total
            total_completed += completed
            
        except Exception as e:
            logger.error(f"Error reading {section_file}: {e}")
    
    overall_progress = round(total_completed / total_commands * 100, 2) if total_commands > 0 else 0
    
    return {
        "total_sections": len(sections_summary),
        "total_commands": total_commands,
        "total_completed": total_completed,
        "overall_progress": overall_progress,
        "sections": sections_summary,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Schedule LSF documentation translation into parallel sections."
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze command distribution")
    analyze_parser.add_argument("--output", "-o", help="Output file for analysis results")
    
    # Create sections command
    create_parser = subparsers.add_parser("create", help="Create translation sections")
    create_parser.add_argument("--sections", "-n", type=int, default=4,
                             help="Number of sections to create (default: 4)")
    create_parser.add_argument("--strategy", "-s", choices=["balanced", "letter"], default="balanced",
                             help="Allocation strategy: balanced (equal commands) or letter (by letter groups)")
    create_parser.add_argument("--custom-ranges", type=str,
                             help="Custom letter ranges in format A-D,E-H,I-L,M-P,Q-T,U-Z")
    
    # Progress command
    progress_parser = subparsers.add_parser("progress", help="Check section progress")
    
    # Update command
    update_parser = subparsers.add_parser("update", help="Update section progress")
    update_parser.add_argument("--section", "-s", required=True, help="Section ID to update")
    update_parser.add_argument("--completed", "-c", required=True, help="Completed command name")
    
    args = parser.parse_args()
    
    # Get untranslated commands
    commands = get_untranslated_commands()
    
    if not commands:
        logger.error("No untranslated commands found")
        return
    
    logger.info(f"Found {len(commands)} untranslated commands")
    
    if args.command == "analyze":
        # Analyze command distribution
        analysis = analyze_command_distribution(commands)
        
        print("\n" + "="*60)
        print("COMMAND DISTRIBUTION ANALYSIS")
        print("="*60)
        
        print(f"\nTotal commands: {analysis['total_commands']}")
        print(f"Unique starting letters: {analysis['unique_letters']}")
        
        print("\nCommands per letter:")
        print("-"*30)
        for letter, count in sorted(analysis['counts'].items()):
            print(f"  {letter}: {count:3d} commands")
        
        print("\nLetter ranges (cumulative):")
        print("-"*30)
        cumulative = 0
        for letter, count in sorted(analysis['counts'].items()):
            cumulative += count
            percentage = (cumulative / analysis['total_commands']) * 100
            print(f"  Up to {letter}: {cumulative:3d} commands ({percentage:.1f}%)")
        
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(analysis, f, indent=2, ensure_ascii=False)
            logger.info(f"Analysis saved to {args.output}")
    
    elif args.command == "create":
        # Create sections
        if args.custom_ranges:
            # Parse custom ranges
            ranges = []
            for range_str in args.custom_ranges.split(","):
                if "-" in range_str:
                    start, end = range_str.split("-")
                    ranges.append((start.strip().upper(), end.strip().upper()))
                else:
                    logger.error(f"Invalid range format: {range_str}")
                    return
            
            sections = create_sections_by_custom_ranges(commands, ranges)
            section_type = "letter"
            
        else:
            sections = create_sections_by_letter_range(
                commands, args.sections, args.strategy
            )
            section_type = "numbered"
        
        # Save sections to files
        saved_files = save_sections_to_files(sections, section_type)
        
        print("\n" + "="*60)
        print("SECTION ALLOCATION SUMMARY")
        print("="*60)
        
        total_commands = 0
        for section_id, section_commands in sections.items():
            print(f"\nSection {section_id}: {len(section_commands)} commands")
            total_commands += len(section_commands)
            
            # Show first few commands
            if section_commands:
                preview = ", ".join(section_commands[:5])
                if len(section_commands) > 5:
                    preview += f", ... (+{len(section_commands)-5} more)"
                print(f"  Commands: {preview}")
        
        print(f"\nTotal allocated: {total_commands} commands")
        print(f"Section files saved to: {SCHEDULE_DIR}")
        
        # Create a simple work assignment guide
        guide_path = SCHEDULE_DIR / "WORK_ASSIGNMENT_GUIDE.md"
        with open(guide_path, "w", encoding="utf-8") as f:
            f.write("# Parallel Translation Work Assignment Guide\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Total sections: {len(sections)}\n")
            f.write(f"Total commands: {total_commands}\n\n")
            
            f.write("## Section Assignments\n\n")
            for section_id, section_commands in sections.items():
                f.write(f"### Section {section_id}\n")
                f.write(f"- **Commands**: {len(section_commands)}\n")
                f.write(f"- **File**: `section_{section_id}.json`\n")
                f.write(f"- **Status**: Pending\n\n")
            
            f.write("## Workflow\n\n")
            f.write("1. Each team/worker takes one section\n")
            f.write("2. Process commands in your section using the standard workflow:\n")
            f.write("   - Check English document quality\n")
            f.write("   - Update 'See Also' links\n")
            f.write("   - Translate to Chinese\n")
            f.write("   - Apply formatting\n")
            f.write("3. Update progress after completing each command:\n")
            f.write("   ```bash\n")
            f.write("   python scripts/section_scheduler.py update --section <id> --completed <command>\n")
            f.write("   ```\n")
            f.write("4. Check overall progress:\n")
            f.write("   ```bash\n")
            f.write("   python scripts/section_scheduler.py progress\n")
            f.write("   ```\n")
        
        logger.info(f"Work assignment guide: {guide_path}")
    
    elif args.command == "progress":
        # Check progress
        progress = get_section_progress()
        
        if "error" in progress:
            print(f"Error: {progress['error']}")
            return
        
        print("\n" + "="*60)
        print("SECTION TRANSLATION PROGRESS")
        print("="*60)
        
        print(f"\nOverall: {progress['total_completed']}/{progress['total_commands']} "
              f"({progress['overall_progress']:.1f}%)")
        
        for section_id, data in progress["sections"].items():
            status_icon = "[DONE]" if data["status"] == "completed" else "[WORKING]" if data["status"] == "in_progress" else "[PAUSED]"
            print(f"\nSection {section_id}: {status_icon}")
            print(f"  Progress: {data['completed']}/{data['total']} ({data['progress']:.1f}%)")
            print(f"  Status: {data['status']}")
    
    elif args.command == "update":
        # Update section progress
        success = update_section_progress(args.section, args.completed)
        if success:
            print(f"[OK] Updated section {args.section}: completed '{args.completed}'")
        else:
            print(f"[ERROR] Failed to update section {args.section}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()