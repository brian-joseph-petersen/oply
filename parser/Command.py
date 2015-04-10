def p_command( p ):
    '''Command : LefthandSide '=' Expression'''
    p[0] = [ "=", p[1], p[3] ]
def p_command_if( p ):
    '''Command : if Expression ':' CommandList else CommandList end '''
    p[0] = [ "if", p[2], p[4], p[6] ]
def p_command_print( p ):
    '''Command : print Expression'''
    p[0] = [ "print", p[2] ]
def p_command_call( p ):
    '''Command : LefthandSide '(' ExpressionList ')' '''
    p[0] = [ "call", p[1], p[3] ]