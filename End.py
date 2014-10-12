import pygame

pygame.font.init()

class messages:
    basicfont = pygame.font.SysFont(None, 22)
        
    firstText = 'That\'s pretty much it. Great Job beating that fatty at the end!'
    secondText = 'Thank you for playing!'
    thirdText = '-Adam Moore'
    fourthText = 'http://moore-interactive.net'
      
    firstLabel = basicfont.render(firstText, True, (255, 255, 255), (0, 0, 0))
    secondLabel = basicfont.render(secondText, True, (255, 255, 255), (0, 0, 0))
    thirdLabel = basicfont.render(thirdText, True, (255, 255, 255), (0, 0, 0))
    fourthLabel = basicfont.render(fourthText, True, (255, 255, 255), (0, 0, 0))
                
    firstRect = firstLabel.get_rect()
    secondRect = secondLabel.get_rect()
    thirdRect = thirdLabel.get_rect()
    fourthRect = fourthLabel.get_rect()
        
    firstRect.x = 185
    firstRect.y = 100

    secondRect.x = 335
    secondRect.y = 150

    thirdRect.x = 450
    thirdRect.y = 340

    fourthRect.x = 450
    fourthRect.y = 365

    def drawText(self, screen, ship):
        
        screen.blit(self.firstLabel, self.firstRect)
        screen.blit(self.secondLabel, self.secondRect)
        screen.blit(self.thirdLabel, self.thirdRect)
        screen.blit(self.fourthLabel, self.fourthRect)