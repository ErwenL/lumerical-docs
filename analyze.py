import os
import re

# Load command names
with open('docs/lsf-script/lsf-script-commands-alphabetical.md', 'r', encoding='utf-8') as f:
    content = f.read()
commands = re.findall(r'\[([^\]]+)\]', content)
print(f"Total commands: {len(commands)}")

# Load filenames (without extension)
filenames = []
for fname in os.listdir('docs/lsf-script/en'):
    if fname.endswith('.md'):
        filenames.append(fname[:-3])
print(f"Total filenames: {len(filenames)}")

# Build mapping from filename to command (guess)
mapping = {}
special_cases = []

# First, exact matches
exact_matches = set(commands) & set(filenames)
print(f"Exact matches: {len(exact_matches)}")

# For each command, find possible filename
def command_to_filename(cmd):
    # Replace special characters
    replacements = [
        (' ', ''),
        ('(', 'lparen'),
        (')', 'rparen'),
        ('!', 'exclamation'),
        ('!=', 'exclamationequals'),
        ('"', 'quote'),
        ('#', 'hash'),
        ('%', 'percent'),
        ('&', 'ampersand'),
        ("'", 'apostrophe'),
        ('*', 'asterisk'),
        ('+', 'plus'),
        ('-', 'minus'),
        ('.', 'dot'),
        ('/', 'slash'),
        (':', 'colon'),
        ('<', 'lt'),
        ('<=', 'lte'),
        ('=', 'equals'),
        ('==', 'equalsequals'),
        ('>', 'gt'),
        ('>=', 'gte'),
        ('?', 'question'),
    ]
    result = cmd
    for old, new in replacements:
        result = result.replace(old, new)
    return result

# Test mapping
mapped = {}
unmapped = []
for cmd in commands:
    fname = command_to_filename(cmd)
    if fname in filenames:
        mapped[cmd] = fname
    else:
        unmapped.append(cmd)

print(f"Mapped: {len(mapped)}")
print(f"Unmapped: {len(unmapped)}")

# Check dot special case
print("\nChecking dot:")
if 'dot' in commands and 'dot_cmd' in filenames:
    print("dot command -> dot_cmd")
if '.' in commands and 'dot' in filenames:
    print(". command -> dot")

# Show some unmapped
print("\nFirst 10 unmapped commands:")
for cmd in unmapped[:10]:
    print(f"  {cmd}")

# Show special mappings
print("\nSpecial character mappings:")
for cmd in commands:
    if any(c in cmd for c in '!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'):
        fname = mapped.get(cmd, 'NOT FOUND')
        print(f"  {cmd} -> {fname}")
