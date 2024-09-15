import pygame, random
from pygame.locals import *
from config import *
from gameObject import GameObject
from map import Map
from player import Player
from tree import Tree

#game init
pygame.init()
clock = pygame.time.Clock() 

#open game window
gameWindow = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("My Game")

#game objects
gameMap = Map(gameWindow)

player = Player(gameWindow, 50, 50, random.randint(50,1500), random.randint(50,800)) #(window, size, X, Y)

tree_small1 = Tree(gameWindow, 80, 30,  random.randint(30,1520), random.randint(80,780)) #(window, X, Y)
#print(f"{tree_small1.objPosX}, {tree_small1.objPosY}")
tree_small2 = Tree(gameWindow, 80, 30,  random.randint(30,1520), random.randint(80,780))
#print(f"{tree_small2.objPosX}, {tree_small2.objPosY}")
tree_small3 = Tree(gameWindow, 80, 30,  random.randint(30,1520), random.randint(80,780))
#print(f"{tree_small3.objPosX}, {tree_small3.objPosY}")
tree_big1 = Tree(gameWindow, 100, 40, random.randint(40,1510), random.randint(100,750))
#print(f"{tree_big1.objPosX}, {tree_big1.objPosY}")
tree_big2 = Tree(gameWindow, 100, 40, random.randint(40,1510), random.randint(100,750))
tree_big3 = Tree(gameWindow, 100, 40, random.randint(40,1510), random.randint(100,750))
tree_big4 = Tree(gameWindow, 100, 40, random.randint(40,1510), random.randint(100,750))
#print(f"{tree_big2.objPosX}, {tree_big2.objPosY}")


gameIsRuning = True
while gameIsRuning:
    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRuning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameIsRuning = False

    #player movment
    futureRect = player.rect.copy()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.rect.x > 0: # if key is pressed and if player doesnt go outside the map
        futureRect.y -= 5
        if not GameObject.check_collision(futureRect, player.rect):
            player.moveYAxis(-5) #nums of pixels moving


    if keys[pygame.K_a] and player.rect.x > 0:
        futureRect.x -= 5
        if not GameObject.check_collision(futureRect, player.rect):
            player.moveXAxis(-5)


    if keys[pygame.K_s] and player.rect.y <= window_h - player.objHeight:
        futureRect.y += 5
        if not GameObject.check_collision(futureRect, player.rect):

            player.moveYAxis(5)
    
    if keys[pygame.K_d] and player.rect.x <= window_w - player.objWidth:
        futureRect.x += 5
        if not GameObject.check_collision(futureRect, player.rect):
            player.moveXAxis(5)
            

    gameMap.draw() #map refresh
    player.draw() #player refresh
    
    #drawing trees
    tree_small1.canBeDrawn()
    tree_small2.canBeDrawn()
    tree_small3.canBeDrawn()
    tree_big1.canBeDrawn()
    tree_big2.canBeDrawn()
    tree_big3.canBeDrawn()
    tree_big4.canBeDrawn()

    pygame.display.flip()
    clock.tick(60)

#close pygame
pygame.quit()