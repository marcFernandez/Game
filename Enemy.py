import pygame

class Enemy(object):

	walkRight = [pygame.image.load('enemySprites/R1.png'),pygame.image.load('enemySprites/R2.png'),
				 pygame.image.load('enemySprites/R3.png'),pygame.image.load('enemySprites/R4.png'),
				 pygame.image.load('enemySprites/R5.png'),pygame.image.load('enemySprites/R6.png'),
				 pygame.image.load('enemySprites/R7.png'),pygame.image.load('enemySprites/R8.png'),
				 pygame.image.load('enemySprites/R9.png')]
	walkLeft = [pygame.image.load('enemySprites/L1.png'),pygame.image.load('enemySprites/L2.png'),
				pygame.image.load('enemySprites/L3.png'),pygame.image.load('enemySprites/L4.png'),
				pygame.image.load('enemySprites/L5.png'),pygame.image.load('enemySprites/L6.png'),
				pygame.image.load('enemySprites/L7.png'),pygame.image.load('enemySprites/L8.png'),
				pygame.image.load('enemySprites/L9.png')]
	char = pygame.image.load('enemySprites/D1.png')


	def __init__(self,x,y,w,h,vel,win,ent=None,name=None):
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
		self.maxJumpCount = 10
		self.jumpCount = self.maxJumpCount
		self.isAlive = True
		self.moveNumber = 30
		self.isEnemy = True
		self.hitbox = (self.x + 15, self.y + 12, 33, 50)
		self.hp = 100
		self.name = name if name else 'Salamo'
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
		
		self.hitbox = (self.x + 15, self.y + 12, 33, 50)
		if self.hitboxShown:
			self.win.drawEntity(0,self.hitbox[0],self.hitbox[1],self.hitbox[2],self.hitbox[3])

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
			self.isJumping = True
			neg = 1
			if self.jumpCount < 0:
				neg = -1
			if self.y - neg*(self.jumpCount**2)*.5 > 0:
				self.y -= neg*(self.jumpCount**2)*.5
				self.jumpCount -= 1
			else:
				self.jumpCount = -self.jumpCount-1
		else:
			self.isJumping = False
			self.jumpCount = 10

	def run(self):
		"""
		if self.left:
			if self.moveNumber - 1 > 0:
				self.moveNumber -= 1
				self.moveLeft()
			else:
				self.moveNumber = 30
				self.moveRight()
		else:
			if self.moveNumber - 1 > 0:
				self.moveNumber -= 1
				self.moveRight()
			else:
				self.moveNumber = 30
				self.moveLeft()
		"""
		if self.hp <= 0:
			self.die()

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