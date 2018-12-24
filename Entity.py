import pygame

class Entity(object):

	def __init__(self,x,y,w,h,win):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.win = win
		self.change = False
		self.isEnemy = False

	def isColliding(self,char):
		if char.base() == self.y - 5 and char.x < self.x + self.w and char.basewidth() > self.x:
				print('Colliding!')
				return True
		return False

	def draw(self):
		if self.change:
			# We here assume that type 1 == rectangle
			self.win.drawEntity(1,self.x,self.y,self.w,self.h)