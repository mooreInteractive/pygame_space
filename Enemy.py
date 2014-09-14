import pygame
import math
import random
import Hull

class enemy:
    x = 768
    y = 0
    yInit = 0
    w = 25
    h = 10
    speed = 0
    payout = 0
    enType = ''
    color = (255, 30, 245)
    hull = []
    _bullets = []
    _enemies = []

    def __init__(self, pType, pSpeed, bulletsArr, enemiesArr):
        self._bullets = bulletsArr
        self._enemies = enemiesArr
        self.y = random.randint(0, (432-(self.h*1.5)))
        self.x = random.randint(768, 900)
        self.yInit = self.y
        self.enType = pType
        self.speed = pSpeed

        self.hull = []
        #print len(self.hull)
        if self.enType == 'grunt':
            self.hull.append(Hull.hull(8, 8, -4, -4, False, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, -4, 6, False, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, 7, -4, False, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, 7, 6, False, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, 18, -4, False, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, 18, 6, False, 250, self._bullets))

            self.payout = 3

        elif self.enType == 'siner':
            self.hull.append(Hull.hull(8, 8, -4, -4, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -4, 6, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -24, -4, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -14, 1, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -34, 1, True, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -14, -9, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -14, 11, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, 7, -4, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, 7, 6, False, random.randint(75, 200), self._bullets))

            self.payout = 10

        elif self.enType == 'fighter':
            self.hull.append(Hull.hull(8, 8, -14, 1, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -4, -4, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -4, 6, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 7, -4, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 7, 6, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, 18, -14, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, 18, 6, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(12, 8, 14, -24, True, 250, self._bullets))
            self.hull.append(Hull.hull(12, 8, 14, 26, True, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, 28, 1, False, 250, self._bullets))

            self.payout = 8



        self._enemies.insert(0, self)
        #print 'Enemy #'+str(enemies.index(self))+' has '+str(len(self.hull))+' hull pieces.'


    def updateThis(self):
        for h in self.hull:
            h.updateThis(self.x, self.y)
            if h.deadtimer == 0:
                self.hull.remove(h)
            if h.isGun and h.isAttached:
                if self.y <= self.yInit + 0.01:
                    h.fire();
                if self.y >= self.yInit + 49.99:
                    h.fire();        
        if self.enType == 'grunt':
            self.x -= self.speed
        if self.enType == 'siner':
            self.x -= self.speed
            self.y = (25 * math.sin(self.x * 0.5 * math.pi / 60)) + (25+self.yInit)
        if self.enType == 'fighter':
            self.x -= self.speed
            self.y = (25 * math.sin(self.x * 0.5 * math.pi / 60)) + (25+self.yInit)
        if self.x < 0-self.w:
            self._enemies.remove(self)

    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))
        for h in self.hull:
            h.drawThis(screen)