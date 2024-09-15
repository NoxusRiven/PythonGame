import pygame
from config import *
from abc import ABC, abstractmethod
from passiveMob import PassiveMob

class Cow(PassiveMob):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSpeed):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSpeed)

    def draw(self):
        pygame.draw.rect(self.gameWindow, pygame.Color(250,250,250), self.rect)