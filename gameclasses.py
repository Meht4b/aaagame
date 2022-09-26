import pygame

class Bullet():
    def __init__(self,x,y):
        self.posx=x
        self.posy=y
        self.vel=10
        
    def move(self):
        self.posx+=self.vel
        self.rect =(self.posx,self.posy,10,4)

    def draw(self,win):
        pygame.draw.rect(win,(0,0,255),self.rect)

    def getPosx(self):
        return self.posx


class Player():
    def __init__(self,color,x,y,):
        self.posx=x
        self.posy=y
        self.color=color
        self.vel=10
        self.rect=(self.posx,self.posy, 30,30)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.posy>0:
            self.posy-=self.vel
        if keys[pygame.K_s] and self.posy<930:
            self.posy+=self.vel
        if keys[pygame.K_a] and self.posx>0:
            self.posx-=self.vel
        if keys[pygame.K_d] and self.posx<1250:
            self.posx+=self.vel

        self.rect=(self.posx,self.posy, 30,30)



            

    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)