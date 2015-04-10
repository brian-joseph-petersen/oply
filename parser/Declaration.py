def p_declaration_int( p ):
    '''Declaration : int ID '=' Expression '''
    p[0] = [ "int", p[2], p[4] ]
def p_declaration_obj( p ):
    '''Declaration : obj ID '=' Expression '''
    p[0] = [ "obj", p[2], p[4] ]
def p_declaration_def( p ):
    '''Declaration : def ID '(' IdentifierList ')' ':' CommandList end '''
    p[0] = [ "def", p[2], p[4], p[7] ]
def p_declaration_class( p ):
    '''Declaration : class ID ':' TypeTemplate '''
    p[0] = [ "class", p[2], p[4] ]