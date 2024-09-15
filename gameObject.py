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

    #cheking if object is touching another object
    def is_colliding(self, object):
        return self.rect.collidedict(object.rect)

    #iterating through all objects to check if they collide
    @classmethod
    def check_collision(cls, rect, selfObject=None): 
        for obj in cls.allObjects:
            if obj == selfObject:
                continue
            if obj.rect.colliderect(rect):
                #print(f"Collision detected between {rect} and {obj}") #debugging
                return True
        return False

    #making sure that no object can be drawn on one another
    def canBeDrawn(self):
        while True:
            if not GameObject.check_collision(self.rect, self):
                self.draw()
                break
            else:
                self.rect.x = random.randint(0, WINDOW_W - self.rect.width)
                self.rect.y = random.randint(0, WINDOW_H - self.rect.height)
                
            

