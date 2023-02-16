
"""
This project illustrates following in procedural way
1. Bringing up a blank window
2. Show an image
3. Detect a mouse click
4. Detect both single and continuous key presses
5. Create a simple animation
6. play sound effects and background sounds
7.Draw shapes

"""

#import packages
import pygame
import sys

#Define contants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

#3 Initialize the world

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 -> Load assets: image(s), sound(s), etc.

#5 -Initialize variables

#6-LoopForever

