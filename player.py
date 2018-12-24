import pygame

class player(object):

	walkRight = [pygame.image.load('playerSprites/R1.png'),pygame.image.load('playerSprites/R2.png'),
				 pygame.image.load('playerSprites/R3.png'),pygame.image.load('playerSprites/R4.png'),
				 pygame.image.load('playerSprites/R5.png'),pygame.image.load('playerSprites/R6.png'),
				 pygame.image.load('playerSprites/R7.png'),pygame.image.load('playerSprites/R8.png'),
				 pygame.image.load('playerSprites/R9.png')]
	walkLeft = [pygame.image.load('playerSprites/L1.png'),pygame.image.load('playerSprites/L2.png'),
				pygame.image.load('playerSprites/L3.png'),pygame.image.load('playerSprites/L4.png'),
				pygame.image.load('playerSprites/L5.png'),pygame.image.load('playerSprites/L6.png'),
				pygame.image.load('playerSprites/L7.png'),pygame.image.load('playerSprites/L8.png'),
				pygame.image.load('playerSprites/L9.png')]
	char = pygame.image.load('playerSprites/standing.png')


	def __init__(self,x,y,w,h,vel,win,entity,name=None):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vel = vel
		self.win = win
		self.right = False
		self.left = False
		self.isStanding = False
		self.walkCount = 0
		self.isJumping = False
		self.maxJumpCount = 7
		self.jumpCount = self.maxJumpCount
		self.isEnemy = False
		self.ent = entity
		self.hitbox = (self.x + 14, self.y + 13, 35, 51)
		self.hp = 100
		self.name = name if name else 'Pep'
		self.isAlive = True
		self.hitboxShown = False

	def draw(self):
		if self.walkCount + 1 >= 27:
			self.walkCount = 0
		if not self.isStanding:
			if self.left:
				self.win.drawChar(self.walkLeft[self.walkCount//3], self.x,self.y)
				self.walkCount += 1
			elif self.right:
				self.win.drawChar(self.walkRight[self.walkCount//3], self.x,self.y)
				self.walkCount += 1
		else:
			"""
			# Code to have a standing position
			self.win.drawChar(self.char, self.x,self.y)
			"""
			if self.right:
				self.win.drawChar(self.walkRight[0], self.x,self.y)
			else:
				self.win.drawChar(self.walkLeft[0], self.x,self.y)
		
		self.hitbox = (self.x + 14, self.y + 13, 35, 51)
		if self.hitboxShown:
			self.win.drawEntity(0,self.hitbox[0],self.hitbox[1],self.hitbox[2],self.hitbox[3])

	def run(self):
		print(self.hitbox[1]+self.hitbox[3])
		if self.hp <= 0:
			self.die()
		#if not self.ent.isColliding(self) and self.base() < 480 - 64 - 29:
		#	self.moveDown()

	def die(self):
		self.isAlive = False

	def hpbar(self):
		hpbar = '|'
		for _ in range(self.hp//10):
			hpbar += '#'
		if self.hp//10 != 10:
			for _ in range(10-self.hp//10):
				hpbar += ' '
		hpbar += '|'
		return hpbar

	def standing(self):
		"""
		# Code to have a standing position
		self.left = False
		self.right = False
		"""
		self.isStanding = True
		# self.walkCount = 0

	def moveLeft(self):
		self.left = True
		self.right = False
		self.isStanding = False
		if self.hitbox[0] > self.vel:
			self.x -= self.vel

	def moveRight(self):
		self.right = True
		self.left = False
		self.isStanding = False
		if self.hitbox[0] < self.win.w - self.hitbox[2] - self.vel:
			self.x += self.vel

	def moveUp(self):
		if self.y > 0:
			self.y -= self.vel

	def moveDown(self):
		if self.y < self.win.w - self.h:
			self.y += self.vel

	def base(self):
		return self.hitbox[1] + self.hitbox[3]

	def basewidth(self):
		return self.hitbox[0] + self.hitbox[2]

	def jump(self):
		if self.jumpCount >= -self.maxJumpCount and self.isJumping:
			
			neg = 1 if not self.jumpCount < 0 else -1

			if self.isJumping and self.y - neg*(self.jumpCount**2)*0.5 > 0:
				self.y -= neg*(self.jumpCount**2)*0.5
				self.jumpCount -= 1
			else:
				self.jumpCount = -self.jumpCount-1
		else:
			self.isJumping = False
			self.jumpCount = self.maxJumpCount
			