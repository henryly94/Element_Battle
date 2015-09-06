__author__ = 'Administrator'
import sys
import pygame
from pygame.locals import *
from math import *

class Object():
    def __init__(self):
        self.percent = 0.5
        self.position = [0.0,0.0,0.0]
        self.speed = 1.0
        self.mode = 0
        self.motion_pic = ""
#        for i in range(30):
#            self.move([2,3,4])
    def ch_pic(self,path):
        self.motion_pic = path

    def move(self,des):
        dis = [des[0]-self.position[0],des[1]-self.position[1],des[2]-self.position[2]]
        tmp = sqrt(pow(dis[0],2)+pow(dis[1],2)+pow(dis[2],2))
        if tmp < 1:
            return
        for i in range(3):
            self.position[i] = (self.position[i] + (self.speed * dis[i] * self.percent) / tmp)
        print self.position


class Character(Object):
    def __init__(self):
        Object.__init__(self)
        self.attack = 10
        self.defence = 10
        self.destination = [0,0,0]
    def ch_speed(self,s):
        self.speed = s

    def ch_mode(self,m):
        self.mode = m


class background(Object):
    def __init__(self):
        Object.__init__()

class Stage():
    def __init__(self):
        self.test = Character()
        self.Items = []
        self.run()

    def Input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            print('Pressed LEFT Button!')
                        elif index == 1:
                            print('The mouse wheel Pressed!')
                        elif index == 2:
                            mouse_pos = pygame.mouse.get_pos()
                            self.test.destination[0] = mouse_pos[0]
                            self.test.destination[1] = mouse_pos[1]
                            print mouse_pos
                            print('Pressed RIGHT Button!')
    def Compute(self):
        a = 1

    def Output(self,screen):
        screen.blit(self.Items[1],[0,0])
        #screen.fill(0x00FF00)
        screen.blit(self.Items[0],[self.test.position[0],self.test.position[1]])
        self.test.move([self.test.destination[0]-60,self.test.destination[1]-60,0])
        pygame.display.flip()


    def Initialize(self):
        backGround = pygame.image.load("img/BG.jpg")
        player = pygame.image.load("img/001.png")
        self.Items.append(player)
        self.Items.append(backGround)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((480,288))

        # Initialize
        self.Initialize()

        while 1:

            # Input
            self.Input()


            # Compute
            self.Compute()

            # Output
            self.Output(screen)

if __name__ == "__main__":
#    ob = Object()
    st = Stage()


