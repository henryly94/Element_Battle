__author__ = 'Administrator'
import sys
import pygame
from math import *

class Object():
    def __init__(self):
        self.percent = 0.5
        self.position = [0.0,0.0,0.0]
        self.speed = 1.0
        self.mode = 0
        self.motion_pic = pygame.image.load("../img/default.jpg")
#        for i in range(30):
#            self.move([2,3,4])

    def move(self,des):
        dis = [des[0]-self.position[0],des[1]-self.position[1],des[2]-self.position[2]]
        tmp = sqrt(pow(dis[0],2)+pow(dis[1],2)+pow(dis[2],2))
        if tmp < 1:
            return
        for i in range(3):
            self.position[i] = (self.position[i] + (self.speed * dis[i] * self.percent) / tmp)
        print self.position
