import ply.lex as lex
import ply.yacc as yacc
from Lexer import tokens

symboltable = {'x':1}

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
                | VAR identifier equals term lessthan term colon
                | VAR identifier equals term greaterthan term colon
                | VAR identifier equals term equalequal term colon
                | VAR identifier equals term lessthanequal term colon
                | VAR identifier equals term  greaterthanequal term colon

                '''
    p[0] = ("assignment",p[2],p[3],p[4],p[5],p[6])

def p_variableaddition(p):
    #rules to for adding to integers
    'varaddvar : identifier plus identifier colon'
    if p[1] in symboltable and p[2] in symboltable:
        p[0] = ("variableadd",p[1],p[2],p[3])
    else:
        p_error("s")


 

def p_add(p):
    #non variable addition eg 1+1;
    'add : term plus term colon'
    p[0] = ('add',p[1],p[2],p[3])

def p_substract(p):
    'sub : term minus term colon'
    p[0] = ('sub',p[1],p[2],p[3])

def p_mutiply(p):
    'mutiply : term times term colon'
    p[0] = ('mutiply',p[1],p[2],p[3])

def p_less(p):
    'less : term lessthan term colon'
    p[0] = ('less',p[1],p[2],p[3])

def p_greater(p):
    'greater : term greaterthan term colon'
    p[0] = ("greater",p[1],p[2],p[3])

def p_equalequalto(p):
    'equalcompare : term equalequal term colon'
    p[0] =("equalcompare",p[1],p[2],p[3])


def p_lessequal(p):
    'lessequal : term lessthanequal term colon'
    p[0] = ("lessequal",p[1],p[2],p[3])



def p_lessthanequal(p):
    'expression : lessthanequal'
    p[0] = p[1]

def p_greaterthanequal(p):
    'expression : greaterthanequal'
    p[0] = p[1]



def p_lessthan(p):
    'expression : lessthan'
    p[0] = p[1]

def p_greaterthan(p):
    'expression : greaterthan'
    p[0] = p[1]

def p_equalequal(p):
    'expression : equalequal'
    p[0] = p[1]


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

start = 'expression'
parser = yacc.yacc(start = start)
while True:
    try:
        s = raw_input('Lox > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

print(symboltable)
