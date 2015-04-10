from config import keywords, literals, primitives
from interpreter import execute, stdin
from lexer import *
from parser import *
from ply.lex import lex
from ply.yacc import yacc
tokens = keywords + primitives
tokenizer = lex( debug=0 )
compiler = yacc()
compiler.error = 0
print( "oply >>>" )
program = compiler.parse( stdin(), debug=0 )
print
execute( program )
print
raw_input( "exit" )