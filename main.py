import pygame as pg
import os
os.environ['pg_HIDE_SUPPORT_PROMPT'] = "True"
from settings import *
from piece import *

class Game:
    def __init__(self, width, height) -> None:
        self.level = 2
        self.score = 0
        self.state = "start"
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.piece = None
        self.height = height
        self.width = width
        self.field = [[0 for i in range(width)] for j in range(height)]

    def new_piece(self):
        self.piece = Piece(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.piece.image() and (i + self.piece.y > self.height - 1 or j + self.piece.x > self.width - 1 or j + self.piece.x < 0 or self.field[i + self.piece.y][j + self.piece.x] > 0):
                    intersection = True
        return intersection

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.piece.image():
                    self.field[i + self.piece.y][j + self.piece.x] = self.piece.type
        self.break_lines()
        self.new_piece()
        if self.intersects():
            self.state = "gameover"

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def hard_drop(self):
        while not self.intersects():
            self.piece.y += 1
        self.piece.y -= 1
        self.freeze()

    def go_down(self):
        self.piece.y += 1
        if self.intersects():
            self.piece.y -= 1
            self.freeze()

    def go_side(self, dx):
        old_x = self.piece.x
        self.piece.x += dx
        if self.intersects():
            self.piece.x = old_x

    def rotate(self):
        old_rotation = self.piece.rotation
        self.piece.rotate()
        if self.intersects():
            self.piece.rotation = old_rotation

if __name__ == "__main__":
    pg.init()

    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption("Tetris")
    done = False
    clock = pg.time.Clock()
    game = Game(10, 20)
    counter = 0

    pressing_down = False

    while not done:
        if game.piece is None:
            game.new_piece()
        counter += 1
        if counter > 999999999:
            counter = 0

        if counter % (FPS // game.level // 2) == 0:
            if game.state == "start":
                game.go_down()

        if pressing_down and counter % (FPS // game.level // DROPSPEED) == 0:
            game.go_down()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if game.state != "gameover":
                    if event.key in UP:
                        game.rotate()
                    if event.key in DROP:
                        pressing_down = True
                    if event.key in LEFT:
                        game.go_side(-1)
                    if event.key in RIGHT:
                        game.go_side(1)
                    if event.key in HARD_DROP:
                        game.hard_drop()
                if event.key == pg.K_ESCAPE:
                    game.__init__(game.width, game.height)

            if event.type == pg.KEYUP:
                if event.key in DROP:
                    pressing_down = False

        screen.fill(WHITE)

        for i in range(game.height):
            for j in range(game.width):
                pg.draw.rect(screen, GREY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pg.draw.rect(screen, colors[game.field[i][j]],
                                    [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        if game.piece is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.piece.image():
                        pg.draw.rect(screen, game.piece.color,
                                        [game.x + game.zoom * (j + game.piece.x) + 1,
                                        game.y + game.zoom * (i + game.piece.y) + 1,
                                        game.zoom - 2, game.zoom - 2])

        font = pg.font.SysFont('Calibri', 25, True, False)
        font1 = pg.font.SysFont('Calibri', 65, True, False)
        text = font.render("SCORE: " + str(game.score), True, BLACK)
        text_game_over = font1.render("GAME OVER", True, BLACK)
        text_game_over1 = font1.render("PRESS ESC", True, BLACK)

        screen.blit(text, [10, 10])
        if game.state == "gameover":
            screen.blit(text_game_over, [20, 200])
            screen.blit(text_game_over1, [25, 265])

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()