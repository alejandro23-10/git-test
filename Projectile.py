from Direction import Dir
import pygame
import math

class Projectile:
    def __init__(self, start_pos, dir, screen, dt, size=10, color="red"):
        self.pos = start_pos
        self.dir = dir
        self.screen = screen
        self.dt = dt * 6
        self.size = size
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.size, self.size))
        if self.dir == Dir.UP:
            self.pos = (self.pos[0], self.pos[1] - self.size * self.dt)
        if self.dir == Dir.DOWN:
            self.pos = (self.pos[0], self.pos[1] + self.size * self.dt)
        if self.dir == Dir.LEFT:
            self.pos = (self.pos[0] - self.size * self.dt, self.pos[1])
        if self.dir == Dir.RIGHT:
            self.pos = (self.pos[0] + self.size * self.dt, self.pos[1])
        if self.dir == Dir.UP_RIGHT:
            self.pos = (self.pos[0] + self.size * self.dt / math.sqrt(2), self.pos[1] - self.size * self.dt / math.sqrt(2))
        if self.dir == Dir.UP_LEFT:
            self.pos = (self.pos[0] - self.size * self.dt/ math.sqrt(2), self.pos[1] - self.size * self.dt / math.sqrt(2))
        if self.dir == Dir.DOWN_RIGHT:
            self.pos = (self.pos[0] + self.size * self.dt/ math.sqrt(2), self.pos[1] + self.size * self.dt / math.sqrt(2))
        if self.dir == Dir.DOWN_LEFT:
            self.pos = (self.pos[0] - self.size * self.dt/ math.sqrt(2), self.pos[1] + self.size * self.dt / math.sqrt(2))

