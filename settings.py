import pygame as pg

pieces = [
    None,
    [[1, 5, 9, 13], [4, 5, 6, 7]],                                                  # Line 
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],                    # L 
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],                      # Reverse L 
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],                       # T 
    [[1, 2, 5, 6]],                                                                 # Square 
    [[0, 1, 5, 6], [1, 5, 4, 8]],                                                   # Left Zigzag 
    [[1, 2, 4, 5], [0, 4, 5, 9]]                                                    # Right Zigzag 
]
colors = [
    None, 
    (0, 255, 255), 
    (0, 0, 255), 
    (255, 127, 0), 
    (127, 0, 255), 
    (255, 255, 0),
    (255, 0, 0), 
    (0, 255, 0)
]

SIZE = (400, 500)
FPS = 250

WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)

UP = [pg.K_w, pg.K_UP]
LEFT = [pg.K_a, pg.K_LEFT]
DROP = [pg.K_s, pg.K_DOWN]
RIGHT = [pg.K_d, pg.K_RIGHT]
HARD_DROP = [pg.K_SPACE]

DROPSPEED = 10