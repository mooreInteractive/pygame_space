import pygame

class bullet:
    w = 6
    h = 2
    x = 0
    y = 0
    color = (255, 255, 255)
    speed = 6
    badBullet = False
    _bullets = []
    
    def __init__(self, enBullet, bulletArr):
        self.badBullet = enBullet
        self._bullets = bulletArr
        if self.badBullet == True:
            self.speed *= -1

    def drawThis(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x,self.y,self.w,self.h))

    def updateThis(self):

        self.x += self.speed
        if self.x > 768 or self.x < 0:
            self._bullets.remove(self)
            #print len(bullets) 