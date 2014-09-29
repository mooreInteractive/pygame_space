import pygame
import math

class mainMenu:

    endProgram = False
    startGame = False

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

    #def __init__(self):
    def getUserInput(self, initGame, done, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.endProgram = True
            #if event.type == pygame.USEREVENT + 1:
                #wave()
                #print 'wave(derp)'
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
        pygame.draw.rect(screen, (50,50,50), pygame.Rect(452,116, 200, 200))
        pygame.draw.rect(screen, (180,235,255), pygame.Rect(452,116, 200, 200), 1)

        #Inventory List
        pygame.draw.rect(screen, (15,15,15), pygame.Rect(80,116, 350, 200))
        pygame.draw.rect(screen, (180,235,255), pygame.Rect(80,116, 350, 200), 1)

        itemsCount = 0
        for item in block.invetory:

            pygame.draw.rect(screen, (235,235,255), pygame.Rect(90 + ((itemsCount%5)*70),136 + (math.floor(itemsCount/5)*70), 50, 50), 1)

            modelW = item[1]
            modelH = item[2]
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(105 + ((itemsCount%5)*70),151 + (math.floor(itemsCount/5))*70, modelW, modelH))
            if item[0] == 'gun':
            	start = (105 + ((itemsCount%5)*70) + (modelW-4),151 + ((math.floor(itemsCount/5))*70) + (modelH/2))
            	end = (105 + ((itemsCount%5)*70) + (modelW+4), 151 + ((math.floor(itemsCount/5))*70) + (modelH/2))
                pygame.draw.line(screen, (255,50,50), start,end)

            invText = item[0]
            invLabel = self.smallfont.render(invText, True, (255, 255, 255), (0, 0, 0))
            invRect = invLabel.get_rect()
    	    invRect.x = 105 + ((itemsCount%5)*70)
            invRect.y = 170 + (math.floor(itemsCount/5))*70
            screen.blit(invLabel, invRect) 
            itemsCount += 1

        block.drawThis(screen)







        
        
