import pygame as py
py.init() 
running = True
Screen = py.display.set_mode((800,600))
bg_image = py.image.load(("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\Loadup_screen.png"))
display = py.transform.scale(bg_image, (800,600))
i = 0
width = 800
fps = 60
timer = py.time.Clock()
main_menu = True
char_select = False
game_screen = False
pause_game = False
Resumebtn = False
PauseBtn = None
menuBtn = None
startBtn = None
quitBtn = None
Charbtn = None
selected_button = None
char1 = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\_Barbie_Car.png")
char2 = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\blade_runner_car.png")
char3 = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\1973_Chevy_Malibu_Drive.png")
char4 = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\_Regular_Show_Cart.png")


selected_char = char2

font = py.font.Font('bladerunner.ttf',24)
Titlefont = py.font.Font('bladerunner.ttf',40)
startText = font.render('Start Game', True, 'black')
quitText = font.render('Quit', True, 'black')
CharText = font.render('Select Vehicle', True, "black")

def draw_game():
    global menuBtn, Pausebtn, main_menu, game_screen,pause_game
    
    
    menuBtn = py.draw.rect(Screen, "light gray", [10, 10, 260, 40],0,5)
    py.draw.rect(Screen, 'dark gray', [10, 10, 260, 40],5,5)
    text = font.render('Main Menu', True, 'black')
    Screen.blit(text, (15, 17))

    
    Pausebtn = py.draw.rect(Screen, "light gray", [10, 560, 260, 40],0,5)
    py.draw.rect(Screen, 'dark gray', [10, 560, 260, 40],5,5)
    text = font.render('Pause Game', True, 'black')
    Screen.blit(text, (15, 565))
    
    if menuBtn.collidepoint(x,y):
        main_menu = True
        game_screen = False
    elif Pausebtn.collidepoint(x,y):
        game_screen = False
        pause_game = True

def pause_menu():
    global Resumebtn,Resumetxt, quitBtn, main_menu, pause_game, running, game_screen, menuBtn
    
    Resumebtn = py.draw.rect(Screen, "Yellow", [220, 185, 250, 40], 0, 5)
    quitBtn = py.draw.rect(Screen, "light green", [220, 285, 250, 40], 0, 5)
    menuBtn = py.draw.rect(Screen, "magenta", [220, 385, 250, 40], 0, 5)

    Title = Titlefont.render("BladeJump Boulevard", True, "Black", "Purple")
    Resumetxt = font.render('Resume Game', True, 'black')
    quitText = font.render('Quit Game', True, 'black')
    CharText = font.render('Main Menu', True, "black")

    
    Screen.blit(Title, (200, 100))
    Screen.blit(Resumetxt, (230,200))
    Screen.blit(quitText, (230, 300))
    Screen.blit(CharText, (230, 400))
    
    
    if Resumebtn.collidepoint(x,y):
        pause_game = False
        game_screen = True
    if menuBtn.collidepoint(x,y):
        main_menu = True
        pause_game = False
    elif quitBtn.collidepoint(x, y):
        running = False

def draw_menu():
    global  startBtn, quitBtn, Charbtn
    startBtn = py.draw.rect(Screen, "Yellow", [220, 185, 270, 60], 0, 5)
    quitBtn = py.draw.rect(Screen, "light green", [320, 330, 250, 40], 0, 5)
    Charbtn = py.draw.rect(Screen, "magenta", [270, 260, 260, 40], 0, 5)

    Title = Titlefont.render("BladeJump Boulevard", True, "Black", "Purple")
    startText = font.render('Start Game', True, 'black')
    quitText = font.render('Quit', True, 'black')
    CharText = font.render('Select Vehicle', True, "black")

    
    Screen.blit(Title, (100, 100))
    Screen.blit(startText, (240, 200))
    Screen.blit(quitText, (350, 335))
    Screen.blit(CharText, (285, 265))

def charselect():
    global menuBtn, main_menu, char_select, selected_char
    global selected_button, char1Btn, char2Btn, char3Btn, char4Btn

    #This loads the car images
    char1Img = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\_Barbie_Car.png")
    char2Img = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\blade_runner_car.png")
    char3Img = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\1973_Chevy_Malibu_Drive.png")
    char4Img = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\_Regular_Show_Cart.png")
    
    #Draws character buttons
    char1Btn = py.draw.rect(Screen, "pink", [250, 50, 200, 100],0,5)
    char2Btn = py.draw.rect(Screen, "magenta", [250, 160, 200, 100],0,5)
    char3Btn = py.draw.rect(Screen, "sky blue", [250, 270, 200, 100],0,5)
    char4Btn = py.draw.rect(Screen, "green", [250, 380, 200, 100],0,5)

    #Now to to display character images 
    Screen.blit(char1Img, (250, 60))
    Screen.blit(char2Img, (250, 165))
    Screen.blit(char3Img, (250, 265))
    Screen.blit(char4Img, (280, 390)) 
    
    #Adds text for the function to use
    char1Text = font.render('Barbie Car', True, 'Sky Blue')
    char2Text = font.render('Blade Runner Car', True, 'Pink')
    char3Text = font.render('I drive Car', True, 'Orange')
    char4Text = font.render('Regular Show Car', True, 'White')
    
    # Displays the text On the right of each button
    Screen.blit(char1Text, (450, 80))
    Screen.blit(char2Text, (450, 185))
    Screen.blit(char3Text, (450, 295))
    Screen.blit(char4Text, (450, 410))

    #Now to draw a yellow rectangle around the selected
    #button to let the player know they have selected 'x' character
    if selected_button == 'char1':
        py.draw.rect(Screen, "yellow", [250, 50, 200, 100],5)
    elif selected_button == 'char2':
        py.draw.rect(Screen, "yellow", [250, 160, 200, 100],5)
    elif selected_button == 'char3':
        py.draw.rect(Screen, "yellow", [250, 270, 200, 100],5)
    elif selected_button == 'char4':
        py.draw.rect(Screen, "yellow", [250, 380, 200, 100],5)

    #Now to update the variable, 'selected_button' when a button is clicked
    if char1Btn.collidepoint(x,y):
        selected_button = 'char1'
    elif char2Btn.collidepoint(x, y):
        selected_button = 'char2'
    elif char3Btn.collidepoint(x, y):
        selected_button = 'char3'
    elif char4Btn.collidepoint(x, y):
        selected_button = 'char4'

    #Makes the main menu buttion that, when clicked, takes the player back to the main menu
    menuBtn = py.draw.rect(Screen, "light gray", [230, 500, 260, 40],0,5)
    py.draw.rect(Screen, 'dark gray', [230, 500, 260, 40],5,5)
    menutext = font.render('Main Menu', True, 'black')
    Screen.blit(menutext, (245, 510))
    if menuBtn.collidepoint(x,y):
        main_menu = True
        char_select = False


while running:
    #draws the background
    Screen.fill((0,0,0))
    Screen.blit(display, (i,0))
    Screen.blit(display, (width+i,0))
    
    #Calls the function if the corresponding variable is True
    if main_menu == True:
        display = py.transform.scale(bg_image, (800,600))
        bg_image = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\Loadup_screen.png")
        Screen.blit(display, (i,0))
        draw_menu()
    elif char_select == True:
        display = py.transform.scale(bg_image, (800,600))
        bg_image = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\Loadup_screen.png")
        Screen.blit(display, (i,0))
        charselect()
    elif game_screen == True: 
        display = py.transform.scale(bg_image, (800,600))
        bg_image = py.image.load(("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\Loadup_screen.png"))
        Screen.blit(display, (0,0))
        draw_game()
    elif pause_game == True:
        display = py.transform.scale(bg_image, (800,600))
        bg_image = py.image.load("C:\\Users\\Player1\\Desktop\\py files\\PygameProject\\pause_menu.png")
        Screen.blit(display, (0,0))
        pause_menu()

    #For loop to tell pygame what to do if a specific, "M1" corrdindate is clicked
    for event in py.event.get():
        # variable, i, will endlessly subtract from variable, i.e. i = i - 1
        # but, ONLY if variable, 'main_menu' == True
        if main_menu or char_select:
            i -= 1 
        #Tells pygame to close
        if event.type == py.QUIT:
            running = False
        #Conditions for certian M1 events 
        if event.type == py.MOUSEBUTTONUP:
            x,y = event.pos
            if main_menu == True:
                #if the start button is selected
                if startBtn.collidepoint(x, y):
                    main_menu = False
                    game_screen = True
                    draw_game
                #if the quit button is clicked
                elif quitBtn.collidepoint(x, y):
                    running = False
                #if The veichle select button is clicked
                elif Charbtn.collidepoint(x,y):
                    main_menu = False
                    char_select = True
            if char_select == True:
                charselect()
                if char1Btn.collidepoint(x, y):
                    selected_char = char1
                elif char2Btn.collidepoint(x, y):
                    selected_char = char2
                elif char3Btn.collidepoint(x, y):
                    selected_char = char3
                elif char4Btn.collidepoint(x, y):
                    selected_char = char4
        # This else state is incharge of making sure the image is constantly replaced, otherwise
        # We will only get one display of the image and a black screen,
        # or a stretched image if not coded in correctly.  Thus, that's what the else block of code is for
        else:              
                if i == -width:
                    Screen.blit(display, (width+i,0))
                    i = 0
    py.display.update()