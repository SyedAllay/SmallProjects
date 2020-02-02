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

# condition
carryOn = True

# clock will be used to update how quickly screen updates (FPS)
clock = pygame.time.Clock()

# Main game loop, while carryOn is True, game will run 
while carryOn:
	# For loop get all events that happen
	for event in pygame.event.get():
		# pygame.QUIT is the event where you press x on the top left of title-bar
		if event.type == pygame.QUIT:
			carryOn = False 
			
	# GAME LOGIC



	# DRAWING STUFF 

	screen.fill(black)
	pygame.draw.rect(screen, red, [55, 200, 100, 70],0)

	## UPDATE SCREEN AND FPS  
	pygame.display.flip()
	clock.tick(60)

# exit game engine after you exit the game 
pygame.quit()