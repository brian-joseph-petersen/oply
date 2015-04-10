def p_expression_list( p ):
    '''ExpressionList : Expression EListTail'''
    p[0] = [ p[1] ] + p[2]
def p_expression_list_empty( p ):
    '''ExpressionList : empty'''
    p[0] = []