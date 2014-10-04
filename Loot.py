import pygame
import math

class loot:
    ltype = 'hull'
    rect = pygame.Rect(0,0,1,1)
    color = (24, 215, 56)
    speed = 1
    inv = []
    
    def __init__(self, typeLoot, hullRect):
        self.ltype = typeLoot
        self.rect = hullRect
        self.inv = [typeLoot,hullRect.w,hullRect.h,1,pygame.Rect(0,0,50,50)]

    
    def updateThis(self):
        self.rect.x -= self.speed
        
    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        