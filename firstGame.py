import pygame 
# initialize pygame engine
pygame.init()

# defines colors 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# initialize other variables  
screenSize = (800,800)
width = 50 
height = 50 
x = 0 
y = 0 

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
	screen.fill(black)
	player = pygame.draw.rect(screen, red, [x, y, width, height],0)
	
	keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

	if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
		x -= 10
	if keys[pygame.K_RIGHT]:
		x += 10 
	if keys[pygame.K_UP]:
		y -= 10
	if keys[pygame.K_DOWN]:
		y += 10 
	pygame.draw.rect(screen, (255,0,0), (x, y, width, height))   


	## UPDATE SCREEN AND FPS  
	pygame.display.update()
	clock.tick(60)

# exit game engine after you exit the game 
pygame.quit()