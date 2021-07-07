import pygame
import math
import random
pygame.init()
def sin(self,value):
  math.sin(self,value)
Width = 900
Height = 650
pygame.display.set_mode((Width,Height))
#Spaceship#
spaceship = pygame.image.load("spaceship.png")
spaceshipx = Width/2
spaceshipy = Height/2
speedx = 0
speedy = 0
leftright = 0
updown = 0
def moveX(joystickx):
  speedx = speedx + 0.9 * joystickx
  speedx = 0.9 * speedx
  spaceshipx = spaceshipx + speedx
def moveY(joysticky):
  speedy = speedy + 0.9 * joysticky
  speedy = 0.9 * speedy
  spaceshipy = spaceshipy + speedy
def UpdateSpaceship(x,y):
  screen.blit(spaceship,(x,y))
#laser#
laser = pygame.image.load("laser.png")
laserx = 0
lasery = 0
def Shoot():
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        laserx = spaceshipx
        lasery = spaceshipy
        screen.blit(laser,(laserx,lasery))
#LEMON#
lemon = pygame.image.load("lemon.png")
lemonx = 0
lemony = 0
direction = 0
def NextEnemy(enemy):
  direction = random.randint(-180,180)
  lemonx = lemonx + -350 * math.sin(direction)
  lemony = lemony + -350 * math.cos(direction)
  if enemy == 1:
    hp = 5
  if enemy == 2:
    hp = 7
  screen.blit(lemon,(lemonx,lemony))
#Gameloop#
pygame.display.set_caption("World Space Shooter")
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        leftright = leftright + 1
        if leftright > 1:
          leftright = 1
        elif leftright < -1:
          leftright = -1
      if event.key == pygame.K_RIGHT:
        leftright = leftright - 1
        if leftright > 1:
          leftright = 1
        elif leftright < -1:
          leftright = -1
  UpdateSpaceship(spaceshipx,spaceshipy)
  Shoot()
  NextEnemy(1)
