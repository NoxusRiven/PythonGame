import pygame
from config import *
from abc import ABC, abstractmethod
from gameObject import GameObject
from passiveMob import PassiveMob

class Pig(PassiveMob):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSPEED):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSPEED)

    def draw(self):
        if self in GameObject.allObjects:
            pygame.draw.rect(self.gameWindow, pygame.Color(250,100,100), self.rect)