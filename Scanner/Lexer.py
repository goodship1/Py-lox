import ply.lex  as scanner
class Lexer(object):
    #lexer for the lox programming language
    key_words = {"if":"IF","else":"ELSE","print":"PRINT","true":"TRUE",
            "false":"FALSE","nil":"NIL","class":"CLASS","or":"OR","and":"AND"
            ,"var":"VAR","for":"FOR","fun":"FUN","while":"WHILE","return":"RETURN","init":"INIT","this":"THIS"}

    tokens = ["plus","minus","equals","colon","times","leftpara","rightpara",
            "leftclosure","rightclosure","integer","float","string","greaterthan","lessthan"
            ,"identifier","whitespace","lessthanequal","greaterthanequal","float","increment","equalequal","constructor"]+list(key_words.values())
    
    def _checknotkeyword(self,value):
        pass

    def t_indentifier(self,t):
        #indentifiers follow the following grammar var id = type; eg var name = "lox"
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.key_words.get(t.value,'identifier')
        return  t

    def t_float(self,t):
		r'\d+\.\d+'
		'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'        
		t.value = float(t.value)
		return t
    
    def t_nil(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.key_words.get(t.value,"nil")
        return t

    def t_init(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.key_words.get("init","constructor")
        return t

    
    def t_plus(self,t):
        r'\+'
        t.type = self.key_words.get(t.value,"plus")
        return t
    
    def t_else(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.key_words.get(t.value,"else")
        return t


    def t_string(self,t):
        r'"([^"\n]|(\\"))*"'
        t.type = self.key_words.get(t.value,"string")
        return t
    
    def t_while(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.key_words.get(t.value,"while")
        return t

    def t_for(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.key_words.get(t.value,"for")
        return t 
    
    def t_equalequal(self,t):
        r'=='
        t.type = self.key_words.get(t.value,"equalequal")
        return t 


    def t_integer(self,t):
        #rules for lexing integers 
        r'\d+'
        t.type = self.key_words.get(t.value,"integer")
        return t
    
    def t_fun(self,t):
         r'[a-zA-Z_][a-zA-Z_0-9]*'
         t.type =  self.key_words.get(t.value,"fun")
         return t

    def t_greaterthanequal(self,t):
        r'>='
        t.type = self.key_words.get(t.value,"greaterthanequal")
        return t

	
    def t_lessthanequal(self,t):
        r'<='
        t.type = self.key_words.get(t.value,"lessthanequal")
        return t
    
    
    def t_equals(self,t):
        #equals lexer 
        r'=+'
        t.type = self.key_words.get(t.value,"equals")
        return t

    def t_colon(self,t):
        r'\;+'
        t.type = self.key_words.get(t.value,"colon")
        return t
    
    def t_minus(self,t):
        r'\-+'
        t.type = self.key_words.get(t.value,"minus")
        return t 
   
    def t_times(self,t):
	r'\*+'
	t.type =  self.key_words.get(t.value,"times")
	return t 


    def t_whitespace(self,t):
	r'(\s)'
        t.type =  self.key_words.get(t.value,"whitespace")
        return t
    
    def t_if(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.key_words.get(t.value,'if')
        return t
   
    def t_leftpara(self,t):
	r'\('
	t.type = self.key_words.get(t.value,"leftpara")
	return t 
        
    def t_error(self,t):
	print("error {}",t.value)
	t.lexer.skip(1)

    def t_rightpara(self,t):
        r'\)'
        t.type = self.key_words.get(t.value,"rightpara")
        return t

    def t_greaterthan(self,t):
        r'>'
        t.type = self.key_words.get(t.value,"greaterthan")
        return t

    def t_rightclosure(self,t):
        r'{'
        t.type = self.key_words.get(t.value,"rightclosure")
        return t 

    def t_leftclosure(self,t):
        r'}'
        t.type = self.key_words.get(t.value,"leftclosure")
        return t

    def t_lessthan(self,t):
        r'<'
        t.type = self.key_words.get(t.value,"lessthan")
        return t 

    

    def t_print(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.key_words.get(t.value,"print")
        return t


    def build(self,**kwargs):
         self.lexer = scanner.lex(module=self, **kwargs)
    
    def test_function(self,src):
        self.lexer.input(src)
        while True:
            tokens = self.lexer.token()
            if not tokens:
                break
            print(tokens)

lexer = Lexer()
lexer.build()
lexer.test_function('''var x  = 10; x<200;''')
