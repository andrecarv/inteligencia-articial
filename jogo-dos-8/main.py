from random import shuffle
CIMA,DIR,ESQ,BAIXO = 'c','d','e','b'

class Game(object):

    def __init__(self):
        numeros = range(1,9)
        numeros.append(None)
        shuffle(numeros)
        self.pos = [0,0]
        self.board =[[None,None,None] for i in xrange(3)]
        for i in xrange(3):
            for j in xrange(3):
                self.board[i][j] = numeros.pop()
                if self.board[i][j] is None: self.pos =[i,j]

    def move(self, direction):
        if direction == CIMA:
            direction = [-1,0]
        elif direction == BAIXO:
            direction = [1,0]
        elif direction == DIR:
            direction = [0,1]
        elif direction == ESQ:
            direction = [0,-1]
        x,y= self.pos
        i,j = direction
        try:
            temp = self.board[x+i][y+j]
        except:
            print "invalid move"
            return
        self.board[x][y] = temp
        self.board[x+i][y+j] = None
        self.pos = [x+i,y+j]

    def check_game_over(self):
        if self.board == [[1,2,3],[4,5,6],[7,8,None]]:
            return True
        return False

    def print_board(self):
        for line in self.board:
            print line

    def get_player_input(self):
        _inp = raw_input('Escolha uma direcao para mover o None ((c)ima,(b)aixo,(d)ireita,(e)squerda) ou (Q) para sair ')
        return _inp

    def game_loop(self):
        while True:
            self.print_board()
            _inp = self.get_player_input()
            if _inp == 'Q' or _inp == 'q':
                print 'saindo...'
                return
            self.move(_inp)
            if self.check_game_over():
                print 'Voce venceu o jogo!'
                return

if __name__ == '__main__':
    jogo = Game()
    jogo.game_loop()


