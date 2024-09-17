import pygame, random
from config import *
from gameObject import GameObject
from collectable import Collectable

class Rock(Collectable):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, collecHp):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY, collecHp)

        self.rockModel = pygame.image.load("Models/Rock/rock_model.png")
        self.rockModel = pygame.transform.scale(self.rockModel, (BIG_ROCK_W, BIG_ROCK_H))


    def draw(self):
        if self in GameObject.allObjects:
            pygame.draw.rect(self.gameWindow, pygame.Color(55,55,55), self.rect)
            self.gameWindow.blit(self.rockModel, (self.rect.x, self.rect.y))

    def makeSmall(self):
        self.rockModel = pygame.transform.scale(self.rockModel, (SMALL_ROCK_W, SMALL_ROCK_H))    

