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
    bossYCount = 0

    def __init__(self, pType, pSpeed, bulletsArr, enemiesArr, sety=0):
        self._bullets = bulletsArr
        self._enemies = enemiesArr
        self.enType = pType
        if self.enType == 'grunt-siner-wave':
            self.y = sety
            self.x = 775
        elif self.enType == 'boss':
            self.y = 200
            self.x = 775
        else:
            self.y = random.randint(0, (432-(self.h*1.5)))
            self.x = random.randint(768, 900)
        self.yInit = self.y
        self.speed = pSpeed

        self.hull = []
        #print len(self.hull)
        if self.enType == 'grunt' or self.enType == 'grunt-siner-wave':
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

        elif self.enType == 'boss':

            #column -9
            self.hull.append(Hull.hull(8, 8, -88, -44, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -88, -34, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -88, -24, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -88, -14, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -88, -4, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -88, 6, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -88, 16, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -88, 26, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -88, 36, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -88, 46, False, random.randint(75, 200), self._bullets))

            #column -8
            self.hull.append(Hull.hull(8, 18, -78, -64, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -78, -44, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -78, -24, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -78, -4, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -78, 16, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -78, 36, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -78, 56, False, random.randint(75, 200), self._bullets))

            #column -7
            self.hull.append(Hull.hull(8, 8, -68, -68, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -68, -48, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -68, -38, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -68, -18, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -68, 22, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -68, 42, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -68, 52, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -68, 72, False, random.randint(75, 200), self._bullets))

            #column -6
            self.hull.append(Hull.hull(12, 8, -62, -78, True, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, -58, -68, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -58, -48, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -58, -38, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -58, -18, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(12, 8, -62, -8, True, 250, self._bullets))
            self.hull.append(Hull.hull(12, 8, -62, 12, True, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, -58, 22, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -58, 42, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -58, 52, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -58, 72, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(12, 8, -62, 82, True, 250, self._bullets))

            #column -5
            self.hull.append(Hull.hull(8, 18, -48, -83, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -48, -63, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -48, -43, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -48, -23, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -48, -3, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -48, 17, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -48, 37, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -48, 57, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -48, 77, False, random.randint(75, 200), self._bullets))

            #column -4
            self.hull.append(Hull.hull(8, 8, -38, -78, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, -68, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, -48, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, -38, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, -18, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, -8, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, 12, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, 22, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, 42, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, 52, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, 72, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -38, 82, False, random.randint(75, 200), self._bullets))

            #column -3
            self.hull.append(Hull.hull(18, 8, -38, -88, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, -78, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, -68, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -38, -58, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, -48, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, -38, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -38, -28, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, -18, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, -8, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -38, 2, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, 12, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, 22, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -38, 32, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, 42, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, 52, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -38, 62, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, 72, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -28, 82, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -38, 92, False, random.randint(75, 200), self._bullets))

            #column -2
            self.hull.append(Hull.hull(8, 18, -18, -103, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, -83, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, -63, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, -43, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, -23, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, -3, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, 17, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, 37, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, 57, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, 77, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 18, -18, 97, False, random.randint(75, 200), self._bullets))

            #column -1
            self.hull.append(Hull.hull(18, 8, -8, -90, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -8, -70, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -8, -50, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -8, -30, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -8, -22, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -8, -14, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(12, 8, -12, -6, True, 250, self._bullets))
            self.hull.append(Hull.hull(12, 8, -12, 2, True, 250, self._bullets))
            self.hull.append(Hull.hull(12, 8, -12, 10, True, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, -8, 18, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -8, 26, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, -8, 34, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -8, 54, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -8, 74, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, -8, 94, False, random.randint(75, 200), self._bullets))

            #column 0
            self.hull.append(Hull.hull(8, 8, 0, -30, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 0, -22, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 0, -14, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 0, -6, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 0, 2, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 0, 10, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 0, 18, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 0, 26, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 0, 34, False, random.randint(75, 200), self._bullets))

            #column 1
            self.hull.append(Hull.hull(12, 8, 8, -90, True, 250, self._bullets))
            self.hull.append(Hull.hull(12, 8, 8, -70, True, 250, self._bullets))
            self.hull.append(Hull.hull(12, 8, 8, -50, True, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, 8, -30, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 8, -22, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(12, 8, 8, -14, True, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, 8, -6, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 8, 2, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 8, 10, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(12, 8, 8, 18, True, 250, self._bullets))
            self.hull.append(Hull.hull(8, 8, 8, 26, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 8, 34, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(12, 8, 8, 54, True, 250, self._bullets))
            self.hull.append(Hull.hull(12, 8, 8, 74, True, 250, self._bullets))
            self.hull.append(Hull.hull(12, 8, 8, 94, True, 250, self._bullets))

            #column 2
            self.hull.append(Hull.hull(18, 8, 20, -14, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 16, -6, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 16, 2, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 16, 10, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(18, 8, 20, 18, False, random.randint(75, 200), self._bullets))

            #column 3
            self.hull.append(Hull.hull(8, 8, 24, -6, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 24, 2, False, random.randint(75, 200), self._bullets))
            self.hull.append(Hull.hull(8, 8, 24, 10, False, random.randint(75, 200), self._bullets))

            self.payout = 50



        self._enemies.insert(0, self)
        #print 'Enemy #'+str(enemies.index(self))+' has '+str(len(self.hull))+' hull pieces.'


    def updateThis(self):
        for h in self.hull:
            h.updateThis(self.x, self.y)
            if h.deadtimer == 0:
                self.hull.remove(h)
            if h.isGun and h.isAttached and self.enType != 'boss':
                if self.y <= self.yInit + 0.01:
                    h.fire()
                if self.y >= self.yInit + 49.99:
                    h.fire()
            elif h.isGun and h.isAttached and self.enType == 'boss':
                if self.bossYCount%25 == 0 and h.x == self.x - 12:
                    h.fire()
                if self.bossYCount%75 == 0 and h.x == self.x + 8:
                    h.fire() 
                if self.bossYCount%150 == 0 and h.x == self.x - 62:
                    h.fire()   
        if self.enType == 'grunt':
            self.x -= self.speed
        if self.enType == 'grunt-siner-wave':
            self.x -= self.speed
            self.y = (150 * math.sin((self.x/4) * 0.5 * math.pi / 120)) + (25+self.yInit)
        if self.enType == 'siner':
            self.x -= self.speed
            self.y = (25 * math.sin(self.x * 0.5 * math.pi / 60)) + (25+self.yInit)
        if self.enType == 'fighter':
            self.x -= self.speed
            self.y = (25 * math.sin(self.x * 0.35 * math.pi / 60)) + (25+self.yInit)
        if self.enType == 'boss':
            self.x -= self.speed
            self.y = (25 * math.sin(self.bossYCount * 0.5 * math.pi / 60)) + (25+self.yInit)
            self.bossYCount += 1
            if self.x < 700:
                self.x = 700
        if self.x < 0-self.w:
            self._enemies.remove(self)

    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))
        for h in self.hull:
            h.drawThis(screen)