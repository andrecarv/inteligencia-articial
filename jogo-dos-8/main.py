from random import shuffle
CIMA,DIR,ESQ,BAIXO = 0,1,2,3

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

    def move(direction):
        if direction == CIMA:
            direction = [0,-1]
        elif direction == BAIXO:
            direction = [0,1]
        elif direction == DIR:
            direction = [-1,0]
        elif direction == ESQ:
            direction = [1,0]
        x,y= self.pos
        i,j = direction
        try:
            temp = self.board[x+i][y+j]
        except:
            print "invalid move"
            return
        self.board[x][y] = temp
        self.board[x+i][y+j] = None

if __name__ == '__main__':
    jogo = Game()
    for line in jogo.board:
        print line


