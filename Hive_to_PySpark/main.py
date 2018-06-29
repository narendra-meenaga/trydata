import sys
from lexer import *
from tokens import *
 

if __name__ == '__main__':
    filename = sys.argv[1]
    print(filename)
    file = open(filename)
    characters = file.read()
    file.close()
    tokens_identified = lex(characters,token_defs)
    #for token in tokens_identified:
    #    print(token)
