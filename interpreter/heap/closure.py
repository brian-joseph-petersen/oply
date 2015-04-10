from interpreter.heap import peek, declare
def closure( oply, index, declaration, identifier, identifiers, value ):
    H = "H" + str( oply.len )
    oply.heap[H] = [ declaration, value, index ] if identifiers == "nil" else [ declaration, identifiers, value, index ]
    oply.len = oply.len + 1
    index = peek( oply )
    declare( oply, index, identifier, H )