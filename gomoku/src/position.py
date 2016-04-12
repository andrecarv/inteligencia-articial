'''
Created on Apr 12, 2016

@author: andre
'''
class Position(object):
    
    def __init__(self, y, x):
        self.x, self.y = x, y
        
    def __add__(self, position):
        if isinstance(position, tuple) or isinstance(position, list):
            return Position(self.y + position[0], self.x + position[1])
        x = self.x + position.x
        y = self.y + position.y
        return Position(y, x)
    
    def __hash__(self):
        return hash((self.y, self.x))
        
    def __eq__(self, position):
        return (self.x, self.y) == (position.x, position.y)
    
    def __str__(self):
        return '(x:%d, y:%d)' % (self.x, self.y)
    
    def __getitem__(self, index):
        if index is 'V' or index is 'v':
            return self.y
        elif index == 'h' or index == 'H':
            return self.x