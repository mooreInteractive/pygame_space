import pygame

pygame.font.init()

class messages:
    basicfont = pygame.font.SysFont(None, 22)
        
    speedText = 'Speed: ' + str(0)
    rateText = 'Fire Rate: ' + str(0)
      
    speedLabel = basicfont.render(speedText, True, (255, 255, 255), (0, 0, 0))
    rateLabel = basicfont.render(rateText, True, (255, 255, 255), (0, 0, 0))
                
    speedRect = speedLabel.get_rect()
    rateRect = rateLabel.get_rect()
        
    speedRect.x = 565
    speedRect.y = 45
       
    rateRect.x = 655
    rateRect.y = 45
    
    energyBar = pygame.Rect(550, 15, 200, 25)

    def drawText(self, screen, ship):
        self.speedText = 'Speed: ' + str(ship.speed)
        self.rateText = 'Fire Rate: ' + str(ship.firingRate)
        
        self.speedLabel = self.basicfont.render(self.speedText, True, (255, 255, 255), (0, 0, 0))
        self.rateLabel = self.basicfont.render(self.rateText, True, (255, 255, 255), (0, 0, 0))
        
        screen.blit(self.speedLabel, self.speedRect)
        screen.blit(self.rateLabel, self.rateRect)
        
        for i in range(1,int(ship.energy)+1):
            if i > 100:
                i1 = i-100
                if i1%10 == 0 or i1%10 == 1:
                    pygame.draw.line(screen, (85, 235, 250), ((self.energyBar.x+i1*2),self.energyBar.y+15), ((self.energyBar.x+i1*2),self.energyBar.y+22))
                
                elif i1%10 == 9 or i1%10 == 2:
                    pygame.draw.line(screen, (85, 235, 250), ((self.energyBar.x+i1*2),self.energyBar.y+15), ((self.energyBar.x+i1*2),self.energyBar.y+24))
                
                else:
                    pygame.draw.line(screen, (85, 235, 250), ((self.energyBar.x+i1*2),self.energyBar.y+15), ((self.energyBar.x+i1*2),self.energyBar.y+25))
            else:
                if i%10 == 0 or i%10 == 1:
                    pygame.draw.line(screen, (55, 135, 250), ((self.energyBar.x+i*2),self.energyBar.y+3), ((self.energyBar.x+i*2),self.energyBar.y+22))
                
                elif i%10 == 9 or i%10 == 2:
                    pygame.draw.line(screen, (55, 135, 250), ((self.energyBar.x+i*2),self.energyBar.y+1), ((self.energyBar.x+i*2),self.energyBar.y+24))
                
                else:
                    pygame.draw.line(screen, (55, 135, 250), ((self.energyBar.x+i*2),self.energyBar.y), ((self.energyBar.x+i*2),self.energyBar.y+25))