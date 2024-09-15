import pygame
from gameObject import GameObject

class Player(GameObject):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY)

    def moveXAxis(self,direction):
        self.rect.x += direction


    def moveYAxis(self,direction):
        self.rect.y += direction

    def draw(self):
        pygame.draw.rect(self.gameWindow, pygame.Color(255,100,100), self.rect) #drawing player

