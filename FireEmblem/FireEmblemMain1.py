""""Our main file is the driver file. This file will be responsible for
handling user input and displaying the current GameState object"""
# for this .pyfile we are going to need to import our Game engine into the main file is we habe access to the board and game state
import pygame as p
import sys
from random import choice
from FireEmblemChar import Unit
from FireemblemGameState import Game
from FireEmblemConstants import SQ_SIZE, WIDTH,HEIGHT
import time as t

MAX_FPS = 60  # This will be for our animations
playerClicks = p.MOUSEBUTTONDOWN
screen = p.display.set_mode((WIDTH, HEIGHT),p.RESIZABLE)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQ_SIZE
    col = x // SQ_SIZE
    return row,col
#The main driver will handle the updating of graphics

def main():
    clock = p.time.Clock()
    running = True
    game = Game(screen)

    while running:
        clock.tick(MAX_FPS)

        if game.winner() != None:
            p.display.set_caption(game.winner())
            t.sleep(15)
            running = False

        for e in p.event.get():
            if e.type == p.QUIT:
               running = False
            if e.type == playerClicks:
                location = p.mouse.get_pos() #this will allow python to track the (x,y) coordinates of our mouse
                row, col = get_row_col_from_mouse(location)
                game.select(row, col)

            
            game.update()
        
        p.quit()

main()


  
            # elif playerClicks == Unit:
            #         for PL in (m,n):
            #             p.display("Name: " self.name)
            #             p.display("HP: " self.hp)
            #             p.display("Mt: " self.mt +self.wpn)
            #             p.display("Skl: " self.skl)
            #             p.display("Spd: " self.spd)
            #             p.display("Lck: " self.lck)
            #             p.display("Def: " self.df)
            #             p.display("Res: " self.res)
            #             p.display("Acc: " self.hit)
            #             p.display("Evd: " self.evd)




'''
#This second sub-function is responsible for drawing the peices on the board in relation to the current GameState
'''

                


