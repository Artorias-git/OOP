import pygame as pg
from pygame.locals import (QUIT)
import math

class Planet():
    def __init__(self, radius, speed, place):
        self.radius = radius/2000
        self.speed = speed
        self.placeX = place/5.5
        self.placeY = y

    def creat(self):
        color = (255, 255, 255)
        a = (360 / self.speed * count) / 57.3
        x1 = self.placeX * math.cos(a)
        y1 = self.placeY - self.placeX * math.sin(a)
        pg.draw.circle(screen, color, (x1 + x, y1), self.radius)

SCREEN_WIDTH = 1000
x = SCREEN_WIDTH/2
SCREEN_HEIGHT = 1000
y = SCREEN_HEIGHT/2
FPS = 365

pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Solar system")
clock = pg.time.Clock()

year = 365.24
Mercury = Planet(2439, 88, 58)
Venus = Planet(6051, 224.7, 108.9)
Earth = Planet (6378, 365.24, 149.6)
Mars = Planet(3389, 686.9, 228)
Jupiter = Planet(71492, 11.89 * year, 741)
Saturn = Planet(60300, 29.46 * year, 1430)
Uranus = Planet(25360, 84 * year, 1800)          # должно быть 2800 в place но это не влазит поэтому вычел 1000М км, бывает
Neptune = Planet(24622, 164.79 * year, 2500)     # должно быть 4500 в place но это не влазит поэтому вычел 2000М км, бывает




count = 0
running = True
while running:
    clock.tick(FPS)
    pg.draw.circle(screen, 	(255, 255, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 3)
    Mercury.creat()
    Venus.creat()
    Earth.creat()
    Mars.creat()
    Jupiter.creat()
    Saturn.creat()
    Uranus.creat()
    Neptune.creat()
    pg.display.update()
    screen.fill((0, 0, 0))
    count += 1
    for event in pg.event.get():
        if event.type == QUIT:
            # print(event.type)
            running = False
