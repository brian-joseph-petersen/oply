def declare( oply, index, identifier, value ):
    if index in oply.heap and identifier in oply.heap[index]: raise Exception
    oply.heap[index][identifier] = value