def sanitize_filename(name):
    original_name = name
    multi_char_replacements = {
        '<=': 'lte',
        '>=': 'gte',
        '==': 'equalequal',
        '!=': 'notequal',
        '+=': 'plusequals',
        '-=': 'minusequals',
        '*=': 'asteriskequals',
        '/=': 'slashequals',
    }
    for combo, replacement in multi_char_replacements.items():
        name = name.replace(combo, replacement)
    replacements = {
        '!': 'exclamation', '"': 'quote', '#': 'hash', '$': 'dollar',
        '%': 'percent', '&': 'ampersand', "'": 'apostrophe', '(': 'lparen',
        ')': 'rparen', '*': 'asterisk', '+': 'plus', ',': 'comma', '-': 'minus',
        '.': 'dot', '/': 'slash', ':': 'colon', ';': 'semicolon', '<': 'lt',
        '=': 'equals', '>': 'gt', '?': 'question', '@': 'at', '[': 'lbracket',
        '\': 'backslash', ']': 'rbracket', '^': 'caret', '`': 'backtick',
        '{': 'lbrace', '|': 'pipe', '}': 'rbrace', '~': 'tilde', ' ': '_'
    }
    for char, replacement in replacements.items():
        name = name.replace(char, replacement)
    illegal_chars = r'<>:"/\|?*'
    for char in illegal_chars:
        name = name.replace(char, '_')
    if name.startswith('.'):
        name = 'dot' + name
    if not name:
        import hashlib
        name = hashlib.md5(original_name.encode()).hexdigest()[:8]
    return name

tests = ['<=', '>=', '"', '*', '/', ':', '?', '|', '<', '>', '.', 'dot', '==', '!=', '+=', '-=', '*=', '/=']
for t in tests:
    print(f'{t!r:4} -> {sanitize_filename(t)}')
