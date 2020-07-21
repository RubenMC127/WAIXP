#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
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
