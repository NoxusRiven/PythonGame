import pygame
from config import *
from abc import ABC, abstractmethod
from mob import Mob


class Monster(Mob):
    
    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSPEED, monsterDMG):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSPEED)

        self.monsterDMG = monsterDMG