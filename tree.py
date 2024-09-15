import pygame, random
from gameObject import GameObject

class Tree(GameObject):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY)


    def draw(self):
        pygame.draw.rect(self.gameWindow, pygame.Color(55,0,0), self.rect)
        

