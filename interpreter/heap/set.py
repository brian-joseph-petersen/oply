def set( oply, index, identifier, value ):
    if index not in oply.heap or identifier not in oply.heap[index]: raise Exception
    if isinstance( oply.heap[index][identifier], type( value ) ) is False: raise Exception
    oply.heap[index][identifier] = value