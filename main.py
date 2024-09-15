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
from cow import Cow
from pig import Pig

#game init
pygame.init()
clock = pygame.time.Clock() 

#open game window
gameWindow = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("My Game")

#game objects
gameMap = Map(gameWindow)

player = Player(gameWindow, 50, 50, random.randint(50,1500), random.randint(0,800), PLAYER_DMG) #(window, size, X, Y)

#1. environment
tree_small1 = Tree(gameWindow, SMALL_TREE_H, SMALL_TREE_W,  random.randint(0,WINDOW_W-SMALL_TREE_W), random.randint(0,WINDOW_H-SMALL_TREE_H), 2) #(window, X, Y)
tree_small2 = Tree(gameWindow, SMALL_TREE_H, SMALL_TREE_W,  random.randint(0,WINDOW_W-SMALL_TREE_W), random.randint(0,WINDOW_H-SMALL_TREE_H), 2)
tree_small3 = Tree(gameWindow, SMALL_TREE_H, SMALL_TREE_W,  random.randint(0,WINDOW_W-SMALL_TREE_W), random.randint(0,WINDOW_H-SMALL_TREE_H), 2)
tree_big1 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H), 3)
tree_big2 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H), 3)
tree_big3 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H), 3)
tree_big4 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H), 3)

rock_small1 = Rock(gameWindow, SMALL_ROCK_H, SMALL_ROCK_W, random.randint(0,WINDOW_W-SMALL_ROCK_W), random.randint(0,WINDOW_H-SMALL_ROCK_H), 1)
rock_small2 = Rock(gameWindow, SMALL_ROCK_H, SMALL_ROCK_W, random.randint(0,WINDOW_W-SMALL_ROCK_W), random.randint(0,WINDOW_H-SMALL_ROCK_H), 1)
rock_big1 = Rock(gameWindow, BIG_ROCK_H, BIG_ROCK_W, random.randint(0,WINDOW_W-BIG_ROCK_W), random.randint(0,WINDOW_H-BIG_ROCK_H), 2)
rock_big2 = Rock(gameWindow, BIG_ROCK_H, BIG_ROCK_W, random.randint(0,WINDOW_W-BIG_ROCK_W), random.randint(0,WINDOW_H-BIG_ROCK_H), 2)

#2. monsters
goblin1 = Goblin(gameWindow, GOBLIN_H, GOBLIN_W, random.randint(0,WINDOW_W-GOBLIN_W), random.randint(0,WINDOW_H-GOBLIN_H), GOBLIN_DMG, GOBLIN_HP, GOBLIN_SPEED)
goblin2 = Goblin(gameWindow, GOBLIN_H, GOBLIN_W, random.randint(0,WINDOW_W-GOBLIN_W), random.randint(0,WINDOW_H-GOBLIN_H), GOBLIN_DMG, GOBLIN_HP, GOBLIN_SPEED)

orc1 = Orc(gameWindow, ORC_H, ORC_W, random.randint(0,WINDOW_W-ORC_W), random.randint(0,WINDOW_H-ORC_H), ORC_DMG, ORC_HP, ORC_SPEED)
orc2 = Orc(gameWindow, ORC_H, ORC_W, random.randint(0,WINDOW_W-ORC_W), random.randint(0,WINDOW_H-ORC_H), ORC_DMG, ORC_HP, ORC_SPEED)

#3. passive mobs
pig1 = Pig(gameWindow, PIG_H, PIG_W, random.randint(0,WINDOW_W-PIG_W), random.randint(0,WINDOW_H-PIG_H), PIG_HP, PIG_SPEED)
pig2 = Pig(gameWindow, PIG_H, PIG_W, random.randint(0,WINDOW_W-PIG_W), random.randint(0,WINDOW_H-PIG_H), PIG_HP, PIG_SPEED)
pig3 = Pig(gameWindow, PIG_H, PIG_W, random.randint(0,WINDOW_W-PIG_W), random.randint(0,WINDOW_H-PIG_H), PIG_HP, PIG_SPEED)

cow1 = Cow(gameWindow, COW_H+100, COW_W+100, COW_START_X, COW_START_Y, COW_HP, COW_SPEED)
cow2 = Cow(gameWindow, COW_H, COW_W, random.randint(0,WINDOW_W-COW_W), random.randint(0,WINDOW_H-COW_H), COW_HP, COW_SPEED)
cow3 = Cow(gameWindow, COW_H, COW_W, random.randint(0,WINDOW_W-COW_W), random.randint(0,WINDOW_H-COW_H), COW_HP, COW_SPEED)


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
    if keys[pygame.K_w] and player.rect.y > 0: # if key is pressed and if player doesnt go outside the map
        futureRect.y -= PLAYER_MOVE_SPEED
        if GameObject.checkCollision(futureRect, player.rect) == None:
            player.moveYAxis(-PLAYER_MOVE_SPEED) #nums of pixels moving


    if keys[pygame.K_a] and player.rect.x > 0:
        futureRect.x -= PLAYER_MOVE_SPEED
        if GameObject.checkCollision(futureRect, player.rect) == None:
            player.moveXAxis(-PLAYER_MOVE_SPEED)


    if keys[pygame.K_s] and player.rect.y <= WINDOW_H - player.rect.height:
        futureRect.y += PLAYER_MOVE_SPEED
        if GameObject.checkCollision(futureRect, player.rect) == None:
            player.moveYAxis(PLAYER_MOVE_SPEED)
    
    if keys[pygame.K_d] and player.rect.x <= WINDOW_W - player.rect.width:
        futureRect.x += PLAYER_MOVE_SPEED
        if GameObject.checkCollision(futureRect, player.rect) == None:
            player.moveXAxis(PLAYER_MOVE_SPEED)

    if keys[pygame.K_f]:
        collidingObject = GameObject.checkCollision(player.interaRect, player.rect)
        if collidingObject != None:
            player.interact(collidingObject)
            
            

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
    """if GameObject.checkCollision(cow1):
        goblin1.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""
    goblin2.canBeDrawn()
    """if GameObject.checkCollision(cow1):
        goblin2.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""
    orc1.canBeDrawn()
    """if GameObject.checkCollision(cow1):
        orc1.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""
    orc2.canBeDrawn()
    """if GameObject.checkCollision(cow1):
        orc2.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""

    #drawing passive mobs
    pig1.canBeDrawn()
    """if GameObject.checkCollision(cow1):
        pig1.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""
    pig2.canBeDrawn()
    """if GameObject.checkCollision(cow1):
        pig2.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""
    pig3.canBeDrawn()
    """if GameObject.checkCollision(cow1):
        pig3.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""

    cow1.canBeDrawn()
    """if GameObject.checkCollision(cow1):
        cow1.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""

    cow2.canBeDrawn()
    """cow2.canBeDrawn()
    if GameObject.checkCollision(cow1):
        cow2.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""
    cow3.canBeDrawn()
    """if GameObject.checkCollision(cow1):
        cow3.moving(0, cow1.mobSPEED, COW_START_X, COW_DESTINATION_X)"""


    pygame.display.flip() #update the full display surface to the screen
    clock.tick(60) #tickrate/fps

#close pygame
pygame.quit()