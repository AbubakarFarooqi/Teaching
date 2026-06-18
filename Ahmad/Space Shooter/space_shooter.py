import pygame

pygame.init()

HEIGHT = 300
WIDTH = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))

player_height = 50
player_width = 50
player_x = WIDTH // 2 # // removes the decimal part
player_y = HEIGHT - 70

total_no_of_enemies = 1
enemy_height = 50
enemy_width = 50

enemy_1_x = 100
enemy_1_y = 30

enemies = []

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

def create_enemies():
    rect1 = pygame.Rect(enemy_1_x,enemy_1_y,enemy_height,enemy_width)
    enemies.append(rect1)

def draw_enemies():
    for rect in enemies:
        pygame.draw.rect(window,RED,rect)

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
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            player_x = player_x - 5
        if keys_pressed[pygame.K_RIGHT]:
            player_x = player_x + 5
        player_rect = create_player()
        draw_player(player_rect)
        create_enemies()
        draw_enemies()
        pygame.display.flip()
        window.fill(BLACK)