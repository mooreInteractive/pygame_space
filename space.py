#! usr/bin/env python
import pygame
import math
import random
import Ship
import Bullet
import Enemy
import Messages
import Bg
import Menu
import Loot

pygame.init()
screen = pygame.display.set_mode((768, 432))
#gamestates = 'menu', 'play'
gamestate = 'menu'
done = False
Clock = pygame.time.Clock()
bullets = [] 
enemies = []
loot = []
waveCount = 1
pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
block = Ship.ship(bullets, list([]))
mainMenu = Menu.mainMenu(block);
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
    global gamestate
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
                    print 'Drop Loot'
                    #print 'Enemy destroyed!'
                    break
        else:
            #Check for Enemy bullets hitting the Player
            thisBull = pygame.Rect(b.x, b.y, b.w, b.h)
            player = pygame.Rect(block.x, block.y, block.w, block.h)
            phullCount = 0
            pbrokeHull = False
            for h in block.hull[:]:
                #print hullCount
                phullCount += 1
                thisHull = pygame.Rect(h.x, h.y, h.w, h.h)
                if thisBull.colliderect(thisHull) and h.isAttached:
                    bullets.remove(b)
                    h.isAttached = False
                    #print b
                    #e.hull.remove(h)
                    pbrokeHull = True
                    #print 'Hull Destroyed!'
                    break
            if pbrokeHull == True:
                break
            if thisBull.colliderect(player):
                bullets.remove(b)
                block.hp -= 10
                #print 'Ship HP: ' + str(block.hp)
                if block.hp == 0:
                    gamestate = 'menu'
                    block.hp = 100
                    block.color = (0, 128, 255)


    #Enemies hit Player(block)
    for n in enemies[:]:
        thisEne = pygame.Rect(n.x, n.y, n.w, n.h)
        player = pygame.Rect(block.x, block.y, block.w, block.h)
        if player.colliderect(thisEne):
            block.hp -= 10
            if block.hp == 0:
                gamestate = 'menu'
            enemies.remove(n)
            
    #Loot hit Player(block)
    for l in loot[:]:
        player = pygame.Rect(block.x, block.y, block.w, block.h)
        if player.colliderect(l.rect):
            mainMenu.playerInv.insert(0, l.inv)
            loot.remove(l)

def initGame():
    global gamestate, waveCount, enemies, bullets, mainMenu
    block.__init__(bullets, mainMenu.equippedInv)
    waveCount = 1
    del enemies[:]
    del bullets[:]
    gamestate = 'play'

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
    for l in loot:
        l.updateThis()
    detectCollisions()

def drawScreen():
    screen.fill((0, 0, 0))
    bg.drawThis(screen)
    block.drawThis(screen)
    for b in bullets:
        b.drawThis(screen)
    for e in enemies:
        e.drawThis(screen)
    for l in loot:
        l.drawThis(screen)
    messageBox.drawText(screen, block)

#Main Game Loop
while not done:
    if gamestate == 'play':
        getUserInput()
        updateGameObjects()
        drawScreen()
    if gamestate == 'menu':
        events = pygame.event.get()
        mainMenu.getUserInput(initGame, done, events)
        mainMenu.updateMenuScreen(block)
        mainMenu.drawMenuScreen(bg, screen, block)
        if mainMenu.endProgram == True:
            done = True
    pygame.display.flip()
    Clock.tick(60)
        