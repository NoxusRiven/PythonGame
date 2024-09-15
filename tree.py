import pygame, random
from collectable import Collectable

class Tree(Collectable):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, collecHp):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY, collecHp)


    def draw(self):
        pygame.draw.rect(self.gameWindow, pygame.Color(55,0,0), self.rect)
        

