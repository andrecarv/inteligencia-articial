'''
Created on Apr 12, 2016

@author: andre
'''
import sys
from piece import _path, Piece
from position import Position
SEQUENCE_VALUE = [10, 1000, 150000, 100000000, 9999999999999]

class IAPlayer(object):
    
    def __init__(self):
        pass
    
    def calculate_move(self, board):
        moves = self.derivate_board('B', board)
        best_move = moves.pop(0)
        best_value = self.minimax_alpha_beta_pruning(best_move)
        for m in moves:
            aux = self.minimax_alpha_beta_pruning(m)
            if best_value < aux:
                best_move = m
                best_value = aux
        return best_move
    
    def minimax_alpha_beta_pruning(self, board, depth=5, _a=(-sys.maxint - 1), _b=sys.maxint, ia_turn=False):
        if depth == 0 or board.check_victory():
            return self.evaluate(board)
        if ia_turn:
            aux = -sys.maxint - 1
            for b in self.derivate_board('B', board):
                aux = max((aux, self.minimax_alpha_beta_pruning(b, depth - 1, _a, _b, not ia_turn)))
                _a = max((_a, aux))
                if _b <= _a:
                    break
            return aux
        else:
            aux = sys.maxint
            for b in self.derivate_board('W', board):
                aux = min((aux, self.minimax_alpha_beta_pruning(b, depth - 1, _a, _b, not ia_turn)))
                _b = min((_b, aux))
                if _b <= _a:
                    break
            return aux
    
    def minimax(self, board, depth, ia_turn=True):
        if depth == 0 or board.check_victory():
            return self.evaluate()
        if ia_turn:
            _result = -sys.maxint - 1
            for b in self.derivate_board('B', board):
                _result = max((self.minimax(board, depth - 1, False), _result))
            return _result
    
    def derivate_piece(self, player_turn, piece):
        d_pieces = []
        for direction in _path.values():
            position = piece.get_position() + direction
            d_pieces.append(Piece(position, player_turn))
            position += direction
            d_pieces.append(Piece(position, player_turn))
        return d_pieces
    
    def derivate_board(self, player_turn, board):
        d_boards = []
        for piece in board.get_pieces():
            b = board.copy()
            for p in self.derivate_piece(player_turn, piece):
                if b.put_piece(p):
                    d_boards.append(b)
        return d_boards
        
    def evaluate(self, board):
        # funcao de utilidade
        board = board.copy()
        _color = None
        for i in xrange(15):
            for j in xrange(15):
                _seq  = True
                board.piece_at((j,i))
                
        pass
        
