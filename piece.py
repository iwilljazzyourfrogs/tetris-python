import pygame as pg
from random import *

from settings import *

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.type = randint(1, len(pieces) - 1)
        self.piece = pieces[self.type]
        self.color = colors[self.type]
        self.rotation = 0

    def image(self):
        return self.piece[self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.piece)