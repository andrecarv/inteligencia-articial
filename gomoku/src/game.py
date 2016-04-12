'''
Created on Apr 5, 2016

@author: andre
'''
from board import Board
from position import Position
from piece import Piece

class Game(object):
    
    def __init__(self):
        self.b = Board()
        p = Position(5,5)
        for i in xrange(4):
            piece = Piece(p,'W')
            p += (1,0)
            self.b.put_piece(piece)
        self.players = ['Black', 'White']
        
    def game_loop(self):
        player = self.players.pop(0)
        while True:
            piece = self.get_move(player)
            if not self.b.put_piece(piece):
                print "Ja existe uma peca nesta posicao."
                continue
            self.b.board_view()
            if piece.check_sequences(self.b):
                break
            self.players.append(player)
            player = self.players.pop(0)
        # escrever qlq merda sobre vitoria
        if player == 'White':
            print "Voce ganhou %s, so pq o outro eh black." % player
        else:
            print "Voce ganhou %s, aposto que usou cotas" % player
    def get_move(self, player):
        move = raw_input("E a vez do jogador %s, digite sua jogada em coordenadas x y (valores entre 1 e 15)\n" % player)
        x, y = move.split(' ')
        x, y = int(x) - 1, int(y) - 1
        if x < 0 or x > 14 or y < 0 or y > 14: 
            print "Posicao invalida."
            self.get_move(player)
        position = Position(y, x)
        piece = Piece(position, player[0])
        return piece

if __name__ == '__main__':
    g = Game()
    g.game_loop()
    
