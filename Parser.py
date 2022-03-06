import ply.lex as lex
import ply.yacc as yacc
from Lexer import tokens

symboltable = {}

def p_assignment(p):
    '''assignment : VAR identifier  equals  term colon
                  | VAR identifier equals str colon
                  | VAR identifier equals true colon
                  | VAR identifier equals false colon
                  | VAR identifier equals nil colon
                  '''

    p[0] = ('assignment',p[2],p[3],p[4])


def safeeval(expression):
    #function limit can be passe to eval
    pass

def p_assignmentofexpression(p):
    '''assignment : VAR identifier equals term plus term colon
                | VAR identifier equals term minus term colon
                | VAR identifier equals term times term colon
                '''
    p[0] = ("assignment",p[2],p[3],p[4],p[5],p[6])



def p_times(p):
    'expression : times'
    p[0] = p[1]


def p_nil(p):
    'nil : NIL'
    p[0] = p[1]

def p_true(p):
    'true : TRUE'
    p[0] = p[1]

def p_false(p):
    'false : FALSE'
    p[0] = p[1]


def p_integer(p):
    'term : integer'
    p[0] = p[1]


def p_float(p):
    'term : float'
    p[0] = p[1]


def p_string(p):
    'str : string'
    p[0] = p[1]

def p_minus(p):
    'expression : minus'
    p[0] = p[1]

def p_error(p):
    print("syntax error")

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
