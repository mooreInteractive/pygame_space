#! usr/bin/env python
import pygame
import math
import Ship
import Bullet
import Enemy
import Messages

pygame.init()
screen = pygame.display.set_mode((768, 432))
done = False
Clock = pygame.time.Clock()
bullets = [] 
enemies = []
waveCount = 1
pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
block = Ship.ship(bullets)
messageBox = Messages.messages()




def wave():
    global waveCount
    numEn = int(math.ceil(waveCount/3)) + 1
    for x in range(0, numEn):
        e = Enemy.enemy('grunt', 3, bullets, enemies)
        if x > 1:
            f = Enemy.enemy('siner', 2, bullets, enemies)
        if x > 3:
            g = Enemy.enemy('fighter', random.randint(4, 5), bullets, enemies)
    waveCount += 1

def detectCollisions():
    #colliders
    #Bullets hit Enemies
    for b in bullets[:]:
        if b.badBullet == False:
            for e in enemies[:]:
                thisBull = pygame.Rect(b.x, b.y, b.w, b.h)
                thisEn = pygame.Rect(e.x, e.y, e.w, e.h)
                #print len(e.hull)
                hullCount = 0
                brokeHull = False
                for h in e.hull[:]:
                    #print hullCount
                    hullCount += 1
                    thisHull = pygame.Rect(h.x, h.y, h.w, h.h)
                    if thisBull.colliderect(thisHull):
                        bullets.remove(b)
                        #print b
                        e.hull.remove(h)
                        brokeHull = True
                        #print 'Hull Destroyed!'
                        break
                if brokeHull == True:
                    break
                if thisBull.colliderect(thisEn):
                    block.ammo += e.payout
                    enemies.remove(e)
                    bullets.remove(b)
                    #print 'Enemy destroyed!'
                    break
        else:
            #Check for Enemy bullets hitting the Player
            thisBull = pygame.Rect(b.x, b.y, b.w, b.h)
            player = pygame.Rect(block.x, block.y, block.w, block.h)
            if thisBull.colliderect(player):
                bullets.remove(b)
                block.hp -= 10
                if block.hp == 0:
                    quit()


    #Enemies hit Player(block)
    for n in enemies[:]:
        thisEne = pygame.Rect(n.x, n.y, n.w, n.h)
        player = pygame.Rect(block.x, block.y, block.w, block.h)
        if player.colliderect(thisEne):
            block.hp -= 10
            if block.hp == 0:
                quit()
                #Add Game Over Screen?
            enemies.remove(n)
            print 'Ship HP: ' + str(block.hp)
            #print 'Ship color: ' + str(block.color)


#Main Game Loop
while not done:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #if event.type == pygame.USEREVENT + 1:
                #wave()
                #print 'wave(derp)'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s: block.switchSpeed()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f: block.switchFiringRate()
        pressed = pygame.key.get_pressed()
        if len(enemies) == 0:
            wave()
        if pressed[pygame.K_UP]: block.y -= block.speed
        if pressed[pygame.K_DOWN]: block.y += block.speed
        if pressed[pygame.K_SPACE]:
            block.fire()
        else:
            block.fireCount = 0
        block.updateThis()
        block.drawThis(screen)
        for b in bullets:
            b.updateThis()
            b.drawThis(screen)
        for e in enemies:
            e.updateThis()
            e.drawThis(screen)
        detectCollisions()
        messageBox.drawText(screen, block) 
        
        pygame.display.flip()
        Clock.tick(60)
        