import pygame, random
from pygame.locals import *
from config import *
from gameObject import GameObject
from map import Map
from player import Player
from tree import Tree
from rock import Rock
from orc import Orc
from goblin import Goblin

#game init
pygame.init()
clock = pygame.time.Clock() 

#open game window
gameWindow = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("My Game")

#game objects
gameMap = Map(gameWindow)

player = Player(gameWindow, 50, 50, random.randint(50,1500), random.randint(0,800)) #(window, size, X, Y)

#1. environment
tree_small1 = Tree(gameWindow, SMALL_TREE_H, SMALL_TREE_W,  random.randint(0,WINDOW_W-SMALL_TREE_W), random.randint(0,WINDOW_H-SMALL_TREE_H)) #(window, X, Y)
tree_small2 = Tree(gameWindow, SMALL_TREE_H, SMALL_TREE_W,  random.randint(0,WINDOW_W-SMALL_TREE_W), random.randint(0,WINDOW_H-SMALL_TREE_H))
tree_small3 = Tree(gameWindow, SMALL_TREE_H, SMALL_TREE_W,  random.randint(0,WINDOW_W-SMALL_TREE_W), random.randint(0,WINDOW_H-SMALL_TREE_H))
tree_big1 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H))
tree_big2 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H))
tree_big3 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H))
tree_big4 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H))

rock_small1 = Rock(gameWindow, SMALL_ROCK_H, SMALL_ROCK_W, random.randint(0,WINDOW_W-SMALL_ROCK_W), random.randint(0,WINDOW_H-SMALL_ROCK_H))
rock_small2 = Rock(gameWindow, SMALL_ROCK_H, SMALL_ROCK_W, random.randint(0,WINDOW_W-SMALL_ROCK_W), random.randint(0,WINDOW_H-SMALL_ROCK_H))
rock_big1 = Rock(gameWindow, BIG_ROCK_H, BIG_ROCK_W, random.randint(0,WINDOW_W-BIG_ROCK_W), random.randint(0,WINDOW_H-BIG_ROCK_H))
rock_big2 = Rock(gameWindow, BIG_ROCK_H, BIG_ROCK_W, random.randint(0,WINDOW_W-BIG_ROCK_W), random.randint(0,WINDOW_H-BIG_ROCK_H))

#2. monsters
goblin1 = Goblin(gameWindow, GOBLIN_H, GOBLIN_W, random.randint(0,WINDOW_W-GOBLIN_W), random.randint(0,WINDOW_H-GOBLIN_H), GOBLIN_DMG, GOBLIN_HP, GOBLIN_SPEED)
goblin2 = Goblin(gameWindow, GOBLIN_H, GOBLIN_W, random.randint(0,WINDOW_W-GOBLIN_W), random.randint(0,WINDOW_H-GOBLIN_H), GOBLIN_DMG, GOBLIN_HP, GOBLIN_SPEED)

orc1 = Orc(gameWindow, ORC_H, ORC_W, random.randint(0,WINDOW_W-ORC_W), random.randint(0,WINDOW_H-ORC_H), ORC_DMG, ORC_HP, ORC_SPEED)
orc2 = Orc(gameWindow, ORC_H, ORC_W, random.randint(0,WINDOW_W-ORC_W), random.randint(0,WINDOW_H-ORC_H), ORC_DMG, ORC_HP, ORC_SPEED)

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
        futureRect.y -= PLAYER_MOVE_SPEED
        if not GameObject.check_collision(futureRect, player.rect):
            player.moveYAxis(-PLAYER_MOVE_SPEED) #nums of pixels moving


    if keys[pygame.K_a] and player.rect.x > 0:
        futureRect.x -= PLAYER_MOVE_SPEED
        if not GameObject.check_collision(futureRect, player.rect):
            player.moveXAxis(-PLAYER_MOVE_SPEED)


    if keys[pygame.K_s] and player.rect.y <= WINDOW_H - player.objHeight:
        futureRect.y += PLAYER_MOVE_SPEED
        if not GameObject.check_collision(futureRect, player.rect):

            player.moveYAxis(PLAYER_MOVE_SPEED)
    
    if keys[pygame.K_d] and player.rect.x <= WINDOW_W - player.objWidth:
        futureRect.x += PLAYER_MOVE_SPEED
        if not GameObject.check_collision(futureRect, player.rect):
            player.moveXAxis(PLAYER_MOVE_SPEED)
            

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

    #drawing rocks
    rock_small1.canBeDrawn()
    rock_small2.canBeDrawn()
    rock_big1.canBeDrawn()
    rock_big2.canBeDrawn()


    #drawing monsters
    goblin1.canBeDrawn()
    goblin2.canBeDrawn()
    orc1.canBeDrawn()
    orc2.canBeDrawn()

    pygame.display.flip() #update the full display surface to the screen
    clock.tick(60) #tickrate/fps

#close pygame
pygame.quit()