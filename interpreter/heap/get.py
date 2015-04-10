def get( oply, index, identifier ):
    if index not in oply.heap or identifier not in oply.heap[index]: raise Exception
    return oply.heap[index][identifier]