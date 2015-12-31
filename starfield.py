#!/usr/bin/env python

import pygame
import random
from collections import namedtuple

width = 1024
height = 768
Pixel = namedtuple('Pixel', ['x', 'y'], verbose=False)


def setup():
    field = []
    for n in range(0, 1000):
        field.append(Pixel(random.randint(0, width - 1),
                            random.randint(0, height - 1)))

    return field


def move_star(height, width, pixel):
    pass


screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
running = True
starfield = setup()

while running:

    for x, y in starfield:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        screen.set_at((x, y), (red, green, blue))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(240)
