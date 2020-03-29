# imports the library
import math

import random
import pygame


# initializes pygame class

pygame.init()



# for configuring display size

screen = pygame.display.set_mode((700, 500))
# background
background = pygame.image.load('galaxy.jpg')


# Title of game

pygame.display.set_caption("Space Invaders")

# Put the icon for the game

gameicon = pygame.image.load('alien.png')
pygame.display.set_icon(gameicon)
pygame.display.update()

#Game Over
over = pygame.font.Font("text.ttf", 60)

def game_over():
    game = over.render("GAME OVER",True,(255,255,255))
    screen.blit(game,(150,200))

# player (spaceship)

playerimg = pygame.image.load('spaceship.png')
playerX = 285
playerY = 390
playerX_change = 0

# bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 390
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('ufo (1).png'))
    enemyX.append(random.randint(10, 650))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(30)



score =0 
font = pygame.font.Font("text.ttf", 20)
scoreX= 10
scoreY =10
#function for score
def show_score(x,y):
    text = font.render("SCORE:"+str(score),True,(255,255,255))
    screen.blit(text,(x,y))
# function for bullet_

def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 20, y + 8))

#funcion for knowing if bullet hit enemy
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
# function for player


def player(x,y):
    screen.blit(playerimg, (x, y))

# function for enemy

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

# keeps the screen running

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire(bulletX,  bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    playerX += playerX_change
    
  
    
    if bulletY<=0:
      bulletY = 390
      bullet_state="ready"
    if bullet_state is "fire":
      fire(bulletX, bulletY)
      bulletY -= bulletY_change
    
#checking boundaries for spaceship 
    if playerX <= 0:
        playerX = 10
    elif playerX >= 620:
        playerX = 620
#checking boundaries for enmy
    for i in range(num_of_enemies):
        if enemyY[i]> 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 650:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i] 
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY= 390
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(10, 650)
            enemyY[i] = random.randint(50, 150) 
        enemy(enemyX[i], enemyY[i],i)           

      
    player(playerX, playerY)
    show_score(scoreX, scoreY)
    pygame.display.update() 