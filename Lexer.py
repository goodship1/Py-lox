import ply.lex  as scanner
    #lexer for the lox programming language
key_words = {"if":"IF","else":"ELSE","print":"PRINT","true":"TRUE",
            "false":"FALSE","nil":"NIL","class":"CLASS","or":"OR","and":"AND"
            ,"var":"VAR","for":"FOR","fun":"FUN","while":"WHILE","return":"RETURN","init":"INIT","this":"THIS"}

tokens = ["plus","minus","equals","colon","times","leftpara","rightpara",
            "leftclosure","rightclosure","integer","float","string","greaterthan","lessthan"
            ,"identifier","whitespace","lessthanequal","greaterthanequal","float","increment","equalequal","constructor"]+list(key_words.values())
   


def t_indentifier(t):
        #indentifiers follow the following grammar var id = type; eg var name = "lox"
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = key_words.get(t.value,'identifier')
        return  t

def t_float(t):
		r'\d+\.\d+'
		'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'        
		t.value = float(t.value)
		return t
t_ignore  = ' \t'

def t_nil(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = key_words.get(t.value,"nil")
        return t

def t_init(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = key_words.get("init","constructor")
        return t

    
def t_plus(t):
        r'\+'
        t.type = key_words.get(t.value,"plus")
        return t
    
def t_else(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = key_words.get(t.value,"else")
        return t


def t_string(t):
        r'"([^"\n]|(\\"))*"'
        t.type = key_words.get(t.value,"string")
        return t
    
def t_while(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = key_words.get(t.value,"while")
        return t

def t_for(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = key_words.get(t.value,"for")
        return t 
    
def t_equalequal(t):
        r'=='
        t.type = key_words.get(t.value,"equalequal")
        return t 


def t_integer(t):
        #rules for lexing integers 
        r'\d+'
        t.type = key_words.get(t.value,"integer")
        return t
    
def t_fun(t):
         r'[a-zA-Z_][a-zA-Z_0-9]*'
         t.type =  key_words.get(t.value,"fun")
         return t

def t_greaterthanequal(t):
        r'>='
        t.type = key_words.get(t.value,"greaterthanequal")
        return t

	
def t_lessthanequal(t):
        r'<='
        t.type = key_words.get(t.value,"lessthanequal")
        return t
    
    
def t_equals(t):
        #equals lexer 
        r'=+'
        t.type = key_words.get(t.value,"equals")
        return t

def t_colon(t):
        r'\;+'
        t.type = key_words.get(t.value,"colon")
        return t
    
def t_minus(t):
        r'\-+'
        t.type = key_words.get(t.value,"minus")
        return t 
   
def t_times(t):
	r'\*+'
	t.type =  key_words.get(t.value,"times")
	return t 


#def t_whitespace(t):
#		r'(\s)'
#		t.type =  key_words.get(t.value,"whitespace")
#		return t

def t_if(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = key_words.get(t.value,'if')
        return t
   
def t_leftpara(t):
	r'\('
	t.type = key_words.get(t.value,"leftpara")
	return t 
        
def t_error(t):
	print("error {}",t.value)
	t.lexer.skip(1)

def t_rightpara(t):
        r'\)'
        t.type = key_words.get(t.value,"rightpara")
        return t

def t_greaterthan(t):
        r'>'
        t.type = key_words.get(t.value,"greaterthan")
        return t

def t_rightclosure(t):
        r'{'
        t.type = key_words.get(t.value,"rightclosure")
        return t 

def t_leftclosure(t):
        r'}'
        t.type = key_words.get(t.value,"leftclosure")
        return t

def t_lessthan(t):
        r'<'
        t.type = key_words.get(t.value,"lessthan")
        return t 

    
def t_print(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = key_words.get(t.value,"print")
        return t


scanner.lex()
