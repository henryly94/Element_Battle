__author__ = 'Administrator'
import Object

class Character(Object.Object):
    def __init__(self):
        Object.Object.__init__(self)
        self.attack = 10
        self.defence = 10
        self.destination = [0.0,0.0,0.0]
    def ch_speed(self,s):
        self.speed = s

    def ch_mode(self,m):
        self.mode = m