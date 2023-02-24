
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
from Ball import Ball

#Define contants
#Colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
N_BALLS = 5
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


#3 Initialize the world

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 -> Load assets: image(s), sound(s), etc.
#ballImageSmall = pygame.transform.scale(ballImage,(BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT))
#5 -Initialize variables
listOfBalls = []
for i in range(0,N_BALLS):
    listOfBalls.append(Ball(window,WINDOW_WIDTH,WINDOW_HEIGHT))
# oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
# oBall2 = Ball(window,WINDOW_WIDTH,WINDOW_HEIGHT)
# oBall3 = Ball(window,WINDOW_WIDTH,WINDOW_HEIGHT)
#ballRect = pygame.Rect(ballx,bally,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)
#
#6-LoopForever
while True:
    #7 check for and handle events
    for event in pygame.event.get():
        #clicked the close button ? Quit the pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #8 do any "per frame" actions
    for i in range(0,N_BALLS):
        listOfBalls[i].update()
    # oBall.update()   
    # oBall2.update()
    # oBall3.update()
    #9 clear the window

    window.fill(WHITE)

    #10 Draw all window elements
    for i in range(0,N_BALLS):
        listOfBalls[i].draw()
    # oBall.draw()
    # oBall2.draw()
    # oBall3.draw()
    #11 update the window
    pygame.display.update()
    #12 
    #show things down a bit
    clock.tick(FRAMES_PER_SECOND)

