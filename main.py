#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from utils import load_image, WIDTH, HEIGHT 

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
