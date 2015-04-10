def p_lefthand_side( p ):
    '''LefthandSide : ID'''
    p[0] = p[1]
def p_lefthand_side_dot( p ):
    '''LefthandSide : LefthandSide '.' ID'''
    p[0] = [ "dot", p[1], p[3] ]