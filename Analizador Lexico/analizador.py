import ply.lex as lex

# Palabras reservadas básicas de C99
reserved_words = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void': 'VOID',
    'while': 'WHILE',
    'for': 'FOR',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'break': 'BREAK'
}

# Lista de tokens
tokens = [
    'ID',
    'INT_CONST',
    'FLOAT_CONST',
    'CHAR_CONST',
    'STRING_LITERAL',
    'LE', 'GE', 'EQ', 'NE', 'AND', 'OR'
] + list(reserved_words.values())

# Declaración de Start Conditions (Estados)
# Se usa 'exclusive' para que las reglas normales no apliquen dentro de strings o comentarios
states = (
    ('string', 'exclusive'),
    ('comment', 'exclusive'),
    ('linecomment', 'exclusive'),
)

t_LE  = r'<='
t_GE  = r'>='
t_EQ  = r'=='
t_NE  = r'!='
t_AND = r'&&'
t_OR  = r'\|\|'

literals = '+-*={}()<,;>!/&|%[]'

t_string_ignore = ''

def t_begin_string(t):
    r'\"'
    t.lexer.string_val = ""
    t.lexer.begin('string')

def t_string_chars(t):
    r'[^"\\\n]+'
    t.lexer.string_val += t.value

def t_string_escape(t):
    r'\\.'
    t.lexer.string_val += t.value

def t_string_end(t):
    r'\"'
    t.type = 'STRING_LITERAL'
    t.value = t.lexer.string_val
    t.lexer.begin('INITIAL')
    return t

def t_string_error(t):
    print(f"Error léxico en string: {t.value[0]}")
    t.lexer.skip(1)

t_comment_ignore = ''

def t_begin_comment(t):
    r'/\*'
    t.lexer.begin('comment')

def t_comment_end(t):
    r'\*/'
    t.lexer.begin('INITIAL')

def t_comment_body(t):
    r'[^*/\n]+'
    pass

def t_comment_star_slash(t):
    r'[*\/]'
    pass

def t_comment_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment_error(t):
    t.lexer.skip(1)

t_linecomment_ignore = ''

def t_begin_linecomment(t):
    r'//'
    t.lexer.begin('linecomment')

def t_linecomment_end(t):
    r'\n'
    t.lexer.lineno += 1
    t.lexer.begin('INITIAL')

def t_linecomment_body(t):
    r'[^\n]+'
    pass

def t_linecomment_error(t):
    t.lexer.skip(1)



def t_FLOAT_CONST(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t

# Enteros (Mantenemos la simpleza, solo base 10)
def t_INT_CONST(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHAR_CONST(t):
    r"'([^'\\]|\\.)'"
    return t

def t_ID(t):
    r"[A-Za-z_][0-9A-Za-z_]*"
    t.type = reserved_words.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter no válido: '{t.value[0]}' en línea {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    data = """
    int main() {
        // Inicialización
        int n = 5;
        float pi = 3.14;
        char c = 'a';

        /* Ciclo principal
           usando start conditions
        */
        while (n <= 10) {
            printf("El valor es: %d\\n", n);
            n = n + 1;
        }
        return 0;
    }
    """
    lexer.input(data)
    for tok in lexer:
        print(tok)
