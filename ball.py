#importing required modules
import pygame
from random import randint
#initializing the color
BLACK = (0, 0, 0)
#start of class Ball
class Ball(pygame.sprite.Sprite):    
	#initialization of the ball
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)
		pygame.draw.rect(self.image, color, [0, 0, width, height], 0, 100)
		self.velocity = [randint(6, 6), randint(-7, 7)]
		self.rect = self.image.get_rect()
	#updates the ball and its movement
	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]
	#boounces the ball
	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-4, 4)