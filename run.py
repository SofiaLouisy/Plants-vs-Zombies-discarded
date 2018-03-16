from Zombie import Zombie
from Plant import Plant
from Board import Board
import pygame
import sys
#pygame.examples.aliens

#Initialize all internal modules
pygame.init()


size = width, height = Board.size

#Inititing zombie
zombie = Zombie()
plant = Plant()

#Setting background
green = 100,255,100
background_img = pygame.image.load(Board.grfx)

#Create surface object (represents the displayed graphics)
screen = pygame.display.set_mode(size)

#Creates surface with data from image
zombie_img = pygame.image.load(zombie.grfx)
plant_img = pygame.image.load(plant.grfx)

print(plant.pos())

#Gives us a rect if we want
#zombie_rect = zombie_img.get_rect(center = zombie.pos())#center = )

while True:
    #Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #Erase screen
    screen.blit(background_img,(0,0))

    #Move image and draw on screen


    if(plant.isBlocking(zombie)):
        screen.blit(zombie_img,zombie.pos())
    else:
        screen.blit(zombie_img,zombie.move())
    
    screen.blit(plant_img,plant.pos())

    #makes everything we just drew visible
    #this strategy makes sure we only see completed stuff
    pygame.display.flip()