import sys
#sys.path.insert(0,'../Scanner/')
import ply.lex as lex
import ply.yacc as yacc
#import scanner.Lexer as Lex
sys.path.insert(0,'../scanner/')
import scanner.Lexer as Lex


class Parser():

    def __str__(self):
        return "parser for the lox programming language"

    def p_indentify(self,p):
        'id:indetifier'
        p[0] = p[1]

    def build(self):
		parser = yacc.yacc()


p = Parser()
p.build()
