import pygame, random
from gameObject import GameObject
from collectable import Collectable

class Rock(Collectable):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, collecHp):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY, collecHp)


    def draw(self):
        if self in GameObject.allObjects:
            pygame.draw.rect(self.gameWindow, pygame.Color(55,55,55), self.rect)
        

