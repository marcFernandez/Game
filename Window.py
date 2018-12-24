import pygame

class Window():

	# Platform in (150,400) , (300,410)

	def __init__(self,weight,height,caption):
		self.w = weight
		self.h = height
		self.caption = caption
		self.bgList = [pygame.image.load('backgrounds/BG0.png'),pygame.image.load('backgrounds/BG0_with_platform.png')]
		self.win = pygame.display.set_mode((self.w,self.h))
		self.font = pygame.font.SysFont('comicsans',30,False,False) # (font,size,bold,italics)
		pygame.display.set_caption('WindowTitle')
		pygame.display.update()

	def update(self,player,enemy=None,entityList=None,enemyProjectileList=None,allyProjectileList=None):
		self.bg()
		# The characters will appear on the window with the same order than drawn. So, the last
		# char drawn will be above all others and so on.
		player.draw()

		if enemy:
			enemy.draw()
		if entityList:
			for ent in entityList:
				ent.draw()
		if enemyProjectileList:
			for proj in enemyProjectileList:
				proj.draw()
		if allyProjectileList:
			for proj in allyProjectileList:
				proj.draw()

		text = self.font.render('Player hp: '+player.hpbar(),1,(0,0,0))
		self.win.blit(text,(10,10))
		pygame.display.update()

	def bg(self):
		self.win.blit(self.bgList[1], (0,0))

	def drawChar(self,sprite,x,y):
		self.win.blit(sprite,(x,y))

	def drawEntity(self,entType,x,y,w,h):
		pygame.draw.rect(self.win, (255,0,0),(x,y,w,h),2)

	def drawProjectile(self,projectileType,c,x,y,r):
		pygame.draw.circle(self.win,c,(x,y),r)

	def getWindow(self):
		return pygame.display.set_mode((self.w,self.h))
