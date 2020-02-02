import pygame 
# initialize pygame engine
pygame.init()

# defines colors 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# initialize other variables  
screenSize = (800,600)
width = 50 
height = 50 
x = 0 
y = 0 
speed = 10 

# define objects 

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
	# black background 
	screen.fill(black)
	# create rectangle for player 
	player = pygame.draw.rect(screen, (255,0,0), (x, y, width, height))   
	# get_pressed fetches boolean dictionary of when keys are pressed
	keys = pygame.key.get_pressed() 
	# K_[direction] are the arrow keys, if statements retrieves if keys are being pressed down as either True or False 
	if keys[pygame.K_LEFT]:
		x -= speed 
	if keys[pygame.K_RIGHT]:
		x += speed 
	if keys[pygame.K_UP]:
		y -= speed 
	if keys[pygame.K_DOWN]:
		y += speed 

	# constrained the player so it can go off the screen 
	if x >= (screenSize[0]-width):
		x = screenSize[0]-width
	if y >= (screenSize[1]-height):
		y = screenSize[1]-height 
	if x <= 0:
		x = 0
	if y <= 0:
		y = 0

	## UPDATE SCREEN AND FPS  
	pygame.display.update()
	clock.tick(60)

# exit game engine after you exit the game 
pygame.quit()