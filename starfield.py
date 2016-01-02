#!/usr/bin/env python

import pygame
import random
from collections import namedtuple

width = 1024
height = 768


# Pixel = namedtuple('Pixel', ['x', 'y', 'xa', 'ya'], verbose=False)

class Pixel:
    def __init__(self, x, y, xa=0, ya=0):
        self.x = x
        self.y = y
        self.xa = xa
        self.ya = ya

    def move(self, width, height):
        self.x += self.xa
        self.y += self.ya

        if self.x <= 0 or self.x >= width:
            self.x = random.randint(0, width - 1)
            self.y = random.randint(0, height - 1)
            self.star_direction(width, height)

        if self.y <= 0 or self.y >= height:
            self.x = random.randint(0, width - 1)
            self.y = random.randint(0, height - 1)
            self.star_direction(width, height)

    def star_direction(self, width, height):

        if self.x < width / 2 and self.y < height / 2:
            self.xa = -1
            self.ya = -1

        if self.x >= width / 2 and self.y >= height / 2:
            self.xa = 1
            self.ya = 1

        if self.x > width / 2 and self.y < height / 2:
            self.xa = 1
            self.ya = -1

        if self.x < width / 2 and self.y > height / 2:
            self.xa = -1
            self.ya = 1


def setup():
    data = []
    for n in range(0, 100):
        pixel = Pixel(random.randint(0, width - 1),
                      random.randint(0, height - 1), 0, 0)
        pixel.star_direction(height, width)
        data.append(pixel)

    return data


screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
running = True
starfield = setup()
black = (0, 0, 0)

while running:
    screen.fill(black)
    for pixel in starfield:
        pixel.move(width, height)

        x = pixel.x
        y = pixel.y

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        screen.set_at((x, y), (red, green, blue))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(240)
