import ply.lex as lex

tokens = (
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
    'pound',
    'dot',
    'space',
    'valite'
)

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
t_pound = r'\#'
t_dot = r'\.'
t_ignore = r'#.*'
t_space = r'\s+'
t_valite = r'[a-zA-Z\_]([a-z]|[A-Z]|[0-9]|(\_))*'


def t_number(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = '''_a2 = 3 +  4 *10+20*13'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break
    
    print(tok)