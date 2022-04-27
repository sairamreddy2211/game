import pygame 
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breakin' Bricks")

#bat

bat = pygame.image.load('./assets/paddle.png').convert_alpha()
bat_rect = bat.get_rect()


game_over  = False 

while not game_over:
    screen.fill((0,0,0))
    screen.blit(bat, bat_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    pygame.display.update()
    
    