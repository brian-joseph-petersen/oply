def p_identifier_list( p ):
    '''IdentifierList : ID IListTail'''
    p[0] = [ p[1] ] + p[2]
def p_identifier_list_empty( p ):
    '''IdentifierList :  empty'''
    p[0] = []