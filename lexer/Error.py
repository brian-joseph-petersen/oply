def t_error( t ):
    print
    print( "ILLEGAL CHARACTER %s" % t.value[0] )
    print
    t.lexer.skip( 1 )