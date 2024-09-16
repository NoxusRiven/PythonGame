import pygame
from gameObject import GameObject
from tree import Tree
from rock import Rock
from mob import Mob

class Player(GameObject):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, playerDMG):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY)
        self.playerDMG = playerDMG

        self.interaRect = pygame.Rect(self.objPosX-10, self.objPosY-10, self.objWidth+20, self.objHeight+20)

    def moveXAxis(self,direction):
        self.rect.x += direction
        self.interaRect.x += direction


    def moveYAxis(self,direction):
        self.rect.y += direction
        self.interaRect.y += direction

    def draw(self):
        #pygame.draw.rect(self.gameWindow, pygame.Color(255,255,255), self.interaRect)
        pygame.draw.rect(self.gameWindow, pygame.Color(255,50,50), self.rect) #drawing player

    def interact(self, object):
        pass
        #if self.rect.colliderect(object.rect):
        if isinstance(object, Tree): #program doesnt detect interaction with tree
                self.gather(object)
        elif isinstance(object, Rock):
                self.gather(object)
    
    def gather(self, object):
        if object in GameObject.allObjects:
            GameObject.allObjects.remove(object)

    def attack(self, object):
         if object in GameObject.allObjects:
            if isinstance(object, Mob):
                object.underAttack()