import pygame

pygame.init()

MAZE_LAYOUT = [
    "###################",
    "#.........#........",
    "#o##.###.#.###.##o#",
    
]


TILE = 24
HEIGHT = 400
WIDTH = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False