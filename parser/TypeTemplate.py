def p_type_template_struct( p ):
    '''TypeTemplate : '{' DeclarationList '}' '''
    p[0] = [ "struct", p[2] ]
def p_type_template_call( p ):
    '''TypeTemplate : LefthandSide'''
    p[0] = [ "call", p[1] ]