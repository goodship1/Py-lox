import ply.lex  as scanner
class Lexer(object):
    #lexer for the lox programming language
    key_words = {"if":"IF","else":"ELSE","print":"PRINT","true":"TRUE",
            "false":"FALSE","nil":"NIL","class":"CLASS","or":"OR","and":"AND"
            ,"var":"VAR","for":"FOR","fun":"FUN","while":"WHILE"}

    tokens = ["plus","minus","equals","colon","times","leftpara","rightparenthensis",
            "leftclosure","rightclousure","integer","float","string","greaterthan","lessthan"
            ,"identifier","whitespace"]+list(key_words.values())
    
    def _checknotkeyword(self,value):
        pass

    def t_indentifier(self,t):
        #indentifiers follow the following grammar var id = type; eg var name = "lox"
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.key_words.get(t.value,'identifier')
        return  t

    def t_integer(self,t):
        #rules for lexing integers 
        r'\d+'
        t.type = self.key_words.get(t.value,"integer")
        return t
    
    def t_fun(self,t):
         r'[a-zA-Z_][a-zA-Z_0-9]*'
         t.type =  self.key_words.get(t.value,"fun")
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

    def t_plus(self,t):
        r'\++'
        t.type =  self.key_words.get(t.value,"plus")
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
lexer.test_function("x=100; y=100 if(x > 10){")
