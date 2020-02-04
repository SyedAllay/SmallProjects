import pygame 
import random 
# initialize pygame engine
pygame.init()

# defines colors 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# initialize other variables  
screenSize = (800,600)
holeSize = 100 
playerSize = 50 
score = 0 

# display screen
screen = pygame.display.set_mode(screenSize)
# initialize what is writeen at the top of the title-bar 
pygame.display.set_caption('My First Game')

# condition
carryOn = True

# clock will be used to update how quickly screen updates (FPS)
clock = pygame.time.Clock()
# initialize a player 

class enemyWall:

    def __init__(self,screenSize,playerSize, holeSize):
        self.screenWidth = screenSize[0]
        self.screenHeight = screenSize[1] 
        self.x = 0
        self.y = 0
        self.x1 = 300
        self.playerSize = playerSize 
        self.holeSize = holeSize 
        self.holeHeight = playerSize

    # moves hole to the left
    def moveR(self):
        if self.x1 <= self.screenWidth:
            self.x1 += 5
        else:
            self.x1 = -self.holeSize
    # moves hole to the right 
    def moveL(self):
        if self.x1 >= -self.holeSize:
            self.x1 -= 5
        else:
            self.x1 = self.screenWidth + self.holeSize
    # moves hole randomly after every reset to the top
    def moveRan(self):
        if self.y == -self.playerSize:
            self.x1 = random.randint(0,self.screenWidth-self.holeSize)
        if self.y <= self.screenHeight:
            self.y += 5
        else:
            self.y = -self.playerSize

    def draw(self):
        # draw hole and bar 
        EnemyRec = pygame.draw.rect(screen, (0,255,0), (self.x, self.y, self.screenWidth, self.playerSize)) 
        EnemyRecHole = pygame.draw.rect(screen, (0,0,0), (self.x1, self.y, self.holeSize, self.holeHeight)) 

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

player1 = player(400,400,50,50)
enemy = enemyWall(screenSize,playerSize,holeSize)
# Main game loop, while carryOn is True, game will run 
while carryOn:
    # For loop get all events that happen
    for event in pygame.event.get():
        # pygame.QUIT is the event where you press x on the top left of title-bar
        if event.type == pygame.QUIT:
            carryOn = False 
    # black background 
    screen.fill(black)
    def collision(playerSize,holeSize,player1,enemy):
        if player1.y <= (enemy.y + playerSize) and enemy.y <= player1.y:
            if (player1.x <= enemy.x1):
                return True
            if ((player1.x + playerSize) >= (enemy.x1 + holeSize)):
                return True
            else:
                return False
    # draw player,enemy and allow for movement
    drawEnemy = enemy.draw()
    moveEnemy = enemy.moveRan()
    draw = player1.draw()
    movement = player1.move()
    if collision(playerSize,holeSize,player1,enemy):
        carryOn = False 
    ## UPDATE SCREEN AND FPS  
    pygame.display.update()
    clock.tick(60)

# exit game engine after you exit the game 
pygame.quit()