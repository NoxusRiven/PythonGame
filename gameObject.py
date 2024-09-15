import pygame, random
from config import *
from abc import ABC, abstractmethod #importing abstract class

class GameObject(ABC): #ABC stands for abstract

    allObjects = []

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY):
        self.gameWindow = gameWindow
        self.objHeight = objHeight
        self.objWidth = objWidth
        self.objPosX = objPosX
        self.objPosY = objPosY

        self.rect = pygame.Rect(self.objPosX, self.objPosY, self.objWidth, self.objHeight)

        #adding object to list of all game objects
        GameObject.allObjects.append(self)
    
    @abstractmethod
    def draw(self):
        pass


    def returnCollidedObject(self, selfObject):
        for obj in GameObject.allObjects:
            if obj == selfObject:
                continue
            if obj.rect.colliderect(self.rect):
                return obj
            
        return None

    #iterating through all objects to check if they collide
    @classmethod
    def checkCollision(cls, rect, selfObject=None): 
        for obj in cls.allObjects:
            if obj == selfObject:
                continue
            if obj.rect.colliderect(rect):
                return obj
        return None

    #making sure that no object can be drawn on one another
    def canBeDrawn(self):
        if self in GameObject.allObjects:   
            while True:
                if not GameObject.checkCollision(self.rect, self):
                    self.draw()
                    break
                else:
                    self.rect.x = random.randint(0, WINDOW_W - self.rect.width)
                    self.rect.y = random.randint(0, WINDOW_H - self.rect.height)
                
            

