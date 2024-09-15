import pygame

class Map():
    
    def __init__(self,gameWindow):
        self.gameWindow = gameWindow

        

    def update(self): #use update to update map independently of player (mobs etc.)
        pass

    def draw(self):
        self.gameWindow.fill(pygame.Color(50,150,50)) #map coloring

    def run(self):
        self.update()
        self.draw()