import pygame
import sys
import time
import random
import math

pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.music.load('bang.mp3')
pygame.mixer.music.play()

size = width,height = 1200,800
speed = [0,0]
speed2 = [0,0]
speed3 = [0,0]
speed4 = [0,0]
speed5 = [1,1]
speedList = [2,2,2,2]
allspeed =2
color = [153, 153, 255]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("paddle1.png")
ball2 = pygame.image.load("paddle1.png")
ball3 = pygame.image.load("paddle1.png")
ball4 = pygame.image.load("paddle1.png")
realball = pygame.image.load("ball.png")

ball = pygame.transform.scale(ball,(150,60))
ball2 = pygame.transform.scale(ball2,(60,150))
ball3 = pygame.transform.scale(ball3,(60,150))
ball4 = pygame.transform.scale(ball4,(150,60))
realball = pygame.transform.scale(realball,(30,30))


ballrect = ball.get_rect()
ballrect2 = ball2.get_rect()
ballrect3 = ball3.get_rect()
ballrect4 = ball4.get_rect()
ballrect5 = realball.get_rect()



lasttime = 0
lasttime2 = 0
lasttime3 = 0
lasttime4 = 0
lasttime5 = 0

ballrect.x=400
ballrect.y=0
ballrect2.x=0
ballrect2.y=400
ballrect3.x=1140
ballrect3.y=400
ballrect4.x=600
ballrect4.y=740
ballrect5.x=600
ballrect5.y=400

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	keys = pygame.key.get_pressed()

	if  ballrect.right > width:
		if keys[pygame.K_y]:
			speed[0] = -speedList[0]
		else:
			speed[0] = 0

	elif  ballrect.left < 0:
		if keys[pygame.K_i]:
		
			speed[0] = speedList[0]
		else:
			speed[0] = 0
	else:
		if keys[pygame.K_y]:
			speed[0] = -speedList[0]
		elif keys[pygame.K_i]:
			speed[0] = speedList[0]
		else:
			speed[0] = 0
	
	
	if ballrect2.bottom > height:
		if keys[pygame.K_q]:
			speed2[1] = -speedList[1]
		else:
			speed2[1] = 0
	
	elif ballrect2.top < 0:
		if keys[pygame.K_a]:
			speed2[1] = speedList[1]
		else:
			speed2[1] = 0
	else:
		if keys[pygame.K_q]:
			speed2[1] = -speedList[1]
		elif keys[pygame.K_a]:
			speed2[1] = speedList[1]
		else:
			speed2[1] = 0
		
	if ballrect3.bottom > height:
		if keys[pygame.K_UP]:
			speed3[1] = -speedList[2]
		else:
			speed3[1] = 0
	
	elif ballrect3.top < 0:
		if keys[pygame.K_DOWN]:
			speed3[1] = speedList[2]
		else:
			speed3[1] = 0
	else:
		if keys[pygame.K_UP]:
			speed3[1] = -speedList[2]
		elif keys[pygame.K_DOWN]:
			speed3[1] = speedList[2]
		else:
			speed3[1] = 0

	if  ballrect4.right > width:
		if keys[pygame.K_b]:
			speed4[0] = -speedList[3]
		else:
			speed4[0] = 0

	elif  ballrect4.left < 0:
		if keys[pygame.K_m]:
			speed4[0] = speedList[3]
		else:
			speed4[0] = 0
	else:
		if keys[pygame.K_b]:
			speed4[0] = -speedList[3]
		elif keys[pygame.K_m]:
			speed4[0] = speedList[3]
		else:
			speed4[0] = 0
	if ballrect5.left<0 or ballrect5.right>width or ballrect5.bottom>height or ballrect5.top<0:
		ballrect5.x=600
		ballrect5.y=400
	
	if (pygame.time.get_ticks() - lasttime > 1):
		ballrect = ballrect.move(speed)
		lasttime = pygame.time.get_ticks() #Update the timer so that it happens again in another 1 ticks

	if (pygame.time.get_ticks() - lasttime2 > 1):
		ballrect2 = ballrect2.move(speed2)
		lasttime2 = pygame.time.get_ticks()

	if (pygame.time.get_ticks() - lasttime3 > 1):
		ballrect3 = ballrect3.move(speed3)
		lasttime3 = pygame.time.get_ticks() #Update the timer so that it happens again in another 1 ticks

	if (pygame.time.get_ticks() - lasttime4 > 1):
		ballrect4 = ballrect4.move(speed4)
		lasttime4 = pygame.time.get_ticks()
	if (pygame.time.get_ticks() - lasttime5 > 1):
		ballrect5 = ballrect5.move(speed5)
		lasttime5 = pygame.time.get_ticks()   

	if ballrect5.colliderect(ballrect) or ballrect5.colliderect(ballrect4): 
		speed5[0] = speed5[0]
		speed5[1] = -speed5[1]

	elif ballrect5.colliderect(ballrect2)or ballrect5.colliderect(ballrect3):
		speed5[0] = -speed5[0]
		speed5[1] = speed5[1]

	if (pygame.time.get_ticks() - lasttime > 1):
		color[0] = random.randint(0,255)	
		color[1] = random.randint(0,255)
		color[2] = random.randint(0,255)
		lasttime2 = pygame.time.get_ticks()

	screen.fill(color)
	screen.blit(ball,ballrect)
	screen.blit(ball2,ballrect2)
	screen.blit(ball3,ballrect3)
	screen.blit(ball4,ballrect4)
	screen.blit(realball,ballrect5)
	pygame.display.flip()