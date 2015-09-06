__author__ = 'Administrator'

import sys
import pygame
from pygame.locals import *
import Character
from math import *


class Stage():
    def __init__(self):
        self.test = Character.Character()
        self.Display = []
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
        self.test.move([self.test.destination[0]-60,self.test.destination[1]-60,0])

    def Output(self,screen):

        screen.blit()
        for item in self.Display:
            screen.blit(item.motion_pic,item.position[0:2])

        pygame.display.flip()


    def Initialize(self):
        backGround = Character.Character()
        backGround.motion_pic = pygame.image.load("../img/BG.jpg")
        self.Display.append(backGround)

        self.test.motion_pic = pygame.image.load("../img/001.png")
        self.Display.append(self.test)


    def run(self):
        pygame.init()
        pygame.time.Clock().tick(1)
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
