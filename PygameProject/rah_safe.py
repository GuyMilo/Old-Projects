# Imports

import pygame 
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 500 #set screen width
screen_height = 500 #set screen height
screen_size = (screen_width, screen_height) #create a variable screen_size
screen = pygame.display.set_mode(screen_size) #set the mode of the display in pygame to the parameters in the screen_size var

# colors
plum = (255,187,255) #plum RGB values
blueviolet = (138,43,226) #blue violet RGB values
white = (255, 255, 255) #white RGB values 
cyan2 = (0,238,238) #cyan2 RGB values
deeppink = (205,16,118) #deeppink RGB values

# boulevard and marker sizes
boulevard_width = 300 #sets size for the entire raod
marker_width = 10 #sets size for the lane markers
marker_height = 50 #sets height for the lane markers

# lane coordinates
left_lane = 150 #initializes left_lane variable and assigns value (position)
center_lane = 250 #initializes center_lane variable and assigns value (position)
right_lane = 350 #initializes right_lane variable and assigns value (position)
lanes = [left_lane, center_lane, right_lane] #initializing and assigning to an array with the position of all lanes

# boulevard and edge/barrier markers
boulevard = (100, 0, boulevard_width, screen_height) #determines position and size of boulevard
left_edge_marker = (95, 0, marker_width, screen_height) #determines position and size of left edge
right_edge_marker = (395, 0, marker_width, screen_height) #determines position and size of right edge

lane_marker_move_y = 0 #variable to help change the position of markers during the game

vehicle_select =  #sets image for car

car_x = 250 #x coordinate of car
car_y = 400 #y coordinate of car

# frame rate initialization
clock = pygame.time.Clock() #creating clock variable to keep track of time and determine frame rate
fps = 120 # frames per seccond

is_crashed = False #initializing and setting is_crashed variable to false
speed = 1.5 #starting speed of car
score = 0 #starting score of car
passed = 0 #passed variable to determine speed

obstacle_images = [pygame.image.load('111_animations/111 animations/obstacles/Group 152.png'),pygame.image.load('111_animations/111 animations/obstacles/Group 153.png'),pygame.image.load('111_animations/111 animations/obstacles/Group 154.png'),pygame.image.load('111_animations/111 animations/obstacles/Group 155.png')] #create array with all possible obstacles images
coin_image = pygame.image.load('111_animations/111 animations/brampton_coin.png') # initializes coin image and loads in asset
coin_image = pygame.transform.rotate(coin_image,90) #rotates position of coin image to orient it correctly


#class definitions
#defining item class for sprites in game
class Item(pygame.sprite.Sprite):              
    def __init__(self, image, x, y): #parameters for item class
        pygame.sprite.Sprite.__init__(self)  #calls the constructor for self

        # scales images to be within the size of the lane, also orients images
        image = pygame.transform.rotate(image, 270)
        image_scale = 40 / image.get_rect().width #scaling factor for images
        new_width = image.get_rect().width * image_scale #width reset based on scaling factor
        new_height = image.get_rect().height * image_scale #height reset based on scaling factor
        self.image = pygame.transform.scale(image, (new_width, new_height)) #replaces image atrribute of sprite with scaled image
        self.rect = self.image.get_rect() #retrieves the area of a rectangle enclosing the item
        self.rect.center = [x, y] #centres the rectangle/hitbox 
class Vehicle(Item): # Vehicle subclass of item class
    def __init__(self, x, y): #parameters for Vehicle class
        image = vehicle_select #assigns Image of vehicle to vehicle_select
        super().__init__(image, x, y) #calls the constructor from the parent item class

#create sprite groups
car_group = pygame.sprite.Group() #creates sprite group for cars
obstacle_group = pygame.sprite.Group() #creates sprite group for obstacles
coin_group = pygame.sprite.Group() #creates sprite group for coins

#create the vehicle object for the player
car = Vehicle(car_x, car_y) #takes position args for car

car_group.add(car) #adds new object to car sprite group


crash_image = pygame.image.load('111_animations/111 animations/Skill Issue Screen (death screen).png') #loads asset for crash_image into game
crash_scale = 500/crash_image.get_rect().width #scaling factor for crash image
crash_width = crash_image.get_rect().width * crash_scale #new width for crash image (determined by scaling factor)
crash_height = crash_image.get_rect().height * crash_scale #new height for crash image based on scaling factor
crash = pygame.transform.scale(crash_image, (crash_width, crash_height)) #scales crash image based on calculated height and width
crash_rect = crash.get_rect() #gets area of rectangle of crash image


running = True #running variable initialized and set to true to run game loop

#running loop
while running: #conditional 
    clock.tick(fps) #sets fps of game
    for event in pygame.event.get(): #monitors all events in pygame
        if event.type == QUIT: #quits game
            running = False
        # move the player's car using the left/right arrow keys
        if event.type == KEYDOWN: #checks if any keys are pressed
            if event.key == K_LEFT and car.rect.center[0] > left_lane: #runs if the left arrow key is pressed and the car is in the centre or right lane
                car.rect.x -= 100 #moves car to the left
            elif event.key == K_RIGHT and car.rect.center[0] < right_lane: #runs if the right arroy key is pressed and the car is in the centre or left lane
                car.rect.x += 100 #moves car to the right

    screen.fill(blueviolet)     # draws the ground
    
    pygame.draw.rect(screen, plum, boulevard) # draws the boulevard



    pygame.draw.rect(screen, deeppink, left_edge_marker)  # draws the left barrier
    pygame.draw.rect(screen, deeppink, right_edge_marker) # draws the right barrier

    lane_marker_move_y += speed * 2 #draws out the lane markers
    if lane_marker_move_y >= marker_height * 2: #determines movement of marke based on position
        lane_marker_move_y = 0
    for y in range(marker_height * -2, screen_height, marker_height * 2): #initializes for loop based on marker height and screen height
        pygame.draw.rect(screen, cyan2, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height)) #draws out left lane marker
        pygame.draw.rect(screen, cyan2, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height)) #draws out right lane marker
    
    car_group.draw(screen) #draws all sprites in car_group
    
    #adds obstacles to game
    if len(obstacle_group) < 2: #runs if there are less than a minimum amount of obstacles on screen
  
        add_obstacle = True #sets add_obstacle to true
        for obstacle in obstacle_group:
            if obstacle.rect.top < obstacle.rect.height * 1.5: #checks distance between obstacles to determine whether or not they should be added
                add_obstacle = False #sets add_obstacle to false
        if add_obstacle:
   
            lane = random.choice(lanes) #chooses random lane to add obstacle to 

            image = random.choice(obstacle_images) #chooses one of four possible obstacle images
            image = pygame.transform.rotate(image, 90) #orients image
            obstacle = Item(image, lane, screen_height / -2) #constructs obstacle object
            obstacle_group.add(obstacle) #adds obstacle item to obstacle group

    # movement of obstacles
    for obstacle in obstacle_group: 
        obstacle.rect.y += speed #moves obstacle based on game speed 

        if obstacle.rect.top >= screen_height: #removes obstacles from group once they go past car
            obstacle.kill() #removes obstacle
            passed+=1 #increments passed variable to determine speed of game

            if passed > 0 and passed % 5 == 0: #increases speed when 5 obstacles are passed
                speed += 0.5

    obstacle_group.draw(screen) #draws sprites in obstacle group

    
    if len(coin_group) < 2: #ensures there is a minimum number of coin objects in the game
        add_coin = True #sets add_coin to true
        for coin in coin_group:
            if coin.rect.top < coin.rect.height * 1.2: #determines distance between coin objects
                add_coin = False #sets add_coin to false
        if add_coin:

            lane = random.choice(lanes) #finds random lane to place coin in
            coin = Item(coin_image, lane, screen_height / -2) #creates coin object
            coin_group.add(coin) #adds coin object to coin group
    for coin in coin_group:
        coin.rect.y += speed #determines movement of coin based on game speed
        if coin.rect.top >= screen_height: #if the coin is uncollected, it will be removed from the coin group
            coin.kill()
    coin_group.draw(screen) #draws sprites in coin group
    font = pygame.font.Font(pygame.font.get_default_font(), 16) # sets game font
    text = font.render('Score: ' + str(score), True, white) # sets parameters for text on screen
    text_rect = text.get_rect() #gets rectangular area of text
    text_rect.center = (50, 400) #sets position of text
    screen.blit(text, text_rect) #displays text on screen

    if pygame.sprite.spritecollide(car, coin_group, True): #checks for collisions with coins
        score += 1 #increases score if a coin is collected
        coin.remove() #removes coin once collected
    if pygame.sprite.spritecollide(car, obstacle_group, True): #checks for collisions with obstacles
        is_crashed = True #sets is_crashed to True
        crash_rect.center = [car.rect.center[0], car.rect.top] #changes position of crash image
        if is_crashed:
            screen.blit(crash, (0, 100)) #displays crash image
    pygame.display.update() #updates display so that changes are visible to player

    while is_crashed: #runs if the vehicle collides with an obstacle
        clock.tick(fps) #resets fps of game
        for event in pygame.event.get(): #looks for events in game
            if event.type == QUIT: #checks if player wants to quit game
                is_crashed = False
                running = False 
            if event.type == KEYDOWN: #checks for user input (keys being pressed down)
                if event.key == K_y: #restarts the game if the player chooses yes (selectes Y key)
                    is_crashed = False
                    speed = 1.5 #resets game variables and groups
                    score = 0
                    passed = 0
                    obstacle_group.empty()
                    coin_group.empty()
                    car.rect.center = [car_x, car_y]
                elif event.key == K_n: #exits the game 
                    is_crashed = False
                    running = False
pygame.quit()