import pygame
import Bullet
import random

class hull:
    x = 0
    y = 0
    w = 0
    h = 0
    xmod = 0
    ymod = 0
    deadx = 1
    deady = -1
    grey = 255
    color = (grey, grey, grey)
    isGun = False
    gunColor = (200, 50, 50)
    _bullets = []
    deadtimer = 30
    isAttached = True

    def __init__(self, w, h, xmod, ymod, gun, grey, bulletsArr):
        self._bullets = bulletsArr
        self.w = w
        self.h = h
        self.xmod = xmod
        self.ymod = ymod
        self.isGun = gun
        self.grey = grey
        self.color = (self.grey, self.grey, self.grey)
        if self.grey == 255:
            self.deadx = random.randint(-4, 0)
            self.deady = random.randint(-3, 3)
        else:
            self.deadx = random.randint(0, 4)
            self.deady = random.randint(-3, 3)

    def updateThis(self, hostx, hosty):
        if self.isAttached:
            self.x = hostx+self.xmod
            self.y = hosty+self.ymod
        else:
            self.x += self.deadx
            self.y += self.deady
            self.deadtimer -= 1


    def fire(self):
        b = Bullet.bullet(True, self._bullets)
        b.y = self.y + (self.h/2)
        b.x = self.x - (self.w/2)
        self._bullets.insert(0, b)

    def drawThis(self, screen):
        
        if self.isAttached:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))
            if self.isGun:  
                if self.grey == 255:
                    pygame.draw.line(screen, self.gunColor, (self.x+(self.w/2), (self.y-1)+(self.h/2)), (self.x+(self.w), (self.y-1)+(self.h/2)), 2)
                else: 
                    pygame.draw.line(screen, self.gunColor, (self.x+(self.w/2), (self.y-1)+(self.h/2)), (self.x-(self.w/2), (self.y-1)+(self.h/2)), 2)

        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h), self.deadtimer%5)






