#importing pygame, ball, and paddle
import pygame
from paddle import Paddle
from ball import Ball

#initializing pygame
pygame.init()

#Colors!!!
BLACK = (0,0,0)        
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

#Setting the screen size and caption
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong by Krishna Meda")

bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 45)

#creating a paddle and setting it on one side of the screen
paddleA = Paddle(RED, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

#creating another paddle and setting it on the other side of the screen
paddleB = Paddle(BLUE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

#creating a ball and setting it in the center just above the center of the paddles
ball = Ball(GREEN,10,10)
ball.rect.x = 345
ball.rect.y = 195

#adding the ball and both paddles into a pygame sprite group aka a list (kind of...)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#more pygame inetialization
carryOn = True
clock = pygame.time.Clock()

#initializing the scores!!!
scoreA = 0
scoreB = 0

#starting the main program loop
while carryOn:
	#to exit the game click x or the close button
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				carryOn=False

	#how to move: w&s for Blue up&down arrow keys for Red
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		paddleA.moveUp(5)
	if keys[pygame.K_s]:
		paddleA.moveDown(5)
	if keys[pygame.K_UP]:
		paddleB.moveUp(5)
	if keys[pygame.K_DOWN]:
		paddleB.moveDown(5)
	all_sprites_list.update()
		
	#scoring system
	if ball.rect.x >= 690:
		scoreA += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.x <= 0:
		scoreB += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.y > 490:
		ball.velocity[1] = -ball.velocity[1]
	if ball.rect.y < 0:
		ball.velocity[1] = -ball.velocity[1]     

	#make ball bounce upon contact with either paddle
	if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
		ball.bounce()
	
	#color background black and dras a line to mark the half way mark of the board
	screen.fill(BLACK)
	pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
	
	#draw all of the sprites
	all_sprites_list.draw(screen) 
	
	#announcing who won the game (first to 21 wins)
	if scoreA >= 21 and scoreB < scoreA:
		screen.fill(BLACK)
		font = pygame.font.Font(None, 75)
		txt = "Player A wins"
		text = font.render(txt, 1, WHITE)
		screen.blit(text, (200,10))
	elif scoreB >= 21 and scoreA < scoreB:
		screen.fill(BLACK)
		font = pygame.font.Font(None, 75)
		txt = "Player B wins"
		text = font.render(txt, 1, WHITE)
		screen.blit(text, (200,10))
	else:
		font = pygame.font.Font(None, 74)
		text = font.render(str(scoreA), 1, WHITE)
		screen.blit(text, (250,10))
		text = font.render(str(scoreB), 1, WHITE)
		screen.blit(text, (420,10))
	#update the screen
	pygame.display.flip()
    
	#even more stuff required by python
	clock.tick(60)

#end pygame 
pygame.quit()
