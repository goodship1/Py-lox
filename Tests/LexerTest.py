import pytest
import sys
sys.path.insert(0,'..')
from Scanner import Lexer as Lex

class LexerTests(object):

    def __str__(self):
        return "test class for lexer"

    def __init__(self):
        self.lexer = Lex()
        self.lexer.build()

    def integerassignmenttest(self):
        #interger assignment test
        assignmentinteger = "var x = 10;"
    
    def floatassignmenttest(self):
        #float assignment test
        assignmentfloat = "var y = 100.0;"

    def stringassignmenttest(self):
        #string assignment test
        assignmentstring = '''var x = "hello";'''

    def nilassignmenttest(self):
        #assignment of nill test
        assignmentnil = '''var x  = nil;'''

    def addingtwovariablestest(self):
        #adding two variables together tests
        addingtwovariables = ''' var x =  10;
                             var y = 200;
                             x + y;'''
    def substractingtwovariablestest(self):
        #substracting two varables
        substractingtwovariables = ''' var x = 10; var y = 10; x-y;'''
    
    def mutiplyingtwovariablestest(self):
        # mutiply two variables together
        mutiplytwovariables = '''var x = 20; var y = 20; x * y;'''

    def lessthanintegertest(self):
        #less than integer value
        lessthaninteger = ''' var x =  100; x<200;'''

    def lessthanequalintegertest(self):
        #less than equal integer
        lessthanequalinteger = ''' var x = 200; x<=200;'''

    def lessthanfloattest(self):
        #less than float test
        lessthanfloat =  '''var x = 100.0; x<200.0;'''

    def lessthanequalfloattest(self):
        #lessthan floating point lexer rules
        lessthanequalfloat = '''var x = 100.0 x<=200.0'''

    def greaterthanintegertest(self):
        #greaterthaninteger test
        greaterthaninteger = '''var x = 200; x>100;'''
    
    def greaterthanfloattest(self):
        #greaterthanfloat test
        greaterthanfloat = '''var x = 100.0; x<200.0;'''

    def greaterthanequalintegertest(self):
        #greater than equal integer
        greatherthanequalinteger = '''var x  = 200; x>=200;'''

    def greaterthanequalfloattest(self):
        #greater than equal float test
        greatherthaneqaulfloat = '''var x = 200.0; x>=200.0;'''

    def booltestoftrue(self):
        #true key word test
        trueassignment= '''var x  = true;'''

    def booltestfalse(self):
        #false key word test
        falseassignment = '''var x  = false;'''

    
        







    
