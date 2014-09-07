#! usr/bin/env python
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((768, 432))
done = False
Clock = pygame.time.Clock()
bullets = [] 
enemies = []
waveCount = 1
pygame.time.set_timer(pygame.USEREVENT + 1, 3000)


class Ship:
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
            b = bullet()
            b.y = self.y + (self.h/2)
            bullets.insert(0, b)
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
            
block = Ship()
            
class bullet:
    w = 6
    h = 2
    x = block.x + block.w + 2
    y = block.y + (block.h/2)
    color = (255, 255, 255)
    speed = 6
    
    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))

    def updateThis(self):
        self.x += self.speed
        if self.x > 768:
            bullets.remove(self)
            #print len(bullets)           


class messages:
    basicfont = pygame.font.SysFont(None, 22)
        
    speedText = 'Speed: ' + str(block.speed)
    rateText = 'Fire Rate: ' + str(block.firingRate)
    ammoText = 'Ammo: ' + str(block.ammo)
      
    speedLabel = basicfont.render(speedText, True, (255, 255, 255), (0, 0, 0))
    rateLabel = basicfont.render(rateText, True, (255, 255, 255), (0, 0, 0))
    ammoLabel = basicfont.render(ammoText, True, (255, 255, 255), (0, 0, 0))
                
    speedRect = speedLabel.get_rect()
    rateRect = rateLabel.get_rect()
    ammoRect = ammoLabel.get_rect()
        
    speedRect.x = 650
    speedRect.y = 15
       
    rateRect.x = 650
    rateRect.y = 40
        
    ammoRect.x = 650
    ammoRect.y = 65
       
    def drawText(self, screen):
        self.speedText = 'Speed: ' + str(block.speed)
        self.rateText = 'Fire Rate: ' + str(block.firingRate)
        self.ammoText = 'Ammo: ' + str(block.ammo)
        
        self.speedLabel = self.basicfont.render(self.speedText, True, (255, 255, 255), (0, 0, 0))
        self.rateLabel = self.basicfont.render(self.rateText, True, (255, 255, 255), (0, 0, 0))
        self.ammoLabel = self.basicfont.render(self.ammoText, True, (255, 255, 255), (0, 0, 0))
        
        screen.blit(self.speedLabel, self.speedRect)
        screen.blit(self.rateLabel, self.rateRect)
        screen.blit(self.ammoLabel, self.ammoRect)

messageBox = messages()

class Hull:
    x = 0
    y = 0
    w = 0
    h = 0
    xmod = 0
    ymod = 0
    color = (255, 255, 255)

    def __init__(self, w, h, xmod, ymod, host):
        self.w = w
        self.h = h
        self.xmod = xmod
        self.ymod = ymod
        self.host = host
        self.x = self.host.x+self.xmod
        self.y = self.host.y+self.ymod

    def updateThis(self):
        self.x = self.host.x+self.xmod
        self.y = self.host.y+self.ymod

    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))


class enemy:
    x = 768
    y = 0
    yInit = 0
    w = 25
    h = 10
    speed = 0
    enType = ''
    color = (255, 30, 245)
    hull = []

    def __init__(self, pType, pSpeed):
        self.y = random.randint(0, (432-self.h))
        self.x = random.randint(768, 900)
        self.yInit = self.y
        enemies.insert(0, self)
        self.enType = pType
        self.speed = pSpeed

        self.hull.insert(0, Hull(8, 8, -4, -4, self))
        self.hull.insert(0, Hull(8, 8, -4, 6, self))
        self.hull.insert(0, Hull(8, 8, 7, -4, self))
        self.hull.insert(0, Hull(8, 8, 7, 6, self))
        self.hull.insert(0, Hull(8, 8, 18, -4, self))
        self.hull.insert(0, Hull(8, 8, 18, 6, self))

    def updateThis(self):
        for h in self.hull:
            h.updateThis()
        if self.enType == 'grunt':
            self.x -= self.speed
            self.y = (25 * math.sin(self.x * 0.5 * math.pi / 30)) + (25+self.yInit)
        if self.x < 0-self.w:
            for i in self.hull:
                    del i
            enemies.remove(self)

    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))
        for h in self.hull:
            h.drawThis(screen)

def wave():
    global waveCount
    numEn = int(math.ceil(waveCount/10)) + 2
    for x in range(0, numEn):
        e = enemy('grunt', 2)
    waveCount += 1

def detectCollisions():
    #colliders
    #Bullets hit Enemies
    for b in bullets:
        for e in enemies:
            thisBull = pygame.Rect(b.x, b.y, b.w, b.h)
            thisEn = pygame.Rect(e.x, e.y, e.w, e.h)
            if thisBull.colliderect(thisEn):
                for h in range(0, len(e.hull)-1):
                    del e.hull[h]
                    h -=1
                    continue
                    #break
                enemies.remove(e)
                bullets.remove(b)
                block.ammo += 3
                print 'Enemy destroyed!'
                break
    #Enemies hit Player(block)
    for n in enemies:
        thisEne = pygame.Rect(n.x, n.y, n.w, n.h)
        player = pygame.Rect(block.x, block.y, block.w, block.h)
        if player.colliderect(thisEne):
            block.hp -= 10
            if block.hp == 0:
                quit()
                #Add Game Over Screen?
            for h in range(0, len(n.hull)-1):
                del n.hull[h]
                #break
            enemies.remove(n)
            print 'Ship HP: ' + str(block.hp)
            print 'Ship color: ' + str(block.color)
            break


#Main Game Loop
while not done:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.USEREVENT + 1:
                wave()
                #print 'wave(derp)'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s: block.switchSpeed()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f: block.switchFiringRate()
        pressed = pygame.key.get_pressed()
		
        if pressed[pygame.K_UP]: block.y -= block.speed
        if pressed[pygame.K_DOWN]: block.y += block.speed
        if pressed[pygame.K_SPACE]:
            block.fire()
        else:
            block.fireCount = 0
        block.updateThis()
        block.drawThis(screen)
        for b in list(bullets):
            b.updateThis()
            b.drawThis(screen)
        for e in list(enemies):
            e.updateThis()
            e.drawThis(screen)
        detectCollisions()
        messageBox.drawText(screen) 
        
        pygame.display.flip()
        Clock.tick(60)
        