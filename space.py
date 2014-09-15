#! usr/bin/env python
import pygame
import math
import random
import Ship
import Bullet
import Enemy
import Messages
import Bg

pygame.init()
screen = pygame.display.set_mode((768, 432))
#gamestates = 'menu', 'play'
gamestate = 'menu'
done = False
Clock = pygame.time.Clock()
bullets = [] 
enemies = []
waveCount = 1
pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
block = Ship.ship(bullets)
messageBox = Messages.messages()
bg = Bg.bg()
bg.img = pygame.image.load("bg.png").convert()

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
                    if thisBull.colliderect(thisHull) and h.isAttached:
                        bullets.remove(b)
                        h.isAttached = False
                        #print b
                        #e.hull.remove(h)
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
                #print 'Ship HP: ' + str(block.hp)
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
            #print 'Ship HP: ' + str(block.hp)
            #print 'Ship color: ' + str(block.color)

def getUserInput():
    global done
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #if event.type == pygame.USEREVENT + 1:
                #wave()
                #print 'wave(derp)'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s: block.switchSpeed()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f: block.switchFiringRate()

    pressed = pygame.key.get_pressed()
    #if pressed[pygame.K_s]: block.switchSpeed()
    #if pressed[pygame.K_f]: block.switchFiringRate()
    if pressed[pygame.K_UP]: block.y -= block.speed
    if pressed[pygame.K_DOWN]: block.y += block.speed
    if pressed[pygame.K_SPACE]:
        block.fire()
    else:
        block.fireCount = 0

def updateGameObjects():
    bg.updateThis()
    if len(enemies) == 0:
            wave()
    block.updateThis()
    for b in bullets:
        b.updateThis()
    for e in enemies:
        e.updateThis()
    detectCollisions()

def drawScreen():
    screen.fill((0, 0, 0))
    bg.drawThis(screen)
    block.drawThis(screen)
    for b in bullets:
        b.drawThis(screen)
    for e in enemies:
        e.drawThis(screen)
    messageBox.drawText(screen, block)

#Main Game Loop
while not done:
    if gamestate == 'play':
        getUserInput()
        updateGameObjects()
        drawScreen()
    if gamestate == 'menu':
        screen.fill((0, 0, 0))
        bg.drawThis(screen)
        playText = 'Press \'S\' to play.'
        basicfont = pygame.font.SysFont(None, 22)
        playLabel = basicfont.render(playText, True, (255, 255, 255), (0, 0, 0))
        playRect = playLabel.get_rect()
        playRect.x = 100
        playRect.y = 200
        screen.blit(playLabel, playRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #if event.type == pygame.USEREVENT + 1:
                #wave()
                #print 'wave(derp)'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s: gamestate = 'play'
    pygame.display.flip()
    Clock.tick(60)
        