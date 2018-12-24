import pygame

class projectile(object):

	def __init__(self,win,r=None,c=None,facing=None,char=None):
		self.win = win
		self.char = char
		self.x = self.char.hitbox[0]+self.char.hitbox[2] if self.char.right else self.char.hitbox[0]
		self.y = self.char.y+self.char.h//2
		self.r = r if r else 6
		self.color = c if c else (255,0,255)
		self.facing = 1 if self.char.right else -1
		self.vel = 8*self.facing
		self.dmg = 10

	def draw(self):
		self.win.drawProjectile(1,self.color,round(self.x),round(self.y),self.r)

	def position(self,coord):
		if coord == 'x':
			return self.x
		if coord == 'y':
			return self.y

	def hits(self,enemyChar): # Enemy for the one shooting
		if self.x + self.r > enemyChar.hitbox[0] and self.x - self.r < enemyChar.hitbox[0] + enemyChar.hitbox[2]:
			if self.y + self.r > enemyChar.hitbox[1] and self.y - self.r < enemyChar.hitbox[1] + enemyChar.hitbox[3]:
				return True
			return False
		return False


	def run(self):
		self.x += self.vel