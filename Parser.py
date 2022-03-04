import ply.lex as lex
import ply.yacc as yacc
from Lexer import tokens

symboltable = {}

def p_assignment(p):
    'assignment : VAR whitespace identifier whitespace equals whitespace expression colon'
    p[0] = ('assignment',p[3],p[5],p[7])

def p_expression_plus(p):
	'add : expression  plus  expression colon'
	p[0] = ('add' ,p[1],p[3],p[5])
	
	

def p_integer(p):
    'expression : integer'
    p[0] = p[1]


def p_float(p):
    'expression : float'
    p[0] = p[1]

def p_string(p):
    'expression : string'
    p[0] = p[1]

def p_plus(p):
    'expression : plus'
    p[0] = p[1]


parser = yacc.yacc()
while True:
    try:
        s = raw_input('Lox > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

print(symboltable)
