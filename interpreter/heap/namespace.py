def namespace( oply ):
    H = "H" + str( oply.len )
    oply.heap[H] = { "$": "nil" }
    oply.len = oply.len + 1
    return H