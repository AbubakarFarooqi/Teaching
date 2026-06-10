import pygame

pygame.init()

HEIGHT = 300
WIDTH = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))

player_height = 50
player_width = 50
player_x = WIDTH // 2 # // removes the decimal part
player_y = HEIGHT - 70

BLUE = (0,0,255)

def create_player():
    return pygame.Rect(player_x,player_y,player_height,player_width)

def draw_player(player_rect):
    pygame.draw.rect(window,BLUE,player_rect)
if __name__ == "__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_rect = create_player()
        draw_player(player_rect)
        pygame.display.flip()