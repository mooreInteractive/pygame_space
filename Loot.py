import pygame
import math

class loot:
    type = 'hull'
    rect = pygame.Rect(0,0,1,1)
    color = (24, 215, 56)
    speed = 1
    inv = ['hull',8,8,1,pygame.Rect(0,0,50,50)]
    
    def __init__(self, type, hullRect):
        self.type = type
        self.rect = hullRect

    
    def updateThis(self):
        self.rect.x -= self.speed
        
    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        