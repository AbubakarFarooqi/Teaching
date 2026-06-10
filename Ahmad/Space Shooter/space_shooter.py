import pygame

pygame.init()

HEIGHT = 300
WIDTH = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))

if __name__ == "__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False