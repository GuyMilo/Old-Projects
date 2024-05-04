import math
import pygame as p
from FireEmblemConstants import SQ_SIZE , DIMENSION , png_dict , screen, RED, BLUE

class Unit:
    
    def __init__(self,name,unit,team):
        self.row = DIMENSION
        self.col = DIMENSION
        self.name = name
        self.team = True or False
        self.x = 0
        self.y = 0
        self.calc_pos()
        self.wpnMt = 0
        self.wpnacc = 0 
        self.wmpWt = 0
        self.hit = 100
        self.evd = 10
        self.evdMtr = 0
        self.crithit = 0
        self.critevd = 0
        self.dodgeCnt = 0
        self.critCnt = 0
        self.wpnCrit = 0

    def calc_pos(self):
        self.x = SQ_SIZE * self.col + SQ_SIZE // 2 
        self.y = SQ_SIZE * self.row + SQ_SIZE // 2

#List of Playable Units
    def BC(self,window):
        self.name = "B!Chrom"
        (window,BLUE,window.blit(png_dict), (self.x,self.y))
        self.hp = 20
        self.mt = 7
        self.skl = 8
        self.spd = 8
        self.lck = 5
        self.df = 7
        self.con = 8
        self.wpnTri = "sword"
        self.wpn = "Exalted Falchion"
        self.wpnCrit = 5
    
    def RC(self,window):
        self.name = "Chrom"
        (window,RED,window.blit(png_dict), (self.x,self.y))
        self.hp = 20
        self.mt = 7
        self.skl = 8
        self.spd = 8
        self.lck = 5
        self.df = 7
        self.con = 8
        self.wpnTri= "sword"
        self.wpn = "Exalted Falchion"
        self.wpnCrit = 5

    def BO(self,window):
        self.name = "Owain"
        (window,BLUE,window.blit(png_dict), (self.x,self.y))
        self.hp = 18
        self.mt = 8
        self.skl = 6
        self.spd = 7
        self.lck = 10
        self.df = 7
        self.con = 8
        self.wpnTri= "sword"
        self.wpn = "steel"
        self.wpnCrit = 5
    
    def RO(self,window):
        self.name = "Owain"
        (window,RED,window.blit(png_dict), (self.x,self.y))
        self.hp = 18
        self.mt = 8
        self.skl = 6
        self.spd = 7
        self.lck = 10
        self.df = 7
        self.con = 8
        self.wpnTri= "sword"
        self.wpn = "steel"
        self.wpnCrit = 5
    
    def RH(self,window):
        self.name = "Hector"
        (window,RED,window.blit(png_dict), (self.x,self.y))
        self.hp = 20
        self.mt = 10
        self.skl = 4
        self.spd = 4
        self.lck = 3
        self.df = 12
        self.con = 13
        self.wpnTri= "axe"
        self.wpn = "silver"
    
    def BH(self,window):
        self.name = "Hector"
        (window,BLUE,window.blit(png_dict), (self.x,self.y))
        self.hp = 20
        self.mt = 10
        self.skl = 4
        self.spd = 4
        self.lck = 3
        self.df = 12
        self.con = 13
        self.wpnTri= "axe"
        self.wpn = "silver"
    
    def BM(self,window):
        self.name = "Marth"
        (window,BLUE,window.blit(png_dict), (self.x,self.y))
        self.hp = 22
        self.mt = 6
        self.skl = 3
        self.spd = 9
        self.lck = 7
        self.df = 7
        self.con = 13
        self.wpnTri= "sword"
        self.wpn = "Falchion"
        self.wpnCrit = 10

    def RM(self,window):
        self.name = "Marth"
        (window,RED,window.blit(png_dict), (self.x,self.y))
        self.hp = 22
        self.mt = 6
        self.skl = 3
        self.spd = 9
        self.lck = 7
        self.df = 7
        self.con = 13
        self.wpnTri = "sword"
        self.wpn = "Falchion"
        self.wpnCrit = 10
    
    def BA(self,window):
        self.name = "Alm"
        (window,BLUE,window.blit(png_dict), (self.x,self.y))
        self.hp = 25
        self.mt = 9
        self.skl = 7
        self.spd = 7
        self.lck = 7
        self.df = 5
        self.con = 13
        self.wpnTri= "sword"
        self.wpn = "steel"
        self.wpnCrit = 5
    
    def RA(self,window):
        self.name = "Alm"
        (window,RED,window.blit(png_dict), (self.x,self.y))
        self.hp = 25
        self.mt = 9
        self.skl = 7
        self.spd = 7
        self.lck = 7
        self.con = 13
        self.wpnTri= "sword"
        self.wpn = "steel"
        self.wpnCrit = 5
    
    def RE(self,window):
        self.name = "Edelgard"
        (window,RED,window.blit(png_dict), (self.x,self.y))
        self.hp = 26
        self.mt = 10
        self.skl = 5
        self.spd = 8
        self.lck = 5
        self.df = 8
        self.con = 8
        self.wpnTri= "axe"
        self.wpn = "steel"

    
    def BE(self,window):
        self.name = "Edelgard"
        (window, BLUE,window.blit(png_dict), (self.x,self.y))
        self.hp = 26
        self.mt = 10
        self.skl = 5
        self.spd = 8
        self.lck = 5
        self.df = 8
        self.con = 8
        self.wpnTri= "axe"
        self.wpn = "steel"

    
    def RR(self,window):
        self.name = "Raiden"
        (window,RED,window.blit(png_dict), (self.x,self.y))
        self.hp = 25
        self.mt = 6
        self.skl = 7
        self.spd = 10
        self.lck = 7
        self.df = 5
        self.con = 8
        self.wpnTri= "sword"
        self.wpn = "iron"
        self.wpnCrit = 15
    
    def BR(self,window):
        self.name = "Raiden"
        (window,BLUE,window.blit(png_dict), (self.x,self.y))
        self.hp = 25
        self.mt = 6
        self.skl = 7
        self.spd = 10
        self.lck = 7
        self.df = 5
        self.con = 8
        self.wpnTri= "sword"
        self.wpn = "iron"
        self.wpnCrit = 10
    
    def BS(self,window):
        self.name = "B!Selena"
        (window,BLUE,window.blit[png_dict()], (self.x,self.y))
        self.hp = 19
        self.mt = 8
        self.skl = 11
        self.spd = 11
        self.lck = 6
        self.df = 6
        self.con = 8
        self.wpnTri= "sword"
        self.wpn = "iron"
 
    def RS(self,window):
        self.name = "R!Selena"
        (window,BLUE,window.blit(png_dict), (self.x,self.y))
        self.hp = 19
        self.mt = 8
        self.skl = 11
        self.spd = 11
        self.lck = 6
        self.df = 6
        self.con = 8
        self.wpnTri= "sword"
        self.wpn = "iron"
        self.wpnMt = 0
        self.wpnacc = 0 
        self.wmpWt = 0


    def wpn_equip(self):
        for self.wpnTri in Unit:
            if (self.wpnTri =="sword"):
                if(self.wpn == "iron"):
                    self.wpnMt = 5
                    self.wpnacc = 90
                    self.wmpWt = 4
                if(self.wpn == "steel"):
                    self.wpnMt = 8
                    self.wpnacc = 85
                    self.wmpWt = 6
                if(self.wpn == "Falchion"):
                    self.wpnMt = 11
                    self.wpnacc = 80
                    self.wpnCrit = 10
                    self.wmpWt = 10 
                if(self.wpn == "Exalted Falchion"):
                    self.wpnMt = 12
                    self.wpnacc = 70
                    self.wpnCrit = 15
                    self.wmpWt = 10
        
            if (self.wpnTri =="axe"):
                if(self.wpn == "steel"):
                    self.wpnMt = 11
                    self.wpnacc = 70
                    self.wmpWt = 8
                if(self.wpn == "silver"):
                    self.wpnMt = 15
                    self.wpnacc = 65
                    self.wmpWt = 10
    
    def unitStats(self):
        self.mt = math.floor(self.mt + self.wpnMt)
        self.hit = math.floor((self.skl*1.5) + (self.lck * .5) + (self.wpnacc) + (self.con - self.wmpWt))
        self.evd =  math.floor((self.spd * 1.5) + (self.lck * .5))
        self.crithit = math.floor(self.skl / 2) + self.wpnCrit
        self.critevd = math.floor(self.lck)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    
    def __repr__(self):
        self.team = RED or BLUE
        return str(self.team)


    

        
    

