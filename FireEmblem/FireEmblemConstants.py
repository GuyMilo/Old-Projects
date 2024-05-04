import pygame as p

WIDTH = HEIGHT = 640

DIMENSION = 8  #8x8 are the dimensions of the game board

SQ_SIZE = HEIGHT // DIMENSION

RedUnits = 8
BlueUnits = 8
RED = False
png_dict= {
    #Red Team
    "RS": p.transform.scale(p.image.load("Images/RS.png"), (SQ_SIZE,SQ_SIZE)),
    "RA": p.transform.scale(p.image.load("Images/RA.png"), (SQ_SIZE,SQ_SIZE)),
    "RH": p.transform.scale(p.image.load("Images/RH.png"), (SQ_SIZE,SQ_SIZE)),
    "RC": p.transform.scale(p.image.load("Images/RC.png"), (SQ_SIZE,SQ_SIZE)),
    "RM": p.transform.scale(p.image.load("Images/RM.png"), (SQ_SIZE,SQ_SIZE)),
    "RE": p.transform.scale(p.image.load("Images/RE.png"), (SQ_SIZE,SQ_SIZE)),
    "RO": p.transform.scale(p.image.load("Images/RO.png"), (SQ_SIZE,SQ_SIZE)),
    "RR": p.transform.scale(p.image.load("Images/RR.png"), (SQ_SIZE,SQ_SIZE)),
    #Blue Team
    "BR": p.transform.scale(p.image.load("Images/BR.png"), (SQ_SIZE,SQ_SIZE)),
    "BO": p.transform.scale(p.image.load("Images/BO.png"), (SQ_SIZE,SQ_SIZE)),
    "BE": p.transform.scale(p.image.load("Images/BE.png"), (SQ_SIZE,SQ_SIZE)),
    "BM": p.transform.scale(p.image.load("Images/BM.png"), (SQ_SIZE,SQ_SIZE)),
    "BC": p.transform.scale(p.image.load("Images/BC.png"), (SQ_SIZE,SQ_SIZE)),
    "BH": p.transform.scale(p.image.load("Images/BH.png"), (SQ_SIZE,SQ_SIZE)),
    "BA": p.transform.scale(p.image.load("Images/BA.png"), (SQ_SIZE,SQ_SIZE)),
    "BS": p.transform.scale(p.image.load("Images/BS.png"), (SQ_SIZE,SQ_SIZE)),
}
EMPTY = 0
BLUE = True

LGREEN = (127,255,212)
WHITE = (255, 255, 255)

screen = p.display.set_mode((WIDTH, HEIGHT),p.RESIZABLE)
# window = screen.fill(p.color("white"))
map1 = (p.image.load("Images/map1.png"),p.RESIZABLE)

"""This board is a 8x8 2d list, each element of are list are comprised  four characters.
    The character on the left side of the comma will repesent which team the unit is on (Red or Blue), 
    and the left side is each unit defined (ex.Alm, Selena, Raiden, etc.)"""

INITIAL_MAP=[["RS", "RA", "RH", "RC", "RM", "RE", "RO", "RR"], # Players on side Red Team
             ["--", "--", "--", "--", "--", "--", "--", "--"], #To define bank space, I used "--" defined as a string
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["--", "--", "--", "--", "--", "--", "--", "--"],
             ["--", "--", "--", "--", "--", "--", "--", "--"], #This layout should represent what our board should look like
             ["BR", "BO", "BE", "BM", "BC", "BH", "BA", "BS"],]

"""
Now, because loading images in is an expensive operation, we will load images in 
by initialize global dictionary of images.
"""

png_dict = {
    #Red Team
    "RS": p.transform.scale(p.image.load("Images/RS.png"), (SQ_SIZE,SQ_SIZE)),
    "RA": p.transform.scale(p.image.load("Images/RA.png"), (SQ_SIZE,SQ_SIZE)),
    "RH": p.transform.scale(p.image.load("Images/RH.png"), (SQ_SIZE,SQ_SIZE)),
    "RC": p.transform.scale(p.image.load("Images/RC.png"), (SQ_SIZE,SQ_SIZE)),
    "RM": p.transform.scale(p.image.load("Images/RM.png"), (SQ_SIZE,SQ_SIZE)),
    "RE": p.transform.scale(p.image.load("Images/RE.png"), (SQ_SIZE,SQ_SIZE)),
    "RO": p.transform.scale(p.image.load("Images/RO.png"), (SQ_SIZE,SQ_SIZE)),
    "RR": p.transform.scale(p.image.load("Images/RR.png"), (SQ_SIZE,SQ_SIZE)),
    #Blue Team
    "BR": p.transform.scale(p.image.load("Images/BR.png"), (SQ_SIZE,SQ_SIZE)),
    "BO": p.transform.scale(p.image.load("Images/BO.png"), (SQ_SIZE,SQ_SIZE)),
    "BE": p.transform.scale(p.image.load("Images/BE.png"), (SQ_SIZE,SQ_SIZE)),
    "BM": p.transform.scale(p.image.load("Images/BM.png"), (SQ_SIZE,SQ_SIZE)),
    "BC": p.transform.scale(p.image.load("Images/BC.png"), (SQ_SIZE,SQ_SIZE)),
    "BH": p.transform.scale(p.image.load("Images/BH.png"), (SQ_SIZE,SQ_SIZE)),
    "BA": p.transform.scale(p.image.load("Images/BA.png"), (SQ_SIZE,SQ_SIZE)),
    "BS": p.transform.scale(p.image.load("Images/BS.png"), (SQ_SIZE,SQ_SIZE)),
}

EMPTY_SPACES = ["--" for _ in range(64)]

