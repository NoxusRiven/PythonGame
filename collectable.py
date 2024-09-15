import pygame
from config import *
from abc import ABC, abstractmethod
from gameObject import GameObject


class Collectable(GameObject):
    
    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, collecHp):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY)
        
        self.collecHp = collecHp