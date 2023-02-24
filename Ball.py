import pygame
from pygame.locals import *
import random

class Ball():
    def __init__(self,window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('images/ball.png')
        #ignore the one line code below, I just added it to make the ball small
        self.image = pygame.transform.scale(self.image,(40,40))
        # a rectangle is made up of [x,y,width,height]
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth-self.width
        self.maxHeight = windowHeight-self.height

        #pick a randome starting position
        self.x = random.randrange(0,self.maxWidth)
        self.y = random.randrange(0,self.maxHeight)
        #
        speedList = [-4,-3,-2,-1,1,2,3,4]
        self.xSpeed = random.choice(speedList)
        self.ySpeed = random.choice(speedList)

    def update(self):
        #check for hitting the wall, if so then change the direction
        if self.x <0 or self.x >= self.maxWidth:
            self.xSpeed = - self.xSpeed
        if self.y < 0  or self.y >= self.maxHeight:
            self.ySpeed = - self.ySpeed
        
        #update the ball x and y direction using these speed
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed
    
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))
    



