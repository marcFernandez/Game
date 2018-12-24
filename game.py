import pygame
import Window,player,Enemy,Entity,projectile

pygame.init()

clock = pygame.time.Clock()

win = Window.Window(640,480,'WindowTitle')

ent = Entity.Entity(150,400,150,10,win)
entList = [ent]


playerx = 64
playery = 480 - 64 - 28
playerw,playerh,playervel = 64,64,5

player = player.player(playerx,playery,playerw,playerh,playervel,win,ent)
enemy = Enemy.Enemy(playerx+50,playery+2,playerw,playerh,playervel,win)

enemyBulletList = []
playerBulletList = []

bulletTimer = 0

run = True
while run:

	clock.tick(27)

	bulletTimer += 1
	if bulletTimer == 5:
		bulletTimer = 0

	enemy.run()
	player.run()

	for bullet in enemyBulletList:
		bullet.run()
		if bullet.position('x') < 0 or bullet.position('x') > 640 or bullet.hits(player):
			if bullet.hits(player):
				player.hp -= bullet.dmg
				print('Player hit! Player hp remaining:',player.hpbar())
			enemyBulletList.remove(bullet)

	if not player.isAlive:
		print('Player dead, so sad :( (kappa)')
		run = False

	for bullet in playerBulletList:
		bullet.run()
		if bullet.position('x') < 0 or bullet.position('x') > 640 or bullet.hits(enemy):
			if bullet.hits(enemy):
				enemy.hp -= bullet.dmg
				print('Enemy hit! Enemy hp remaining:',enemy.hpbar())
			playerBulletList.remove(bullet)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	mouse = pygame.mouse.get_pressed()

	if mouse[0] and len(enemyBulletList) < 3 and bulletTimer == 0: # Left button
		enemyBulletList.append(projectile.projectile(win,None,None,1,enemy))
	
	if mouse[2] and len(playerBulletList) < 3 and bulletTimer == 0: # Right button
		playerBulletList.append(projectile.projectile(win,None,None,1,player))

	if keys[pygame.K_ESCAPE]:
		run = False

	if keys[pygame.K_LEFT]:
		player.moveLeft()
	elif keys[pygame.K_RIGHT]:
		player.moveRight()
	else:
		player.standing()

	if not player.isJumping:
		if keys[pygame.K_UP]: # SPACE]:
			player.isJumping = True

		

	else:
		player.jump()

	
	# Enemy movement with w,a,s,d keys

	if keys[pygame.K_a]:
		enemy.moveLeft()
	elif keys[pygame.K_d]:
		enemy.moveRight()
	else:
		enemy.standing()

	if keys[pygame.K_h]:
		player.hitboxShown = not player.hitboxShown
		enemy.hitboxShown = not enemy.hitboxShown 

	if not enemy.isJumping:	
		if keys[pygame.K_w]:
			enemy.isJumping = True
	else:
		enemy.jump()

	if keys[pygame.K_k] and enemy.isAlive:
		enemy.die()
		print("Enemy death!")

	if keys[pygame.K_c]:
		entList[0].change = not entList[0].change
		print('Color changing')

	if enemy.isAlive:
		win.update(player,enemy,entList,enemyBulletList,playerBulletList)
	else:
		win.update(player,None,entList,enemyBulletList,playerBulletList)

print('Credit: 0, insert coin')
pygame.quit()