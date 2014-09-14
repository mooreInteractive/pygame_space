import pygame
import Bullet

class hull:
    x = 0
    y = 0
    w = 0
    h = 0
    xmod = 0
    ymod = 0
    grey = 255
    color = (grey, grey, grey)
    isGun = False
    gunColor = (200, 50, 50)
    _bullets = []

    def __init__(self, w, h, xmod, ymod, gun, grey, bulletsArr):
        self._bullets = bulletsArr
        self.w = w
        self.h = h
        self.xmod = xmod
        self.ymod = ymod
        self.isGun = gun
        self.grey = grey
        self.color = (self.grey, self.grey, self.grey)

    def updateThis(self, hostx, hosty):
        self.x = hostx+self.xmod
        self.y = hosty+self.ymod

    def fire(self):
        b = Bullet.bullet(True, self._bullets)
        b.y = self.y + (self.h/2)
        b.x = self.x - (self.w/2)
        self._bullets.insert(0, b)

    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))
        if self.isGun:
            pygame.draw.line(screen, self.gunColor, (self.x+(self.h/2), (self.y-1)+(self.h/2)), (self.x-(self.w/2), (self.y-1)+(self.h/2)), 2)

