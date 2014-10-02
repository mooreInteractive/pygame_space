import pygame
import math

class mainMenu:

    endProgram = False
    startGame = False
    gridRect = pygame.Rect(452,116, 200, 200)
    mousePos = (0,0)
    playerInv = []
    equippedInv = []
    dragging = False
    draggedItem = []

    playText = 'Press \'S\' to play.'
    titleText = 'Pygame_Space'
    inventoryText = 'Inventory'
    configText = 'Ship Configuration'
    largefont = pygame.font.SysFont(None, 28)
    basicfont = pygame.font.SysFont(None, 22)
    smallfont = pygame.font.SysFont(None, 18)
    playLabel = basicfont.render(playText, True, (255, 255, 255), (0, 0, 0))
    playRect = playLabel.get_rect()
    playRect.x = 515
    playRect.y = 360

    titleLabel = largefont.render(titleText, True, (255, 255, 255), (0, 0, 0))
    titleRect = titleLabel.get_rect()
    titleRect.x = 305
    titleRect.y = 15

    inventoryLabel = basicfont.render(inventoryText, True, (255, 255, 255), (0, 0, 0))
    inventoryRect = inventoryLabel.get_rect()
    inventoryRect.x = 80
    inventoryRect.y = 95

    configLabel = basicfont.render(configText, True, (255, 255, 255), (0, 0, 0))
    configRect = configLabel.get_rect()
    configRect.x = 452
    configRect.y = 95

    def __init__(self, player):
        newinv = []
        del self.equippedInv[:]
        del player.hull[:]
        for item in player.inventory:
            if len(newinv) == 0:
                newinv.insert(0,[item[0],item[1],item[2], 1, pygame.Rect(0,0,50,50)])
            else:
                isdupe = False
                for _item in newinv:
                    if item[0] == _item[0] and item[1] == _item[1] and item[2] == _item[2]:
                        _item[3] += 1
                        isdupe = True
                if isdupe == False:
                    newinv.insert(0,[item[0],item[1],item[2], 1, pygame.Rect(0,0,50,50)])

        self.playerInv = newinv
    def getUserInput(self, initGame, done, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.endProgram = True

            if event.type == pygame.MOUSEMOTION:
                self.mousePos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if self.dragging:
                    if self.gridRect.collidepoint(self.mousePos):
                        self.draggedItem[4].x = math.floor((self.mousePos[0] - (self.draggedItem[1]/2)) + 0.5)
                        self.draggedItem[4].y = math.floor((self.mousePos[1] - (self.draggedItem[2]/2))+ 0.5)
                        self.equippedInv.insert(0, self.draggedItem)
                    else:
                        inInv = False
                        for _inv in self.playerInv:
                            if _inv[0] == self.draggedItem[0]:
                                _inv[3] += 1
                                inInv = True
                        if inInv == False:
                            self.draggedItem[3] = 1
                            self.playerInv.insert(0, self.draggedItem)
                self.draggedItem = []
                self.dragging = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for _inv in self.playerInv:
                    if _inv[4].collidepoint(self.mousePos):
                        self.dragging = True
                        if _inv[3] > 1:
                            copyInv = list(_inv)
                            copyInv[4] = pygame.Rect(0,0,50,50)
                            self.draggedItem = list(copyInv)
                            _inv[3] -= 1
                        else:
                            self.draggedItem = _inv
                            self.playerInv.remove(_inv)
                for _eqp in self.equippedInv:
                    if pygame.Rect(_eqp[4].x, _eqp[4].y, _eqp[1], _eqp[2]).collidepoint(self.mousePos):
                        self.dragging = True
                        self.draggedItem = _eqp
                        self.equippedInv.remove(_eqp)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                initGame()
                self.startGame = True

    def updateMenuScreen(self, block):
        if self.startGame == False:
            block.x = 530
            block.y = 206
        else: 
            self.startGame = False

    def drawMenuScreen(self, bg, screen, block):
        screen.fill((0, 0, 0))
        bg.drawThis(screen)
        screen.blit(self.playLabel, self.playRect)
        screen.blit(self.titleLabel, self.titleRect)
        screen.blit(self.inventoryLabel, self.inventoryRect)
        screen.blit(self.configLabel, self.configRect)

        #Ship grid
        pygame.draw.rect(screen, (50,50,50), self.gridRect)
        pygame.draw.rect(screen, (180,235,255), self.gridRect, 1)

        block.drawThis(screen)

        #Inventory List
        pygame.draw.rect(screen, (15,15,15), pygame.Rect(80,116, 350, 200))
        pygame.draw.rect(screen, (180,235,255), pygame.Rect(80,116, 350, 200), 1)

        if self.dragging:
            drugX = self.mousePos[0] - (self.draggedItem[1]/2)
            drugY = self.mousePos[1] - (self.draggedItem[2]/2)
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(drugX, drugY, self.draggedItem[1], self.draggedItem[2]))
            if self.draggedItem[0] == 'gun':
            	start = (drugX + (self.draggedItem[1]/2), drugY + (self.draggedItem[2]/2))
            	end = (drugX + (self.draggedItem[1]*1.5), drugY + (self.draggedItem[2]/2))
                pygame.draw.line(screen, (255,50,50), start,end)

        itemsCount = 0
        for item in self.playerInv:
            item[4].x = 90 + ((itemsCount%5)*70)
            item[4].y = 136 + (math.floor(itemsCount/5)*70)
            item[4].w = item[4].h = 50
            pygame.draw.rect(screen, (235,235,255), item[4], 1)

            modelW = item[1]
            modelH = item[2]
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(105 + ((itemsCount%5)*70),151 + (math.floor(itemsCount/5))*70, modelW, modelH))
            if item[0] == 'gun':
            	start = (105 + ((itemsCount%5)*70) + (modelW-4),151 + ((math.floor(itemsCount/5))*70) + (modelH/2))
            	end = (105 + ((itemsCount%5)*70) + (modelW+4), 151 + ((math.floor(itemsCount/5))*70) + (modelH/2))
                pygame.draw.line(screen, (255,50,50), start,end)
            if item[3] > 1:
                invText = item[0] + ' x' + str(item[3])
            else:
                invText = item[0]
            invLabel = self.smallfont.render(invText, True, (255, 255, 255), (0, 0, 0))
            invRect = invLabel.get_rect()
    	    invRect.x = 95 + ((itemsCount%5)*70)
            invRect.y = 170 + (math.floor(itemsCount/5))*70
            screen.blit(invLabel, invRect) 
            itemsCount += 1

        for hull in self.equippedInv:
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(hull[4].x, hull[4].y, hull[1], hull[2]))
            if hull[0] == 'gun':
            	start = (hull[4].x + (hull[1]/2), hull[4].y + (hull[2]/2))
            	end = (hull[4].x + (hull[1]*1.5), hull[4].y + (hull[2]/2))
                pygame.draw.line(screen, (255,50,50), start,end)