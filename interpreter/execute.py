from interpreter.heap import stringify
from interpreter.interpret import DTREE, CTREE
class execute():
    def __init__( self, program ):
        self.len = 0
        self.heap = {}
        self.stack = []
        H = "H" + str( self.len )
        self.heap[H] = { "$": "nil" }
        self.len = self.len + 1
        self.stack.append( H )
        for declaration in program[0]: DTREE( self, declaration )
        for command in program[1]: CTREE( self, command )
        stringify( self )