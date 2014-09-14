import pygame

pygame.font.init()

class messages:
    basicfont = pygame.font.SysFont(None, 22)
        
    speedText = 'Speed: ' + str(0)
    rateText = 'Fire Rate: ' + str(0)
    ammoText = 'Ammo: ' + str(0)
      
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

    def drawText(self, screen, ship):
        self.speedText = 'Speed: ' + str(ship.speed)
        self.rateText = 'Fire Rate: ' + str(ship.firingRate)
        self.ammoText = 'Ammo: ' + str(ship.ammo)
        
        self.speedLabel = self.basicfont.render(self.speedText, True, (255, 255, 255), (0, 0, 0))
        self.rateLabel = self.basicfont.render(self.rateText, True, (255, 255, 255), (0, 0, 0))
        self.ammoLabel = self.basicfont.render(self.ammoText, True, (255, 255, 255), (0, 0, 0))
        
        screen.blit(self.speedLabel, self.speedRect)
        screen.blit(self.rateLabel, self.rateRect)
        screen.blit(self.ammoLabel, self.ammoRect)