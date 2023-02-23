
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
import random

#Define contants
#Colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

BALL_WIDTH_HEIGHT = 60
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3
#3 Initialize the world

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 -> Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.png')
ballImageSmall = pygame.transform.scale(ballImage,(BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT))
targetImageSmall = pygame.transform.scale(targetImage,(TARGET_WIDTH_HEIGHT,TARGET_WIDTH_HEIGHT))
#5 -Initialize variables
ballx = random.randrange(MAX_WIDTH)
bally = random.randrange(MAX_HEIGHT)
#ballRect = pygame.Rect(ballx,bally,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)
targetRect = pygame.Rect(TARGET_X,TARGET_Y, TARGET_WIDTH_HEIGHT,TARGET_WIDTH_HEIGHT)
#6-LoopForever
while True:
    #7 check for and handle events
    for event in pygame.event.get():
        #clicked the close button ? Quit the pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #see if user clicked
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballx -= N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballx += N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                bally -= N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                bally += N_PIXELS_TO_MOVE
    #8 do any "per frame" actions
    ballRect = pygame.Rect(ballx,bally, BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)
    
    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')
    #9 clear the window

    window.fill(WHITE)

    #10 Draw all window elements
    window.blit(targetImageSmall,(TARGET_X,TARGET_Y))
    window.blit(ballImageSmall,(ballx,bally)) #bit block transfer, just means draw
    #11 update the window
    pygame.display.update()
    #12 
    #show things down a bit
    clock.tick(FRAMES_PER_SECOND)

