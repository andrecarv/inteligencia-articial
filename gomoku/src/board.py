'''
Created on Apr 12, 2016

@author: andre
'''
from position import Position
class Board(object):
    
    def __init__(self, pieces={}):
        self.pieces = pieces
        self.last_piece = None
        
    def put_piece(self, piece):
        if self.pieces.has_key(piece.get_position()):
            return False
        self.pieces[piece.get_position()] = piece
        return True
    
    def check_victory(self):
        if self.last_piece is not None:
            return self.last_piece.check_sequences()
        return False
    
    def piece_at(self, position):
        return self.pieces[position]
    
    def board_view(self):
        s = "  "
        for i in xrange(15):
            if i < 9:
                s += "   %d  " % (i + 1)
            else:
                s += "   %d " % (i + 1)
        s += "\n"
        for j in xrange(15):
            if j < 9: s += " %d" % (j + 1)
            else: s += "%d" % (j + 1)
            for i in xrange(15):
                color = ' '
                if self.pieces.has_key(Position(j, i)):
                    color = self.pieces[Position(j, i)].get_color()
                s += "|  %s  " % color
            s += "|\n"
        print s
        
    def copy(self):
        return Board(self.piece.copy())
    
        