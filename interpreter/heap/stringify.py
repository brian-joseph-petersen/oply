def stringify( oply ):
    print
    keys = oply.heap.keys()
    keys.sort()
    for key in keys: print( "[" + key + "] " + str( oply.heap[key] ) )