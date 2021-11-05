from os import error, read


txt = open("input.txt", 'r')
token = 0                    #token per character
LETTER = 0
DIGIT = 1
UNKNOWN =2
EOF = -1 
lexeme = []                  #each lexeme
char = ''                    #each character in the file
tokenFinal = ''              #token per lexeme
ident = "Identifier"         #identifier (e.g., 'total', 'A', 'B1')
number = "Integer"           #integer literal
ctr =0                       #counter to limit lexeme length to 9 characters
LexDict = {}
_id = 0
space = False

def getChar():               #identify the token of each character
    global char, token, space
    char = txt.read(1)       #read one character from txt
    if(char):                #checks if end of file
        if char.isalpha():   #letters
            token = LETTER
        elif char.isdigit(): #digits
            token = DIGIT
        elif char.isspace(): #ignore blank spaces
            space = True
        else:
            token = UNKNOWN  #unknown characters (e.g., operators)
    else:
        token = EOF

def addChar():               #add character to array to form lexeme
    if ctr <10:
        lexeme.append(char)
        ++ctr
    else:
        print('too long')


def lookup(c):               #identify unknown characters
    if c=='=':
        operator = 'Equals'
    elif c=='(':
        operator = 'L_Paren'
    elif c==')':
        operator = 'R_paren'
    elif c=='+':
        operator = 'Plus'
    elif c=='-':
        operator = 'Minus'
    elif c=='\\':
        operator = 'Division'
    elif c=='*':
        operator = 'Multiplication'
    else:
        operator = 'EOF'
    return operator


def stringLookup(c):
    if c == 'var':
        reserved = 'var type'
    elif c == 'while' or c == 'While':
        reserved = 'loop'
    elif c == 'if' or c== 'elif' or c== 'else':
        reserved = 'conditional'
    elif c=='True' or c== 'False':
        reserved = 'boolean'
    else:
        reserved = ident
    
    return reserved

def lex():                  
    global defined,lexeme,tokenFinal,char,token,_id,space
    space = False
    lexeme.clear()                                  #clear lexeme array for the next lexeme
    global ctr
    ctr = 0
    if  (token == LETTER):                          #identifier
        #addChar()
        #getChar()
        while (token==LETTER or token==DIGIT)and space==False:
            addChar()
            getChar()
        tokenFinal = stringLookup(''.join(lexeme))
    elif (token == DIGIT):                          #integer literal
        #addChar()
        #getChar()
        while token==DIGIT:
            addChar()
            getChar()
        tokenFinal = number
    elif token==UNKNOWN :                          #unknown characters
        tokenFinal =lookup(char)
        lexeme.append(char)
        if tokenFinal == 'EOF':
            token = EOF
        getChar()
    elif token == EOF :                            #end of file
        lexeme.append('E')
        lexeme.append('O')
        lexeme.append('F')
        lexeme.append(0)
        tokenFinal = 'EOF'
    

    print(''.join(lexeme), "      ", tokenFinal)   
    LexDict[_id]  = {''.join(lexeme):tokenFinal}    #Save in a dictionary
    _id += 1

    if space == True:
        getChar()
        return

if (txt!= None):
    getChar()
    while (token != EOF):
        lex()
        if (tokenFinal =='EOF'):
            break

else:
    print("There's a problem with the file.")

#for k,v in LexDict.items():                         #Just printing the contents of the dictionary
#    print(v)

