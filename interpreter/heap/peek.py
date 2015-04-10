def peek( oply ):
    length = len( oply.stack )
    return oply.stack[( length - 1 )] if length > 0 else "nil"