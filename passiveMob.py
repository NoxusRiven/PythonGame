import pygame
from config import *
from abc import ABC, abstractmethod
from mob import Mob


class PassiveMob(Mob):
    
    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSpeed):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSpeed)