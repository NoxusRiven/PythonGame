import pygame
from config import*
from gameObject import GameObject
from monster import Monster

class Orc(Monster):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, monsterDMG, monsterHP, monsterSPEED):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY, monsterDMG, monsterHP, monsterSPEED)

    def draw(self):
        if self in GameObject.allObjects:
            pygame.draw.rect(self.gameWindow, pygame.Color(10,50,10), self.rect)