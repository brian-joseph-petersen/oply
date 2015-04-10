def p_command_list( p ):
    '''CommandList : Command
                   | Command ';' CommandList
                   | empty '''
    if ( len( p ) == 2 ) and ( p[1] != None ): p[0] = [ p[1] ]
    elif ( len( p ) == 4 ): p[0] = [ p[1] ] + p[3]
    else: p[0] = []