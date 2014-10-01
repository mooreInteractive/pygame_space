import pygame
import math

class loot:
    type = 'hull'
    x = 0
    y = 0
    w = 8
    h = 8
    rect = pygame.Rect(x, y, w, h)
    speed = 1
    inv = ['hull',8,8,1,pygame.Rect(0,0,50,50)]
    
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
    
    def updateThis(self):
        self.x -= self.speed
        
    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        