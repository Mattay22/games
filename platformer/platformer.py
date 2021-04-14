import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screem_height = 1000
#### (https://www.youtube.com/watch?v=Ongc4EVqRjo&t=86s)4:30, 9:00
screen = pygame.display.set_mode((screen_width, screem_height))
pygame.display.set_caption('Platformer')

#define game variables
tile_size = 200


#load images
bg_img = pygame.image.load('background.png')

class World():
    def __init__(self, data):

        #load images
        



run = True
while run:

    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()


