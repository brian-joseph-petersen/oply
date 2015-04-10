def p_expression_num( p ):
    '''Expression : NUM'''
    p[0] = p[1]
def p_expression_operator( p ):
    '''Expression : '(' Expression Op Expression ')' '''
    p[0] = [ p[3], p[2], p[4] ]
def p_expression_deref( p ):
    '''Expression : LefthandSide '''
    p[0] = [ "deref", p[1] ]
def p_expression_new( p ):
    '''Expression : new TypeTemplate '''
    p[0] = [ "new", p[2] ]
def p_expression_nil( p ):
    '''Expression : nil'''
    p[0] = "nil"