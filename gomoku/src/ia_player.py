'''
Created on Apr 12, 2016

@author: andre
'''
SEQUENCE_VALUE = [10, 1000, 150000, 100000000, 9999999999999]
class IAPlayer(object):
    
    def __init__(self):
        pass
    
    def derivate_board(self, player_turn, board, depth=5):
        for piece in board.get_pieces():
            """
            A ideia sera gerar jogadas a partir da primeira peca em todas a direcoes possiveis de fazer sequencia,
            ate no maximo duas casas de distancia da peca base e gerar tabuleiros para nova verificacao recursiva.
            """
            p = None  # aqui devera ser usado um algoritmo para definir a peca (posicao e player_turn)
            b = board.copy
            if b.put_piece(p):
                if depth < 1 or p.check_sequences(b):
                    self.evaluate(b)  # funcao de utilidade
                self.derivate_board(player_turn, board, depth - 1)
            pass
        b = board.copy()
        
    def evaluate(self, board):
        # funcao de utilidade
        pass
        
