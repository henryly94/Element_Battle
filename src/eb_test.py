import pygame
import math
from pygame.locals import  *


def test1():
    pygame.init()

    keys = [False,False,False,False]
    playerpos = [100,100]
    backGround = pygame.image.load("img/BG.jpg")

    screen = pygame.display.set_mode((480,288))
    player = pygame.image.load("img/001.png")

    while 1:

        screen.blit(backGround,[0,0])
        #screen.fill(0x00FF00)
        #screen.blit
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1]-(playerpos[1]),position[0]-(playerpos[0]))
        playerrot = pygame.transform.rotate(player, 270-angle*57.29)
        playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
        screen.blit(playerrot, playerpos1)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key==K_w:
                    keys[0]=True
                elif event.key==K_a:
                    keys[1]=True
                elif event.key==K_s:
                    keys[2]=True
                elif event.key==K_d:
                    keys[3]=True
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    keys[0]=False
                elif event.key==pygame.K_a:
                    keys[1]=False
                elif event.key==pygame.K_s:
                    keys[2]=False
                elif event.key==pygame.K_d:
                    keys[3]=False
        if keys[0]:
            playerpos[1]-=0.3
        elif keys[2]:
            playerpos[1]+=0.3
        if keys[1]:
            playerpos[0]-=0.3
        elif keys[3]:
            playerpos[0]+=0.3