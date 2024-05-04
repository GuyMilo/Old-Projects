# Imports

import pygame
import sys
import numpy as np
import random as rand
# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gameplay")

# Set colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255,255,0)

# Variables
speed = 10
# Lanes
lanes = np.zeros(shape=(2, 4))
lane_pos = [[400,10],[400,160],[400,310],[400,460]]


#Player

car_width, car_height = 200, 130
car_x, car_y = lane_pos[0]
car_distance = 0
#Obstacle
crash_obstacle = np.zeros(shape=(2,3)) # Init , lane , distance
# [release, lane]

# Obstacle timing

obstacle_burst = 10 #Recalc time after initial range (3o frames after last obstacle)

def make_burst(min, max, size):
    objects = np.zeros(shape=(size, 3), dtype=object)
    for x in range(size):
        timing = rand.randint(min, max)
        position = rand.randint(0, 3)
        objects[x, 0], objects[x, 1], objects[x, 2] = "obstacle", timing, position
    return objects

def make_field(min, max):
    obstacles = make_burst(min, max, 3)
    return obstacles

def make_track(min, max):
    obstacles = make_field(min, max)
    powers = make_field(min, max)
    track = np.zeros(shape=(3, 3), dtype=object)
    
    # Copy obstacle information to the track
    for i in range(3):
        track[i, 0] = obstacles[i]

    # Copy power information to the track
    for i in range(3):
        track[i, 1] = powers[i]

    return track

def generate_track(min, max):
    track = make_track(min, max)
    objects = np.zeros(shape=(3, 3), dtype=object)

    # Fill the first column with "object"
    objects[:, 0] = "object"

    # Copy lanes from make_burst to the second column
    objects[:, 1] = track[:, 1, 1:]

    # Copy lanes to the last column
    objects[:, 2] = track[:, 0, 2]

    return objects


def drive(car_distance, car_lane, track):
    # Increment car_distance by 1
    car_distance += 1

    make_obstacle_appear(car_distance, track)
    # Check if there is an object at the new position
    for i in range(len(track)):
        if track[i, 0] == "obstacle" and track[i, 1] == car_distance+800 and track[i, 2] == car_lane:
           return 1 # Crash (KHANIJ)

def make_obstacle_appear(car_distance, track):
     for i in range(len(track)):
        if track[i, 0] == "obstacle" and track[i, 1] == car_distance:
           return 1 #MAKE IMAGE (KHANIJ)
            

# Main game loop
while True:
    # Ranges for release
    timer = 0
    ramp = 1.04**(-0.1*timer-135)
    min_release = 120 + ramp
    max_release = 200 + ramp


    # Clear the screen with a black background
    screen.fill(black)

    # Draw a white rectangle

    '''pygame.draw.rect(screen, white, (car_x, car_y, car_width, car_height))

    pygame.draw.rect(screen, yellow, (0, 150, 800, 5))
    pygame.draw.rect(screen, yellow, (0, 300, 800, 5))
    pygame.draw.rect(screen, yellow, (0, 450, 800, 5))'''

    if car_distance == 300:
        game_state = generate_track(min_release,max_release)
        car_distance = 0
    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)