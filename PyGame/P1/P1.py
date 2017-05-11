"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/4YqIKncMJNs
 Explanation video: http://youtu.be/ONAK8VZIcI4
 Explanation video: http://youtu.be/_6c4o41BIms
"""

image_list = ["Jenny_attack1.png", "Jenny_attack2.png", "Jenny_attack3.png",
           "Jenny_attack4.png", "Jenny_attack5.png", "Jenny_attack6.png",
           "Jenny_attack7.png" ]
image_count = 0
 
import pygame
import time
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('CMSC 150 is cool')
 
clock = pygame.time.Clock()
 
# Before the loop, load the sounds:
 
# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
background_image = pygame.image.load("GameBG.png").convert()
player_image = pygame.image.load(image_list[image_count]).convert()
player_image.set_colorkey(BLACK)
 
done = False

now = time.time()
change = time.time() + 0.15
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = time.time()
    if(now >= change) :
        image_count = image_count + 1
        if(image_count == 7) :
            image_count = 0
        player_image = pygame.image.load(image_list[image_count]).convert()
        player_image.set_colorkey(BLACK)
        change = now + 0.15
 
    # Copy image to screen:
    screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0] - (player_image.get_width() / 2)
    y = player_position[1] - (player_image.get_height() / 2)
 
    # Copy image to screen:
    screen.blit(player_image, [x, y])
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
