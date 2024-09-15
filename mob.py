import pygame
from config import *
from abc import ABC, abstractmethod
from gameObject import GameObject


class Mob(GameObject):
    
    
    def __init__(self, gameWindow, objHeight, objWidth, objPosX, objPosY, mobHP, mobSPEED):
        super().__init__(gameWindow, objHeight, objWidth, objPosX, objPosY)
        self.mobHP = mobHP
        self.mobSPEED = mobSPEED
        self.turn = False


    def moving(self, direction, mobMoveSpeed, start, destination):
        if direction == 0: #left-right
            if not self.turn:    
                self.rect.x += mobMoveSpeed

                print(self.rect.x)
                print(destination)
                if(self.rect.x >= destination):
                    print("zmiana")
                    self.turn = True
            elif self.turn:
                self.rect.x -= mobMoveSpeed
                if(self.rect.x == start):
                    self.turn = False
        elif direction == 1: #up-down
            
            if not self.turn:    
                self.rect.y += mobMoveSpeed
                if(self.rect.y == destination):
                    self.turn = True
            elif self.turn:
                self.rect.y -= mobMoveSpeed
                if(self.rect.y == start):
                    self.turn = False
