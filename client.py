from operator import index
import pygame,sys
from gameclasses import Player,Bullet
from clientnetwork import clientNet

pygame.init()

winHeight=720
winWidth=1280

win = pygame.display.set_mode((winWidth,winHeight))

clock = pygame.time.Clock()

network=clientNet()
p1=network.connect()
bulletlist=[]
t1=Player((10,10,10),40,40)
t2=Player((20,20,20,),60,60)
testarr=[t1,t2]

while True:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit


    win.fill((0,0,0))


    p1.move()
    p2=network.send(p1)
    print('recv obj p2')

    p1.draw(win)
    p2.draw(win)
    pygame.display.flip()