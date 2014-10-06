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
    energy = 100
    rechargeRate = 0.1
    energyMax = 100
    defaultEnergy = 100
    defaultRechargeRate = 0.1
    defaultHP = 100
    hpMax = 100
    hp = 100
    hull = []
    inventory = [['hull',8,8,1,pygame.Rect(0,0,50,50)],['hull',8,8,1,pygame.Rect(0,0,50,50)],['gun',12,8,1,pygame.Rect(0,0,50,50)]]
    _bullets = []
	
    def __init__(self, bulletsArr, equipment):
        self._bullets = bulletsArr;

        del self.hull[:]
        
        for eqp in equipment:
            isgun = False
            if eqp[0] == 'gun':
                isgun = True
            
            self.hull.append(Hull.hull(eqp[1],eqp[2],(eqp[4].x - self.x),(eqp[4].y - self.y), isgun, 255, self._bullets))

        self.updateStats()

        self.x = 30;
        self.y = 30;
        
        self.energy = 100
        self.hp = 100

    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))
        for h in self.hull:
            h.drawThis(screen)

    def updateStats(self):
        #update Stats for each item equipped's value
        newRR = self.defaultRechargeRate
        newEC = self.defaultEnergy
        newHP = self.defaultHP
        for h in self.hull:
            if h.isGun == False and h.isAttached == True:
                if h.w == 8 and h.h == 18:
                    newRR += 0.1
                if h.w == 18 and h.h == 18:
                    newEC += 10
                if h.w == 18 and h.h == 8:
                    newHP += 10
        self.rechargeRate = newRR
        self.energyMax = newEC
        self.hpMax = newHP
        #print 'Ship Status - RR: '+str(self.rechargeRate)+', EC: '+str(self.energyMax)+', maxHP:'+str(self.hpMax)

    def updateThis(self):
        for h in self.hull:
            h.updateThis(self.x, self.y)
            if h.deadtimer == 0:
                self.hull.remove(h)
                self.updateStats()
        newRed = int(255 - ((self.hp/float(100)) * 255))
        newBlue = int((self.hp/float(100)) * 255)
        self.color = (newRed, 30, newBlue)
        if self.y < 0: self.y = 0;
        if self.y > (432-self.h): self.y = (432-self.h)
        self.energy += self.rechargeRate
        if self.energy > self.energyMax:
            self.energy = self.energyMax
    
    def fire(self):
        if self.fireCount%(60/self.firingRate) == 0:
            for h in self.hull:
                if h.isGun == True and h.isAttached == True and self.energy > 0:
                    b = Bullet.bullet(False, self._bullets)
                    b.x = h.x + h.w + 2
                    b.y = h.y + (h.h/2)
                    self._bullets.insert(0, b)
                    self.energy -= 1
        
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