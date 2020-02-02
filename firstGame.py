import pygame 
# initialize pygame engine
pygame.init()

# defines colors 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# initialize screen size 
screenSize = (800,800)
# display screen
screen = pygame.display.set_mode(screenSize)
# initialize what is writeen at the top of the title-bar 
pygame.display.set_caption('My First Game')