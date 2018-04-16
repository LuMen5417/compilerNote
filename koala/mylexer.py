import ply.lex as lex

tokens = [ 
    'number',
    'plus',
    'minus',
    'multiply',
    'divide',
    'lparen',
    'rparen',
    'assign',
    'equal',
    'greater',
    'less',
    'colon',
    'dot',
    'id'
]

t_plus = r'\+'
t_minus = r'-'
t_multiply = r'\*'
t_divide = r'/'
t_lparen = r'\('
t_rparen = r'\)'
t_assign = r'='
t_equal = r'=='
t_greater = r'>'
t_less = r'<'
t_colon = r':'
t_dot = r'\.'
t_ignore = r' \t'
t_ignore_comment = r'\#.*'

reserved = {
    'if': 'if',
    'else': 'else',
    'while': 'while',
    'continue': 'continue',
    'break': 'break',
    'import': 'import',
}

tokens = tokens + list(reserved.values())

def t_number(t):
    r'\d+'
    t.value = int(t.value)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_id(t):
    r'[a-zA-Z\_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'id')
    return t


lexer = lex.lex()

data = '''
            import sys
            if a=1:
            _a2 = 3 +  4 *10+20*13'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break
    
    print(tok)