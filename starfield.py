#!/usr/bin/env python

import pygame
import random

WIDTH = 1024
HEIGHT = 768


# Pixel = namedtuple('Pixel', ['x', 'y', 'xa', 'ya'], verbose=False)

class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)

    def move(self, width, height):
        self.y = self.y + self.dy
        self.x = self.x + self.dx

        if self.x <= 0 or self.x >= width:
            self.x = width / 2 + random.randint(-20, 20)
            self.y = height / 2 + random.randint(-10, 10)

        if self.y <= 0 or self.y >= height:
            self.x = width / 2 + random.randint(-20, 20)
            self.y = height / 2 + random.randint(-10, 10)


def setup():
    data = []
    for n in range(0, 1000):
        pixel = Pixel(WIDTH / 2, HEIGHT / 2)
        data.append(pixel)

    return data


pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('starfield')

print pygame.display.Info()

clock = pygame.time.Clock()
running = True
starfield = setup()
black = (0, 0, 0)

s = pygame.Surface((20, 20))  # the size of your rect
s.set_alpha(128)  # alpha level
s.fill((0, 0, 0))  # this fills the entire surface

while running:
    screen.fill(black)
    for pixel in starfield:
        pixel.move(WIDTH, HEIGHT)

        x = int(round(pixel.x))
        y = int(round(pixel.y))

        red = 250  # random.randint(0, 255)
        green = 250  # random.randint(0, 255)
        blue = 250  # random.randint(0, 255)

        screen.set_at((x, y), (red, green, blue))
        screen.blit(s, (WIDTH / 2 - 10, HEIGHT / 2 - 10))  # (0,0) are the top-left coordinates
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(240)
