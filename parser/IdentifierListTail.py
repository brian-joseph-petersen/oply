def p_identifier_list_tail( p ):
    '''IListTail : ',' ID IListTail'''
    p[0] = [ p[2] ] + p[3]
def p_identifier_list_tail_empty( p ):
    '''IListTail : empty'''
    p[0] = []