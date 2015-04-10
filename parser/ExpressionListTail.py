def p_expression_list_tail( p ):
    '''EListTail : ',' Expression EListTail'''
    p[0] = [ p[2] ] + p[3]
def p_expression_list_tail_empty( p ):
    '''EListTail : empty'''
    p[0] = []