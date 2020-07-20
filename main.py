#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except Exception as e:
        raise e

    image = image.convert()

    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)

    return image


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")

    background_image = load_image("images/background.png")

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

        screen.blit(background_image, (0,0))
        pygame.display.flip()

    return 0


if __name__ == '__main__':
    pygame.init()
    main()
