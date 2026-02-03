# Parallel Translation Work Assignment Guide

Generated: 2026-02-03T08:29:38.821443
Total sections: 4
Total commands: 708

## Section Assignments

### Section 1
- **Commands**: 177
- **File**: `section_1.json`
- **Status**: Pending

### Section 2
- **Commands**: 177
- **File**: `section_2.json`
- **Status**: Pending

### Section 3
- **Commands**: 177
- **File**: `section_3.json`
- **Status**: Pending

### Section 4
- **Commands**: 177
- **File**: `section_4.json`
- **Status**: Pending

## Workflow

1. Each team/worker takes one section
2. Process commands in your section using the standard workflow:
   - Check English document quality
   - Update 'See Also' links
   - Translate to Chinese
   - Apply formatting
3. Update progress after completing each command:
   ```bash
   python scripts/section_scheduler.py update --section <id> --command <command>
   ```
4. Check overall progress:
   ```bash
   python scripts/section_scheduler.py progress
   ```
