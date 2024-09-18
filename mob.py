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
        self.fullHp = self.mobHP

        #self.cooldown = 3

        self.hitboxRect = pygame.Rect(self.objPosX-15, self.objPosY-15, self.objWidth+30, self.objHeight+30)
    

    def draw(self):
        self.hpBarRect = pygame.Rect(self.rect.x, self.rect.y-15, self.rect.width , 10)
        pygame.draw.rect(self.gameWindow, pygame.Color(20,20,20), self.hpBarRect)
        #pygame.draw.rect(self.gameWindow, pygame.Color(255,255,255), self.hitboxRect)


    def moving(self, direction, mobMoveSpeed, start, destination):
        previousX = self.rect.x
        previousY = self.rect.y
        
        colliding_object = GameObject.checkCollision(self.hitboxRect, self)
        
        #checking collision with screen edges
        if  (colliding_object is None and 
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
            #if collision got detected we turn, revert move
            if colliding_object:
                #print(f"{self} collided with {colliding_object}") debuging

                self.rect.x = previousX
                self.rect.y = previousY
                self.hitboxRect.x = previousX-15
                self.hitboxRect.y = previousY-15

            #Screen edges collision
            if direction == 0:  # X-axis collision
                self.turnX = not self.turnX
                self.rect.x += mobMoveSpeed*2 if not self.turnX else -mobMoveSpeed*2
                self.hitboxRect.x += mobMoveSpeed*2 if not self.turnX else -mobMoveSpeed*2
            elif direction == 1:  # Y-axis collision
                self.turnY = not self.turnY
                self.rect.y += mobMoveSpeed*2 if not self.turnY else -mobMoveSpeed*2
                self.hitboxRect.y += mobMoveSpeed*2 if not self.turnY else -mobMoveSpeed*2
        
        # Kolizja z krawędzią ekranu
        if self.rect.x <= 0 or self.rect.x >= WINDOW_W - self.rect.width:
            self.turnX = not self.turnX
        if self.rect.y <= 0 or self.rect.y >= WINDOW_H - self.rect.height:
            self.turnY = not self.turnY
        

    def underAttack(self, playerDMG):
        self.gotAttacked = True
        #self.updateHPBar(playerDMG)
        #self.gotAttacked = False
        
    def updateHPBar(self, playerDMG):
        self.mobHP -= playerDMG
        dmgDone = self.mobHP/self.fullHp
        print("i update hp bar")
        self.hpBarRect = self.hpBarRect = pygame.Rect(self.rect.x, self.rect.y-15, int(self.rect.width*dmgDone), 10)
