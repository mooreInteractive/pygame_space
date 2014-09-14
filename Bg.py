import pygame
pygame.init()

class bg():
    img = None
    x = 0
    y = 0
    altx = 0
    alty = 0
    onAlt = False
    width = 1600
    height = 480

    def updateThis(self):
        if self.onAlt:
            self.altx = self.x + self.width
            self.x -= 2
        else:    
            self.x -= 2
        switchDist = -(self.width - 768)
        if self.x <= switchDist:
            self.altx = self.x + self.width
            self.onAlt = True
        if self.x <= -(self.width):
            self.onAlt = False
            self.x = self.altx 

    def drawThis(self, screen):
        if self.onAlt:
            screen.blit(self.img, (self.x, self.y))
            screen.blit(self.img, (self.altx, self.alty))
        else:    
            screen.blit(self.img, (self.x, self.y))