from interpreter.heap import peek, declare, get, set, namespace, closure

''' LTREE ::=  ID  |  [ "dot", LTREE, ID ]  '''
def LTREE( oply, lefthand_side ):
    if isinstance( lefthand_side, str ):
        index = peek( oply )
        if ( index == "nil" ): raise Exception
        identifier = lefthand_side
        if identifier not in oply.heap[index]:
            index = get( oply, index, "$" )
            if ( index == "nil" ): raise Exception
            if identifier not in oply.heap[index]: raise Exception
            return ( index, identifier )
        return ( index, identifier )
    else:
        index, identifier = LTREE( oply, lefthand_side[1] )
        return ( get( oply, index, identifier ), lefthand_side[2] )

''' TTREE ::=  [ "struct", DLIST ]  |  [ "call", LTREE ]  '''
def TTREE( oply, type_template ):
    if ( type_template[0] == "struct" ):
        index = namespace( oply )
        oply.heap[index]["$"] = peek( oply )
        oply.stack.append( index )
        for declaration in type_template[1]: DTREE( oply, declaration )
        oply.stack.pop()
        return index
    elif ( type_template[0] == "call" ):
        index, identifier = LTREE( oply, type_template[1] )
        return TTREE( oply, oply.heap[get( oply, index, identifier )][1] )

''' ETREE ::=  NUM  |  [ "+", ETREE, ETREE ] |  [ "deref", LTREE ]  |  [ "new", TTREE ]  |  "nil" '''
def ETREE( oply, expression ):
    if ( expression == "nil" ): return expression
    elif ( expression[0] == "new" ): return TTREE( oply, expression[1] )
    elif isinstance( expression, str ) and expression.isdigit(): return int( expression )
    elif ( expression[0] == "+" ) or ( expression[0] == "-" ):
        left = ETREE( oply, expression[1] )
        right = ETREE( oply, expression[2] )
        if isinstance( left, int ) and isinstance( right, int ):
            if ( expression[0] == "+" ): return left + right
            elif ( expression[0] == "-" ): return left - right
        else: raise Exception
    elif ( expression[0] == "deref" ):
        index, identifier = LTREE( oply, expression[1] )
        return get( oply, index, identifier )
    else: raise Exception

''' DTREE ::=  [ "int", ID, ETREE ]  |  [ "obj", ID, ETREE ]  |  [ "def", ID, ILIST, CLIST ]  |  [ "class", ID, TTREE ] '''
def DTREE( oply, declaration ):
    if ( declaration[0] == "int" ):
        index = peek( oply )
        identifier = declaration[1]
        value = ETREE( oply, declaration[2] )
        declare( oply, index, identifier, value )
    elif ( declaration[0] == "obj" ):
        index = peek( oply )
        identifier = declaration[1]
        value = ETREE( oply, declaration[2] )
        if value in oply.heap: declare( oply, index, identifier, value )
        elif ( value == "nil" ): declare( oply, index, identifier, value )
    elif ( declaration[0] == "def" ):
        index = peek( oply )
        identifier = declaration[1]
        identifiers = declaration[2]
        value = declaration[3]
        closure( oply, index, declaration[0], identifier, identifiers, value )
    elif ( declaration[0] == "class" ):
        index = peek( oply )
        identifier = declaration[1]
        identifiers = "nil"
        value = declaration[2]
        closure( oply, index, declaration[0], identifier, identifiers, value )
    else: raise Exception

''' CTREE ::=  [ "=", LTREE, ETREE ]  |  [ "if", ETREE, CLIST, CLIST ]  |  [ "print", LTREE ]  |  [ "call", LTREE, ELIST ] '''
def CTREE( oply, command ):
    if ( command[0] == "=" ):
        index, identifier = LTREE( oply, command[1] )
        value = ETREE( oply, command[2] )
        set( oply, index, identifier, value )
    elif ( command[0] == "print" ):
        print ETREE( oply, command[1] )
    elif ( command[0] == "if" ):
        commands = command[2] if ETREE( oply, command[1] ) != 0 else command[3]
        for cmd in commands: CTREE( oply, cmd )
    elif ( command[0] == "call" ):
        index, identifier = LTREE( oply, command[1] )
        pointer = oply.heap[get( oply, index, identifier )]
        arguments = pointer[1]
        commands = pointer[2]
        expressions = command[2]
        parameters = []
        for expression in expressions: parameters.append( ETREE( oply, expression ) )
        index = namespace( oply )
        oply.heap[index]["$"] = pointer[3];
        oply.stack.append( index )
        if len( parameters ) == len( arguments ):
            for identifier, value in enumerate( parameters ):
                identifier = arguments[identifier]
                declare( oply, index, identifier, value )
        for cmd in commands: CTREE( oply, cmd )
        oply.stack.pop()
    else: raise Exception