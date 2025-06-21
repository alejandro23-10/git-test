import math

import pygame
from Direction import Dir
from Projectile import Projectile

SCALE = 3
BOUND_X = [0, 1280]
BOUND_Y = [0, 720]
SIZE = 32


def get_color(num):
    if num == 1:
        return "red"
    if num == 2:
        return "blue"


class Player:
    def __init__(self, pos, screen, dt, number):
        self.pos = pos
        self.dir = Dir.UP
        self.screen = screen
        self.image = pygame.transform.scale_by(pygame.image.load('assets/spin-sheet.png'), SCALE)
        self.dt = dt
        self.created_projectiles = []
        self.last_shot = 0
        self.number = number
        self.color = get_color(number)
        self.health = 100

    def check_boundaries(self):
        if self.pos[0] < BOUND_X[0]:
            self.pos = (BOUND_X[0], self.pos[1])
        if self.pos[0] > BOUND_X[1] - (SIZE * SCALE):
            self.pos = (BOUND_X[1] - (SIZE * SCALE), self.pos[1])
        if self.pos[1] < BOUND_Y[0]:
            self.pos = (self.pos[0], BOUND_Y[0])
        if self.pos[1] > BOUND_Y[1] - (SIZE * SCALE):
            self.pos = (self.pos[0], BOUND_Y[1] - (SIZE * SCALE))

    def move(self, keys, delta):
        if (keys[pygame.K_w] and keys[pygame.K_d] and self.number == 1) or (keys[pygame.K_UP] and keys[pygame.K_RIGHT] and self.number == 2):
            self.pos = (self.pos[0] + delta * self.dt / math.sqrt(2), self.pos[1] - delta * self.dt / math.sqrt(2))
            self.dir = Dir.UP_RIGHT
        elif (keys[pygame.K_s] and keys[pygame.K_d] and self.number == 1) or (keys[pygame.K_DOWN] and keys[pygame.K_RIGHT] and self.number == 2):
            self.pos = (self.pos[0] + delta * self.dt / math.sqrt(2), self.pos[1] + delta * self.dt / math.sqrt(2))
            self.dir = Dir.DOWN_RIGHT
        elif (keys[pygame.K_a] and keys[pygame.K_w] and self.number == 1) or (keys[pygame.K_UP] and keys[pygame.K_LEFT] and self.number == 2):
            self.pos = (self.pos[0] - delta * self.dt / math.sqrt(2), self.pos[1] - delta * self.dt / math.sqrt(2))
            self.dir = Dir.UP_LEFT
        elif (keys[pygame.K_a] and keys[pygame.K_s] and self.number == 1) or (keys[pygame.K_DOWN] and keys[pygame.K_LEFT] and self.number == 2):
            self.pos = (self.pos[0] - delta * self.dt / math.sqrt(2), self.pos[1] + delta * self.dt / math.sqrt(2))
            self.dir = Dir.DOWN_LEFT
        elif (keys[pygame.K_w] and self.number == 1) or (keys[pygame.K_UP] and self.number == 2):
            self.pos = (self.pos[0], self.pos[1] - delta * self.dt)
            self.dir = Dir.UP
        elif (keys[pygame.K_s] and self.number == 1) or (keys[pygame.K_DOWN] and self.number == 2):
            self.pos = (self.pos[0], self.pos[1] + delta * self.dt)
            self.dir = Dir.DOWN
        elif (keys[pygame.K_a] and self.number == 1) or (keys[pygame.K_LEFT] and self.number == 2):
            self.pos = (self.pos[0] - delta * self.dt, self.pos[1])
            self.dir = Dir.LEFT
        elif (keys[pygame.K_d] and self.number == 1) or (keys[pygame.K_RIGHT] and self.number == 2):
            self.pos = (self.pos[0] + delta * self.dt, self.pos[1])
            self.dir = Dir.RIGHT
        if (keys[pygame.K_SPACE] and self.number == 1) or (keys[pygame.K_BACKSPACE] and self.number == 2):
            self.shoot()
        self.check_boundaries()

    def shoot(self):
        current_tick = pygame.time.get_ticks()
        cooldown = 100
        projectile_size = 8
        if self.last_shot + cooldown < current_tick:
            new_projectile = Projectile(
                (self.pos[0] + SIZE * SCALE / 4 - projectile_size / 2, self.pos[1] + SIZE * SCALE / 2), self.dir,
                self.screen, self.dt, projectile_size, self.color)
            self.created_projectiles.append(new_projectile)
            self.last_shot = pygame.time.get_ticks()

    def draw(self):
        delta = 0
        if self.dir == Dir.UP:
            delta = 4
        if self.dir == Dir.RIGHT:
            delta = 2
        if self.dir == Dir.DOWN:
            delta = 0
        if self.dir == Dir.LEFT:
            delta = 6
        if self.dir == Dir.UP_RIGHT:
            delta = 3
        if self.dir == Dir.UP_LEFT:
            delta = 5
        if self.dir == Dir.DOWN_RIGHT:
            delta = 1
        if self.dir == Dir.DOWN_LEFT:
            delta = 7
        self.screen.blit(self.image, self.pos, (0, delta * SIZE * SCALE, SIZE * SCALE, SIZE * SCALE))
