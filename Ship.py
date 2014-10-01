import pygame
import Bullet
import Hull

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
    inventory = [['hull',8,8,100,100],['hull',8,8,100,100],['gun',12,8,100,100]]
    _bullets = []
	
    def __init__(self, bulletsArr, equipment):
        self._bullets = bulletsArr;

        del self.hull[:]
        
        for eqp in equipment:
            isgun = False
            if eqp[0] == 'gun':
                isgun = True
            
            self.hull.append(Hull.hull(eqp[1],eqp[2],(eqp[4].x - self.x),(eqp[4].y - self.y), isgun, 255, self._bullets))
        
        #self.hull.append(Hull.hull(8, 8, 41, -4, False, 255, self._bullets))
        #self.hull.append(Hull.hull(8, 8, 31, -4, False, 255, self._bullets))
        #self.hull.append(Hull.hull(8, 8, 41, 6, False, 255, self._bullets))
        #self.hull.append(Hull.hull(8, 8, 41, 16, False, 255, self._bullets))
        #self.hull.append(Hull.hull(8, 8, 31, 16, False, 255, self._bullets))
        #self.hull.append(Hull.hull(8, 8, 51, 1, False, 255, self._bullets))
        #self.hull.append(Hull.hull(8, 8, 51, 11, False, 255, self._bullets))

        #self.hull.append(Hull.hull(12, 8, 61, 1, True, 255, self._bullets))
        #self.hull.append(Hull.hull(12, 8, 61, 11, True, 255, self._bullets))

        self.x = 30;
        self.y = 30;
        
        self.ammo = 100
        self.hp = 100

    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))
        for h in self.hull:
            h.drawThis(screen)

    def updateThis(self):
        for h in self.hull:
            h.updateThis(self.x, self.y)
            if h.deadtimer == 0:
                self.hull.remove(h)
        newRed = int(255 - ((self.hp/float(100)) * 255))
        newBlue = int((self.hp/float(100)) * 255)
        self.color = (newRed, 30, newBlue)
        if self.y < 0: self.y = 0;
        if self.y > (432-self.h): self.y = (432-self.h)
    
    def fire(self):
        if self.fireCount%(60/self.firingRate) == 0:
            for h in self.hull:
                if h.isGun == True and h.isAttached == True and self.ammo > 0:
                    b = Bullet.bullet(False, self._bullets)
                    b.x = h.x + h.w + 2
                    b.y = h.y + (h.h/2)
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