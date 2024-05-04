"""This class is resposible for storing all the information about the current state of 
our Fire emblem game.  It will also be resposible for determining the vaild moves at the
current state.  It will also keep a move log for the program to keep track of"""

#Classes in python are used, remembering python is an object relation programming language, 
#to tell python how to create it's own objects.  To simplify, It's Python's blueprint funtion 

#all classes must have a function called "__init__(), this code is essential (like keys to a car),
#as it initates (turns on to paraphrase) the respective class."

import pygame as p
import random
from FireEmblemConstants import RedUnits, BlueUnits, DIMENSION, SQ_SIZE, LGREEN, EMPTY,WHITE
from FireEmblemChar import Unit, RED, BLUE

class BoardState: 
    def __init__(self): 
        self.board = []
        self.red_left = RedUnits
        self.blue_left = BlueUnits
        self.draw_board()
    
    '''
    #This first sub-function is responsible for drawing the movement squares on the board
    '''
    def draw_places(self, window):
        window.fill(WHITE)
        for row in range(DIMENSION):
            for col in range(row % 2,DIMENSION,2):
                p.draw.rect(window, LGREEN,( col*(SQ_SIZE), row*(SQ_SIZE),SQ_SIZE,SQ_SIZE))
    
    """This is for movement"""
    """We are, in this move function, just simply swapping values in our self.board list we declared"""
    def move(self,unit, row, col):
        self.board[unit.row][unit.col], self.board[row][col] = self.board[row][col], self.board[unit.row][unit.col]
        unit.move(row,col)

    def get_unit(self,row,col):
        return self.board[row][col]

    def render(self, window):
        window.blit(BLUE[""])
        window.blit(RED[""])
    
    def draw_board(self):
        for row in range(DIMENSION):
            self.board.append([])
            for col in range(DIMENSION):
                square = ((row+col)%2)
                if row == 1:
                    self.board[row].append(Unit(square,RED[{}]))
                elif row == 8:
                    self.board[row].append(Unit(square,BLUE[{}]))
                else:
                    self.board[row].append(EMPTY)
            else:
                self.board[row].append(EMPTY)


    def generate(self,window):
        self.draw_places(window)
        for row in range(DIMENSION):
            for col in range (DIMENSION):
                unit = self.board[row][col]
                if unit!= 0:
                        unit.generate(window)

    #import unitstrike later

    def remove(self, units):
        for unit in units:
            self.board[unit.row][unit.col] = 0
            for self.hp in unit:
                if self.hp == 0:
                    if unit.team == RED:
                        self.red_left -= 1
                    else:
                        self.blue_left -= 1
    
    def winner(self):
        if self.red_left <= 0:
            return BLUE
        elif self.blue_left <= 0:
            return RED

        return None
    
    def get_vaild_moves(self, unit):
        moves = {}
        up = unit.row - 1
        down = unit.row + 1
        left = unit.col - 1
        right = unit.col + 1
        row = unit.row
        col = unit.col

        if self.team == RED:

            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, unit.team, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, unit.team, right))
            moves.update(self._traverse_left(row +1, min(row+3, DIMENSION), 1, unit.team, left))
            moves.update(self._traverse_right(row +1, min(row+3, DIMENSION), 1, unit.team, right))
        
            moves.update(self._traverse_up(col -1, max(row-3, -1), -1, unit.team, up))
            moves.update(self._traverse_down(col -1, max(row-3, -1), -1, unit.team, down))
            moves.update(self._traverse_up(col +1, min(row+3, DIMENSION), 1, unit.team, up))
            moves.update(self._traverse_down(col +1, min(row+3, DIMENSION), 1, unit.team, down))
    
        if self.team == BLUE:

            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, unit.team, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, unit.team, right))
            moves.update(self._traverse_left(row +1, min(row+3, DIMENSION), 1, unit.team, left))
            moves.update(self._traverse_right(row +1, min(row+3, DIMENSION), 1, unit.team, right))
        
            moves.update(self._traverse_up(col -1, max(row-3, -1), -1, unit.team, up))
            moves.update(self._traverse_down(col -1, max(row-3, -1), -1, unit.team, down))
            moves.update(self._traverse_up(col +1, min(row+3, DIMENSION), 1, unit.team, up))
            moves.update(self._traverse_down(col +1, min(row+3, DIMENSION), 1, unit.team, down))
    



    def _traverse_up(self, start, stop, step, team, up, skipped=[]):
        moves = {}
        last = []
        for c in range(start, stop, step):
            if up < 0:
                break
            
            current = self.board[c][up]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(c, up)] = last + skipped
                else:
                    moves[(c, up)] = last
                
                if last:
                    if step == -1:
                        col = max(c-3, 0)
                    else:
                        col = min(c+3, DIMENSION)
                    moves.update(self._traverse_up(c+step, col, step, team, up-1,skipped=last))
                    moves.update(self._traverse_down(c+step, col, step, team, up+1,skipped=last))
                break
            elif current.team == team:
                break
            else:
                last = [current]

            up -= 1
        
        return moves

    def _traverse_down(self, start, stop, step, team, down, skipped=[]):
        moves = {}
        last = []
        for c in range(start, stop, step):
            if down >= DIMENSION:
                break
            
            current = self.board[c][down]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(c, down)] = last + skipped
                else:
                    moves[(c, down)] = last
                
                if last:
                    if step == -1:
                        col = max(c-3, 0)
                    else:
                        col = min(c+3, DIMENSION)
                    moves.update(self._traverse_up(c+step, col, step, team, down-1,skipped=last))
                    moves.update(self._traverse_down(c+step, col, step, team, down+1,skipped=last))
                break
            elif current.team == team:
                break
            else:
                last = [current]

            down += 1
        
        return moves

    def _traverse_left(self, start, stop, step, team, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, DIMENSION)
                    moves.update(self._traverse_left(r+step, row, step, team, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, team, left+1,skipped=last))
                break
            elif current.team == team:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, team, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= DIMENSION:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, DIMENSION)
                    moves.update(self._traverse_left(r+step, row, step, team, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, team, right+1,skipped=last))
                break
            elif current.team == team:
                break
            else:
                last = [current]

            right += 1
        
        return moves





    



    


     
        
    


        



















    