import pygame, random
from gameObject import GameObject

class Rock(GameObject):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY)


    def draw(self):
        pygame.draw.rect(self.gameWindow, pygame.Color(55,55,55), self.rect)
        

