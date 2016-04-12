'''
Created on Apr 12, 2016

@author: andre
'''
class IAPlayer(object):
    
    def __init__(self):
        pass
    
    def derivate_board(self, player_turn, board, depth=5):
        for piece in board.get_pieces():
            pass
        b = board.copy()
        