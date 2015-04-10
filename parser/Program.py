def p_program( p ):
    '''Program : DeclarationList CommandList''' 
    p[0] = [ p[1], p[2] ]