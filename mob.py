import pygame
from config import *
from abc import ABC, abstractmethod
from gameObject import GameObject


class Mob(GameObject):
    
    
    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSPEED):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY)
        
        self.mobHP = mobHP
        self.mobSPEED = mobSPEED
        self.turnX = False
        self.turnY = False
        self.gotAttacked = False

        #self.cooldown = 3

        self.hitboxRect = pygame.Rect(self.objPosX-10, self.objPosY-10, self.objWidth+20, self.objHeight+20)
        self.hpBarRect = pygame.Rect(self.rect.x-15, self.rect.y-15, 60 , 10)
    

    def draw(self):
        self.hpBarRect = pygame.Rect(self.rect.x, self.rect.y-15, self.rect.width , 10)
        pygame.draw.rect(self.gameWindow, pygame.Color(20,20,20), self.hpBarRect)


    def moving(self, direction, mobMoveSpeed, start, destination):
        colliding_object = GameObject.checkCollision(self.hitboxRect, self)
        
        #checking collision with screen edges
        if  (colliding_object == None and 
            0 <= self.rect.y <= WINDOW_H - self.rect.height and 
            0 <= self.rect.x <= WINDOW_W - self.rect.width):    
            
            if direction == 0: #left-right
                
                if not self.turnX: #right
                    self.rect.x += mobMoveSpeed
                    self.hitboxRect.x += mobMoveSpeed
                    if self.rect.x >= destination: #turning back to start
                        self.turnX = True
                
                else:               #left
                    self.rect.x -= mobMoveSpeed
                    self.hitboxRect.x -= mobMoveSpeed
                    if self.rect.x <= start: #turning back to destination
                        self.turnX = False
            
            elif direction == 1: #up-down
                
                if not self.turnY: #down
                    self.rect.y += mobMoveSpeed
                    self.hitboxRect.y += mobMoveSpeed
                    if self.rect.y >= destination:
                        self.turnY = True
                
                else:               #up   
                    self.rect.y -= mobMoveSpeed
                    self.hitboxRect.y -= mobMoveSpeed
                    if self.rect.y <= start:
                        self.turnY = False
        else:
            #if collision got detected we turn
            if colliding_object:
                #turn back object (mobSpeed value)
                if direction == 0:  #if X axies
                    self.rect.x -= mobMoveSpeed if not self.turnX else -mobMoveSpeed
                    self.hitboxRect.x -= mobMoveSpeed if not self.turnX else -mobMoveSpeed
                    self.turnX = not self.turnX
                elif direction == 1:  #if Y axies
                    self.rect.y -= mobMoveSpeed if not self.turnY else -mobMoveSpeed
                    self.hitboxRect.y -= mobMoveSpeed if not self.turnY else -mobMoveSpeed
                    self.turnY = not self.turnY

            #Screen edges collision
            if self.rect.x <= 0 or self.rect.x >= WINDOW_W - self.rect.width:
                self.turnX = not self.turnX
            if self.rect.y <= 0 or self.rect.y >= WINDOW_H - self.rect.height:
                self.turnY = not self.turnY

    def underAttack(self):
        self.gotAttacked = True
        
