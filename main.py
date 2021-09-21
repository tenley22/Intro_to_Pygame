import pygame
import math
import random


# create color constants
# RGB values meaning (red, green, blue) 255 is most 0 is none
# use color picker for more complex colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)
COLORS = [GREEN, RED, BLUE, BLACK]

# create math constants
PI = math.pi

# to convert from degrees tp radians is the angle * (pi/180)

# create game constants
SIZE = (700, 500)
# (width, height)
FPS = 60
# frames per second

########################################################
########################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('My First Pygame')

clock = pygame.time.Clock()


running = True
while running:

    # get all keyboard, mouse, joystick, etc events
    for event in pygame.event.get():

        # check for specific user event
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print('You Pressed a Key Down')
        elif event.type == pygame.KEYUP:
            print('You Pressed a Key Up')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('You Pressed the Mouse Button Down')

    # game logic goes here

    screen.fill(WHITE)

    # drawing goes here
    pygame.draw.rect(screen, GREEN, (55, 50, 20, 250))

    pygame.draw.arc(screen, BLACK, (255, 250, 200, 200), 0, 5*PI/4, width=5)

    for multiplier in range(10):
        color = random.choice(COLORS)
        pygame.draw.line(screen, color, (10 + 15*multiplier, 10), (50 + 15*multiplier, 50), width=5)

    pygame.display.flip()

    clock.tick(FPS)


# to be run after the main game loop
pygame.quit()