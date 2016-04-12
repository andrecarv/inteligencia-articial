'''
Created on Apr 12, 2016

@author: andre
'''
_path = {'up' : (-1, 0), 'down' : (1, 0), 'left' : (0, -1), 'right':(0, 1),
              'upper left':(-1, -1), 'upper right':(-1, 1), 'bottom left': (1, -1), 'bottom right':(1, 1)}
        
class Piece(object):
    
    def __init__(self, position, color):
        self.pos = position
        self.color = color
        
    def check_sequences(self, board):
        directions = {'-':1, '|':1, '\\':1, '/':1}
        for d in _path.keys():
            i = self._check_sequence(d, board)
            if d in ('up','down'):
                directions['|'] += i
            elif d in ('left','right'):
                directions['-'] += i
            elif d in ('upper left', 'bottom right'):
                directions['\\'] += i
            else:
                directions['/'] += i
        for v in directions.values():
            if v >= 5:
                return True
        return False
        
    def _check_sequence(self, direction, board, i=0):
        pos = self.pos + _path[direction]
        piece = board.piece_at(pos)
        if piece is not None:
            if piece.get_color() == self.color and i < 4:
                return piece._check_sequence(direction, board, i + 1)
        return i
            
    def get_position(self):
        return self.pos
    
    def get_color(self):
        return self.color
    