# Example file showing a circle moving on screen
import pygame
from Player import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = clock.tick(60) / 1000
player1 = Player(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), screen, dt, 1)
player2 = Player(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), screen, dt, 2)
players = [player1, player2]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    keys = pygame.key.get_pressed()
    for player in players:
        player.draw()
        player.move(keys, 20)
        for projectile in player.created_projectiles:
            projectile.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.


pygame.quit()
