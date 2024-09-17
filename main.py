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

player = Player(gameWindow, 128, 50, random.randint(50,1500), random.randint(0,800), PLAYER_DMG) #(window, size, X, Y)

#1. environment
tree_small1 = Tree(gameWindow, SMALL_TREE_H, SMALL_TREE_W,  random.randint(0,WINDOW_W-SMALL_TREE_W), random.randint(0,WINDOW_H-SMALL_TREE_H), 2) #(window, X, Y)
tree_small1.makeSmall()
tree_small1.canBeDrawn()

tree_small2 = Tree(gameWindow, SMALL_TREE_H, SMALL_TREE_W,  random.randint(0,WINDOW_W-SMALL_TREE_W), random.randint(0,WINDOW_H-SMALL_TREE_H), 2)
tree_small2.makeSmall()
tree_small2.canBeDrawn()

tree_small3 = Tree(gameWindow, SMALL_TREE_H, SMALL_TREE_W,  random.randint(0,WINDOW_W-SMALL_TREE_W), random.randint(0,WINDOW_H-SMALL_TREE_H), 2)
tree_small3.makeSmall()
tree_small3.canBeDrawn()

tree_big1 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H), 3)
tree_big1.canBeDrawn()

tree_big2 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H), 3)
tree_big2.canBeDrawn()

tree_big3 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H), 3)
tree_big3.canBeDrawn()

tree_big4 = Tree(gameWindow, BIG_TREE_H, BIG_TREE_W, random.randint(0,WINDOW_W-BIG_TREE_W), random.randint(0,WINDOW_H-BIG_TREE_H), 3)
tree_big4.canBeDrawn()


rock_small1 = Rock(gameWindow, SMALL_ROCK_H, SMALL_ROCK_W, random.randint(0,WINDOW_W-SMALL_ROCK_W), random.randint(0,WINDOW_H-SMALL_ROCK_H), 1)
rock_small1.makeSmall()
rock_small1.canBeDrawn()

rock_small2 = Rock(gameWindow, SMALL_ROCK_H, SMALL_ROCK_W, random.randint(0,WINDOW_W-SMALL_ROCK_W), random.randint(0,WINDOW_H-SMALL_ROCK_H), 1)
rock_small2.makeSmall()
rock_small2.canBeDrawn()

rock_big1 = Rock(gameWindow, BIG_ROCK_H, BIG_ROCK_W, random.randint(0,WINDOW_W-BIG_ROCK_W), random.randint(0,WINDOW_H-BIG_ROCK_H), 2)
rock_big1.canBeDrawn()

rock_big2 = Rock(gameWindow, BIG_ROCK_H, BIG_ROCK_W, random.randint(0,WINDOW_W-BIG_ROCK_W), random.randint(0,WINDOW_H-BIG_ROCK_H), 2)
rock_big2.canBeDrawn()


#2. monsters
goblin1 = Goblin(gameWindow, GOBLIN_H, GOBLIN_W, random.randint(0,WINDOW_W-GOBLIN_W), random.randint(0,WINDOW_H-GOBLIN_H), GOBLIN_DMG, GOBLIN_HP, GOBLIN_SPEED)
goblin1.canBeDrawn()

goblin2 = Goblin(gameWindow, GOBLIN_H, GOBLIN_W, random.randint(0,WINDOW_W-GOBLIN_W), random.randint(0,WINDOW_H-GOBLIN_H), GOBLIN_DMG, GOBLIN_HP, GOBLIN_SPEED)
goblin2.canBeDrawn()


orc1 = Orc(gameWindow, ORC_H, ORC_W, random.randint(0,WINDOW_W-ORC_W), random.randint(0,WINDOW_H-ORC_H), ORC_DMG, ORC_HP, ORC_SPEED)
orc1.canBeDrawn()

orc2 = Orc(gameWindow, ORC_H, ORC_W, random.randint(0,WINDOW_W-ORC_W), random.randint(0,WINDOW_H-ORC_H), ORC_DMG, ORC_HP, ORC_SPEED)
orc2.canBeDrawn()


#3. passive mobs
pig1 = Pig(gameWindow, PIG_H, PIG_W, random.randint(0,WINDOW_W-PIG_W), random.randint(0,WINDOW_H-PIG_H), PIG_HP, PIG_SPEED)
pig1.canBeDrawn()

pig2 = Pig(gameWindow, PIG_H, PIG_W, random.randint(0,WINDOW_W-PIG_W), random.randint(0,WINDOW_H-PIG_H), PIG_HP, PIG_SPEED)
pig2.canBeDrawn()

pig3 = Pig(gameWindow, PIG_H, PIG_W, random.randint(0,WINDOW_W-PIG_W), random.randint(0,WINDOW_H-PIG_H), PIG_HP, PIG_SPEED)
pig3.canBeDrawn()


cow1 = Cow(gameWindow, COW_H, COW_W, COW_START_X, COW_START_Y, COW_HP, COW_SPEED)
cow1.canBeDrawn()

cow2 = Cow(gameWindow, COW_H, COW_W, COW_START_X, COW_START_Y, COW_HP, COW_SPEED)
cow2.canBeDrawn()

cow3 = Cow(gameWindow, COW_H, COW_W, COW_START_X, COW_START_Y, COW_HP, COW_SPEED)
cow3.canBeDrawn()

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
            player.playerModel = pygame.image.load("Models/Player/player_model_moving_up.png")


    if keys[pygame.K_a] and player.rect.x > 0:
        futureRect.x -= PLAYER_MOVE_SPEED
        if GameObject.checkCollision(futureRect, player.rect) == None:
            player.playerModel = pygame.transform.flip(pygame.image.load("Models/Player/player_model_moving_l_r.png"), True, False)
            player.moveXAxis(-PLAYER_MOVE_SPEED)


    if keys[pygame.K_s] and player.rect.y <= WINDOW_H - player.rect.height:
        futureRect.y += PLAYER_MOVE_SPEED
        if GameObject.checkCollision(futureRect, player.rect) == None:
            player.playerModel = pygame.image.load("Models/Player/player_model_moving_down.png")
            player.moveYAxis(PLAYER_MOVE_SPEED)
    
    if keys[pygame.K_d] and player.rect.x <= WINDOW_W - player.rect.width:
        futureRect.x += PLAYER_MOVE_SPEED
        if GameObject.checkCollision(futureRect, player.rect) == None:
            player.playerModel = pygame.image.load("Models/Player/player_model_moving_l_r.png")
            player.moveXAxis(PLAYER_MOVE_SPEED)
    
    collidingObject = GameObject.checkCollision(player.interaRect, player.rect)

    if keys[pygame.K_f]:
        if collidingObject != None:
            player.interact(collidingObject)
    
    if keys[pygame.K_SPACE]:
        if collidingObject != None:
            player.attack(collidingObject)

            
    gameMap.draw() #map refresh
    player.draw() #player refresh
    
    #drawing trees
    tree_small1.draw()
    tree_small2.draw()
    tree_small3.draw()
    tree_big1.draw()
    tree_big2.draw()
    tree_big3.draw()
    tree_big4.draw()

    #drawing rocks
    rock_small1.draw()
    rock_small2.draw()
    rock_big1.draw()
    rock_big2.draw()


    #drawing monsters
    goblin1.draw()
    if GameObject.checkCollision(goblin1):
        goblin1.moving(random.randint(0,50), cow1.mobSPEED, COW_START_X, destination=random.randint(0,WINDOW_H-ORC_H))
    goblin2.draw()
    if GameObject.checkCollision(goblin2):
        goblin2.moving(random.randint(0,50), cow1.mobSPEED, COW_START_X, destination=random.randint(0,WINDOW_H-ORC_H))
    orc1.draw()
    if GameObject.checkCollision(orc1):
        orc1.moving(random.randint(0,50), cow1.mobSPEED, COW_START_X, destination=random.randint(0,WINDOW_H-ORC_H))
    orc2.draw()
    if GameObject.checkCollision(orc2):
        orc2.moving(random.randint(0,50), cow1.mobSPEED, COW_START_X, destination=random.randint(0,WINDOW_H-ORC_H))

    #drawing passive mobs (moving)
    #1.PIG
    pig1.draw()
    if GameObject.checkCollision(pig1):
        pig1.moving(random.randint(0,50), cow1.mobSPEED, PIG_START_X, destination=random.randint(0,WINDOW_H-PIG_H))
    pig2.draw()
    if GameObject.checkCollision(pig2):
        pig2.moving(random.randint(0,50), cow1.mobSPEED, PIG_START_X, destination=random.randint(0,WINDOW_H-PIG_H))
    pig3.draw()
    if GameObject.checkCollision(pig3):
        pig3.moving(random.randint(0,50), cow1.mobSPEED, PIG_START_X, destination=random.randint(0,WINDOW_H-PIG_H))
    
    #2.COW
    cow1.draw()
    if GameObject.checkCollision(cow1):
        cow1.moving(random.randint(0,50), cow1.mobSPEED, COW_START_X, destination=random.randint(0,WINDOW_H-COW_H))

    cow2.draw()
    if GameObject.checkCollision(cow2):
        cow2.moving(random.randint(0,50), cow1.mobSPEED, COW_START_X, destination=random.randint(0,WINDOW_H-COW_H))
    
    cow3.draw()
    if GameObject.checkCollision(cow3):
        cow3.moving(random.randint(0,50), cow1.mobSPEED, COW_START_X, destination=random.randint(0,WINDOW_H-COW_H))


    pygame.display.flip() #update the full display surface to the screen
    clock.tick(60) #tickrate/fps

#close pygame
pygame.quit()