import ply.lex as lex
import ply.yacc as yacc
from Lexer import tokens

class Parser():


    def build(self):
		parser = yacc.yacc()


p = Parser()
p.build()
