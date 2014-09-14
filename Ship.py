import pygame
import Bullet

class ship:
    color = (0, 128, 255)
    w = 45
    h = 20
    x = 30
    y = 30
    speed = 2
    firingRate = 2
    fireCount = 0
    firing = False
    ammo = 100
    hp = 100
    hull = []
    _bullets = []
	
    def __init__(self, bulletsArr):
        self._bullets = bulletsArr;

    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))

    def updateThis(self):
        newRed = int(255 - ((self.hp/float(100)) * 255))
        newBlue = int((self.hp/float(100)) * 255)
        self.color = (newRed, 30, newBlue)
        if self.y < 0: self.y = 0;
        if self.y > (432-self.h): self.y = (432-self.h)
    
    def fire(self):
        if self.fireCount%(60/self.firingRate) == 0 and self.ammo > 0:
            b = Bullet.bullet(False, self._bullets)
            b.x = self.x + self.w + 2
            b.y = self.y + (self.h/2)
            self._bullets.insert(0, b)
            self.ammo -= 1
        
        self.fireCount += 1
        #print self.fireCount
        if self.fireCount >= 61:
            self.fireCount = 1
    
    def switchFiringRate(self):
        if self.firingRate == 2:
            self.firingRate = 4
        elif self.firingRate == 4:
            self.firingRate = 10
        elif self.firingRate == 10:
            self.firingRate = 2        
            
    def switchSpeed(self):
        if self.speed == 2:
            self.speed = 4
        elif self.speed == 4:
            self.speed = 8
        elif self.speed == 8:
            self.speed = 2