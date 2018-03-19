from Board.Board import Board
from AdventureGames.A1 import *
import Actor
import pygame
import sys

#Initialize all internal modules
pygame.init()

size = width, height = Board.size

#Inititing zombie
game = A1()

#Setting background
green = 100,255,100
background_img = pygame.image.load(Board.grfx)

#Create surface object (represents the displayed graphics)
screen = pygame.display.set_mode(size)

#Gives us a rect if we want
#zombie_rect = zombie_img.get_rect(center = zombie.position())#center = )

while True:
    #Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #Erase screen
    screen.blit(background_img,(0,0))

    #Move image and draw on screen
    game.run()
    actors = game.getActors()

    for zombie in actors[0]:
        screen.blit(pygame.image.load(zombie.grfx),zombie.position())
    for plant in actors[1]:
        screen.blit(pygame.image.load(plant.grfx),plant.position())
    """
    for zombie in zombies:
        if(zombie[0].isDead()):
            zombies.remove(zombie)
        else:
            if plants:
                if(zombie[0].isBlocked(plants[0][0])):
                    zombie[0].attack(plants[0][0])
                else:
                    zombie[0].move()
            else:
                zombie[0].move()
            
            screen.blit(zombie[1],zombie[0].position())

    for plant in plants:
        if(plant[0].isDead()):
            plants.remove(plant)
        else:
            screen.blit(plant[1],plant[0].position())"""

    #makes everything we just drew visible
    #this strategy makes sure we only see completed stuff
    pygame.display.flip()