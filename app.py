"""
Import the pygame and time modules
"""
# Pong v1
# Author: Ivan Windon

import pygame, time
pygame.init()

#variables
ScreenWidth = 800
ScreenHeight = 600
BallX = 100
BallY = 100
BallLocation = (BallX, BallY)
dx = 1
dy = 1

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


#create a window
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))

#Game Loop
GameRunning = True
while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False

    BallX = BallX + dx
    BallY = BallY + dy
    BallLocation = (BallX, BallY)

    if BallY > 600 or BallY < 0:
        dy = dy * -1

    if BallX > 800 or BallX < 0:
        dx = dx * -1

    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, BallLocation, 10, 5)
    pygame.draw.rect(screen, WHITE, (395, 0, 10, 600))

    pygame.display.update()
    time.sleep(0.01)

print("Game Over")
pygame.quit()
