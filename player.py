import pygame
from gameObject import GameObject
from tree import Tree
from rock import Rock
from mob import Mob

class Player(GameObject):

    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, playerDMG):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY)
        self.playerDMG = playerDMG
        self.playerModel = pygame.image.load("Models/Player/player_model_moving_down.png")
        self.interaRect = pygame.Rect(self.rect.x-10, self.rect.y-10, self.rect.width+20, self.rect.height+20)

    def moveXAxis(self,direction):
        self.rect.x += direction
        self.interaRect.x += direction


    def moveYAxis(self,direction):
        self.rect.y += direction
        self.interaRect.y += direction

    def draw(self):
        #debuging
        #pygame.draw.rect(self.gameWindow, pygame.Color(255,255,255), self.interaRect) #drawing interactive range
        #pygame.draw.rect(self.gameWindow, pygame.Color(255,50,50), self.rect) #drawing hitbox
        
        self.gameWindow.blit(self.playerModel, (self.rect.x-40, self.rect.y))

    def interact(self, object):
        if isinstance(object, Tree):
                self.gather(object)
        elif isinstance(object, Rock):
                self.gather(object)
    
    def gather(self, object):
        if object in GameObject.allObjects:
            GameObject.allObjects.remove(object)

    def attack(self, object):
         if object in GameObject.allObjects:
            if isinstance(object, Mob):
                object.underAttack(self.playerDMG)