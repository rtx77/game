import pygame
import render
import socket
import client
import time

pygame.init()
render.Render.init("file.txt")
window = pygame.display.set_mode((1000, 600))
tank = pygame.Rect(0, 0, 20, 20)
enemy = pygame.Rect(0, 0, 20, 20)
render.Render.rects("99")

vel = 5

run = True
while run:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if not render.Render.intersection(tank):
        tank.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel

        if render.Render.intersection(tank):
            tank.x -= (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel

        tank.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel

        if render.Render.intersection(tank):
            tank.y -= (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel

    enemy.x, enemy.y = client.function(tank.x, tank.y)


    window.fill(0)
    pygame.draw.rect(window, (0, 255, 0), tank)
    pygame.draw.rect(window, (0, 255, 255), enemy)
    render.Render.render("99", window, (255, 255, 255))
    pygame.display.flip()

pygame.quit()
exit()
