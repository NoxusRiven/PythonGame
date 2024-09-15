import pygame
from config import *
from abc import ABC, abstractmethod
from gameObject import GameObject


class Monster(GameObject):
    
    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, monsterDMG, monsterHP, monsterSPEED):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY)
        self.monsterDMG = monsterDMG
        self.monsterHP = monsterHP
        self.monsterSPEED = monsterSPEED