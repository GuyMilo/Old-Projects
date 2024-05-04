import pygame as p
from FireEmblemConstants import RED, BLUE, SQ_SIZE
from FireEmblemEngine import BoardState


class Game:
    def __init__(self, window):
        self._init()
        self.window = window

    
    def update(self):
        self.board.generate(self.window)
        self.draw_valid_moves(self.valid_moves)
        p.display.update()

    def _init(self):
        self.selected = None
        self.board = BoardState()
        self.turn = BLUE
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        unit = self.board.get_unit(row, col)
        if unit != 0 and self.team == self.turn:
            self.selected = unit
            self.valid_moves = self.board.get_vaild_moves(unit)
            return True
            
        return False

    def _move(self, row, col):
        unit = self.board.get_unit(row, col)
        if self.selected and unit == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            p.draw.rect(self.window, BLUE, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE,SQ_SIZE))

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLUE:
            self.turn = RED
        else:
            self.turn = BLUE

