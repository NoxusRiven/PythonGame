import pygame, random
from config import *
from gameObject import GameObject
from collectable import Collectable

class Tree(Collectable):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, collecHp):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY, collecHp)
        
        self.treeModel = pygame.image.load("Models/Tree/tree_model.png")


    def draw(self):
        if self in GameObject.allObjects:
            #pygame.draw.rect(self.gameWindow, pygame.Color(55,0,0), self.rect) #hitbox
            self.gameWindow.blit(self.treeModel, (self.rect.x-8, self.rect.y))

        
    def makeSmall(self):
        self.treeModel = pygame.transform.scale(self.treeModel, (SMALL_TREE_H, SMALL_TREE_H))
