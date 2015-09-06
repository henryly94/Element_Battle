import sys
import pygame
from eb_test import *
from pygame.locals import *

class Element_Battle:
    def __init__(self):
        print "Initializing..."
        for paths in sys.path:
            print paths

    def run(self):
        print "Running..."
        test1()
        self.Key_Press()
        self.jugde()
        self.Motion()

    def jugde(self):
        print "Judging..."

    def Key_Press(self):
        print "Dealing with KeyPressing..."


    def Graphic(self):
        print "Graphic Function"

    def Motion(self):
        print "Motion Function"



if __name__ == "__main__":
    E_B = Element_Battle()
    E_B.run()