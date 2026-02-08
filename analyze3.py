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

# Define mapping rules
# Order matters: longer sequences first
replacements = [
    ('!=', 'exclamationequals'),
    ('<=', 'lte'),
    ('>=', 'gte'),
    ('==', 'equalsequals'),
    (' ', '_'),
    ('(', 'lparen'),
    (')', 'rparen'),
    ('!', 'exclamation'),
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
    ('=', 'equals'),
    ('>', 'gt'),
    ('?', 'question'),
    ('[', 'lbracket'),
    (']', 'rbracket'),
    ('^', 'caret'),
    ('|', 'pipe'),
    ('~', 'tilde'),
]

def command_to_filename(cmd):
    result = cmd
    for old, new in replacements:
        result = result.replace(old, new)
    return result

# Special cases
special_cases = {
    'dot': 'dot_cmd',  # dot command -> dot_cmd
    '.': 'dot',        # . command -> dot
    '[': 'lbracketrbracket',  # [ command -> lbracketrbracket (covers [])
}

# Build mapping
mapping = {}
unmapped = []
for cmd in commands:
    if cmd in special_cases:
        fname = special_cases[cmd]
        if fname in filenames:
            mapping[cmd] = fname
        else:
            unmapped.append(cmd)
        continue
    fname = command_to_filename(cmd)
    if fname in filenames:
        mapping[cmd] = fname
    else:
        unmapped.append(cmd)

print(f"Mapped: {len(mapping)}")
print(f"Unmapped: {len(unmapped)}")
if unmapped:
    print("Unmapped commands:")
    for cmd in unmapped:
        print(f"  '{cmd}' -> attempted '{command_to_filename(cmd)}'")

# Verify all filenames are covered
covered_filenames = set(mapping.values())
missing_filenames = set(filenames) - covered_filenames
if missing_filenames:
    print(f"\nFilenames not covered by mapping ({len(missing_filenames)}):")
    for f in sorted(missing_filenames):
        print(f"  {f}")

# Print special character mapping table
print("\n=== Special Character Mapping Table ===")
special_chars = [c for c in commands if any(ch in c for ch in ' !\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')]
special_chars.sort()
for cmd in special_chars:
    if cmd in mapping:
        print(f"  {repr(cmd):20} -> {mapping[cmd]}")
    else:
        print(f"  {repr(cmd):20} -> NOT MAPPED")

# Print dot conflict info
print("\n=== Dot Conflict ===")
print(f"  '.' command -> {mapping.get('.', 'N/A')}")
print(f"  'dot' command -> {mapping.get('dot', 'N/A')}")

# List all exceptions (where mapping is not just identity)
print("\n=== Non-identity Mappings (Exceptions) ===")
exceptions = []
for cmd, fname in sorted(mapping.items()):
    if cmd != fname:
        exceptions.append((cmd, fname))
print(f"Total exceptions: {len(exceptions)}")
for cmd, fname in exceptions[:30]:
    print(f"  {repr(cmd):30} -> {fname}")
if len(exceptions) > 30:
    print(f"  ... and {len(exceptions)-30} more")

# Generate Python function
print("\n=== Python function draft ===")
print("""
def command_to_filename(cmd: str) -> str:
    \"\"\"Convert Lumerical command name to documentation filename.\"\"\"
    # Special cases
    special = {
        'dot': 'dot_cmd',
        '.': 'dot',
        '[': 'lbracketrbracket',
    }
    if cmd in special:
        return special[cmd]
    
    # Replacement rules (order matters)
    replacements = [
        ('!=', 'exclamationequals'),
        ('<=', 'lte'),
        ('>=', 'gte'),
        ('==', 'equalsequals'),
        (' ', '_'),
        ('(', 'lparen'),
        (')', 'rparen'),
        ('!', 'exclamation'),
        ('\"', 'quote'),
        ('#', 'hash'),
        ('%', 'percent'),
        ('&', 'ampersand'),
        (\"'\", 'apostrophe'),
        ('*', 'asterisk'),
        ('+', 'plus'),
        ('-', 'minus'),
        ('.', 'dot'),
        ('/', 'slash'),
        (':', 'colon'),
        ('<', 'lt'),
        ('=', 'equals'),
        ('>', 'gt'),
        ('?', 'question'),
        ('[', 'lbracket'),
        (']', 'rbracket'),
        ('^', 'caret'),
        ('|', 'pipe'),
        ('~', 'tilde'),
    ]
    result = cmd
    for old, new in replacements:
        result = result.replace(old, new)
    return result
""")
