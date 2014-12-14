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
import End

pygame.init()
screen = pygame.display.set_mode((768, 432))
#gamestates = 'menu', 'play'
gamestate = 'menu'
done = False
Clock = pygame.time.Clock()
bullets = [] 
enemies = []
loot = []
playCount = 0
waveCount = 1
pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
block = Ship.ship(bullets, list([]))
mainMenu = Menu.mainMenu(block)
messageBox = Messages.messages()
endMessage = End.messages()
bg = Bg.bg()
bg.img = pygame.image.load("bg.png").convert()

waveDone = False
lastSpawn = 0
numSpawned = 0
lastwave = 0
randomGroupY = 50

def wave():
    global waveCount, waveDone, lastSpawn, numSpawned, lastWave, randomGroupY, gamestate
    t = pygame.time.get_ticks()
    #print 'en: ' + str(len(enemies)) + ', wave: ' + str(waveCount) #str(t - lastSpawn) 
    if waveCount < 20:
        if waveCount %2 == 1:
            if not waveDone:
                if (t - lastSpawn) > 200:
                    a = Enemy.enemy('grunt-siner-wave', 3, bullets, enemies, randomGroupY)
                    lastSpawn = pygame.time.get_ticks()
                if len(enemies)%5 == 0 and waveCount > 9:
                    f = Enemy.enemy('siner', 2, bullets, enemies)
                if len(enemies) > 12:
                    waveDone = True
            if (t - lastSpawn) > 5000 and waveDone:
                waveCount += 1
                lastwave = pygame.time.get_ticks()
                waveDone = False
                randomGroupY = random.randint(50, 300)
        else:
            numEn = int(math.ceil(waveCount/3)) + 1
            if not waveDone: 
                for x in range(0, numEn):
                    e = Enemy.enemy('grunt', 3, bullets, enemies)
                    if x > 1:
                        f = Enemy.enemy('siner', 2, bullets, enemies)
                    if x > 3:
                        g = Enemy.enemy('fighter', random.randint(4, 5), bullets, enemies)
                    waveDone = True
            if len(enemies) == 0 and waveDone:
                waveCount += 1
                waveDone = False
    else:
        if not waveDone:
            b = Enemy.enemy('boss', 0.5, bullets, enemies)
            waveDone = True
        if len(enemies) == 0 and waveDone:
            gamestate = 'game over'
            #print 'game should be over now'

    

def dropLoot(x,y):
    global playCount
    if playCount > 0:
        randoBool = random.randint(1,2)
        rando = random.randint(1,6)
        #print 'round '+str(playCount)+' rando = '+str(rando)
        if randoBool == 2:
            if rando == 1:
                loot.insert(0, Loot.loot('hull',pygame.Rect(x, y, 8, 18)))
            elif rando == 2:
                loot.insert(0, Loot.loot('hull',pygame.Rect(x, y, 18, 8)))
            elif rando == 3:
                loot.insert(0, Loot.loot('gun',pygame.Rect(x, y, 12, 8)))
            elif rando == 4:
                loot.insert(0, Loot.loot('hull',pygame.Rect(x, y, 18, 18)))
            elif rando > 4: 
                loot.insert(0, Loot.loot('hull',pygame.Rect(x, y, 8, 8)))
    else:
        rando = random.randint(1,6)
        #print 'round '+str(playCount)+' rando1 = '+str(rando1)
        if rando == 1:
            loot.insert(0, Loot.loot('hull',pygame.Rect(x, y, 8, 18)))
        elif rando == 2:
            loot.insert(0, Loot.loot('hull',pygame.Rect(x, y, 18, 8)))
        elif rando == 3:
            loot.insert(0, Loot.loot('hull',pygame.Rect(x, y, 8, 8)))
        elif rando == 4:
            loot.insert(0, Loot.loot('hull',pygame.Rect(x, y, 18, 18)))
        elif rando > 4: 
            loot.insert(0, Loot.loot('gun',pygame.Rect(x, y, 12, 8)))


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
                    #block.energy += e.payout
                    dropLoot(e.x+(e.w/2), e.y+(e.h/2))
                    enemies.remove(e)
                    bullets.remove(b)
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
                    pbrokeHull = True
                    #removeFromPlayerInventory(h)
                    break
            if pbrokeHull == True:
                break
            if thisBull.colliderect(player):
                bullets.remove(b)
                block.hp -= 10
                #print 'Ship HP: ' + str(block.hp)
                if block.hp <= 0:
                    block.hp = 100
                    block.color = (0, 128, 255)
                    mainMenu.__init__(block)
                    gamestate = 'menu'


    #Enemies hit Player(block)
    for n in enemies[:]:
        thisEne = pygame.Rect(n.x, n.y, n.w, n.h)
        player = pygame.Rect(block.x, block.y, block.w, block.h)
        if player.colliderect(thisEne):
            block.hp -= 10
            if block.hp == 0:
                block.hp = 100
                block.color = (0, 128, 255)
                mainMenu.__init__(block)
                gamestate = 'menu'
            enemies.remove(n)
            break
        for h in block.hull[:]:
                #print hullCount
                thisHull = pygame.Rect(h.x, h.y, h.w, h.h)
                if thisEne.colliderect(thisHull) and h.isAttached:
                    enemies.remove(n)
                    h.isAttached = False
                    pbrokeHull = True
                    #removeFromPlayerInventory(h)
                    break
            
    #Loot hit Player(block)
    for l in loot[:]:
        player = pygame.Rect(block.x, block.y, block.w, block.h)
        if player.colliderect(l.rect):
            block.inventory.insert(0, l.inv)
            loot.remove(l)
            break

def initGame():
    global gamestate, waveCount, enemies, bullets, mainMenu, playCount
    block.__init__(bullets, mainMenu.equippedInv)
    waveCount = 1
    waveDone = False
    del enemies[:]
    del bullets[:]
    del block.inventory[:]
    playCount += 1
    gamestate = 'play'

def getUserInput():
    global done
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s: block.switchSpeed()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f: block.switchFiringRate()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if block.energy > 0:
            block.y -= block.speed
            block.energy -= (block.speed - 2)/2
    if pressed[pygame.K_DOWN]:
        if block.energy > 0: 
            block.y += block.speed
            block.energy -= (block.speed - 2)/2
    if pressed[pygame.K_SPACE]:
        block.fire()
    else:
        block.fireCount = 0

def getEndInput():
    global done
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

def updateGameObjects():
    bg.updateThis()
    #if len(enemies) == 0:
    wave()
    block.updateThis()
    for b in bullets:
        b.updateThis()
    for e in enemies:
        e.updateThis()
    for l in loot:
        l.updateThis()
        if l.rect.x < (0-l.rect.w):
            loot.remove(l)
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

def drawEndScreen():
    screen.fill((0,0,0))
    bg.drawThis(screen)
    block.drawThis(screen)
    endMessage.drawText(screen, block)

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
    if gamestate == 'game over':
        getEndInput()
        drawEndScreen()
    pygame.display.flip()
    Clock.tick(60)
        