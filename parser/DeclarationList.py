def p_declaration_list( p ):
    '''DeclarationList : Declaration ';' DeclarationList'''
    p[0] = [ p[1] ] + p[3]
def p_declaration_list_empty( p ):
    '''DeclarationList : empty'''
    p[0] = []