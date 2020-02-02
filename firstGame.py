import pygame 
# initialize pygame engine
pygame.init()

# create player objct 
class player: 
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = 10

	def move(self):
		keys = pygame.key.get_pressed() 
		# K_[direction] are the arrow keys, if statements retrieves if keys are being pressed down as either True or False 
		if keys[pygame.K_LEFT]:
			self.x -= self.speed 
		if keys[pygame.K_RIGHT]:
			self.x += self.speed 
		if keys[pygame.K_UP]:
			self.y -= self.speed 
		if keys[pygame.K_DOWN]:
			self.y += self.speed 
		# Contrain movement so player can't leave screen
		if self.x >= (screenSize[0]-self.width):
			self.x = screenSize[0]-self.width
		if self.y >= (screenSize[1]-self.height):
			self.y = screenSize[1]-self.height
		if self.x <= 0:
			self.x = 0
		if self.y <= 0:
			self.y = 0

	def draw(self):
		# draw player 
		playerRect = pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.width, self.height))   

# defines colors 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# initialize other variables  
screenSize = (800,600)



# display screen
screen = pygame.display.set_mode(screenSize)
# initialize what is writeen at the top of the title-bar 
pygame.display.set_caption('My First Game')

# condition
carryOn = True

# clock will be used to update how quickly screen updates (FPS)
clock = pygame.time.Clock()
player1 = player(0,0,50,50)
# Main game loop, while carryOn is True, game will run 
while carryOn:
	# For loop get all events that happen
	for event in pygame.event.get():
		# pygame.QUIT is the event where you press x on the top left of title-bar
		if event.type == pygame.QUIT:
			carryOn = False 

	# black background 
	screen.fill(black)

	# draw player 
	draw = player1.draw()
	# allow movement
	movement = player1.move()
	## UPDATE SCREEN AND FPS  
	pygame.display.update()
	clock.tick(60)

# exit game engine after you exit the game 
pygame.quit()