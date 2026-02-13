import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game window size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game (With Background)")

# Colors
WHITE = (255, 255, 255)

# Load images
snake_head_img = pygame.image.load("head.png").convert_alpha()
snake_body_img = pygame.image.load("head.png").convert_alpha()
food_img = pygame.image.load("apple.png").convert_alpha()
background_img = pygame.image.load("background.jpg").convert()

# Resize images
snake_head_img = pygame.transform.scale(snake_head_img, (CELL_SIZE, CELL_SIZE))
snake_body_img = pygame.transform.scale(snake_body_img, (CELL_SIZE, CELL_SIZE))
food_img = pygame.transform.scale(food_img, (CELL_SIZE, CELL_SIZE))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Font
font = pygame.font.SysFont("comicsansms", 25)

# Clock
clock = pygame.time.Clock()


def draw_snake(snake_body):
    """Draw snake with images."""
    for i, block in enumerate(snake_body):
        if i == len(snake_body) - 1:
            screen.blit(snake_head_img, (block[0], block[1]))
        else:
            screen.blit(snake_body_img, (block[0], block[1]))


def message(text, color, y_offset=0):
    mesg = font.render(text, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3 + y_offset])


def game_loop():
    x = WIDTH // 2
    y = HEIGHT // 2
    dx, dy = 0, 0

    snake_body = []
    length = 1

    food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
    food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE

    game_over = False

    while True:
        while game_over:
            screen.blit(background_img, (0, 0))
            message("Game Over! Press C to Play Again or Q to Quit", (255, 0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -CELL_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = CELL_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy, dx = -CELL_SIZE, 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy, dx = CELL_SIZE, 0

        # Move snake
        x += dx
        y += dy

        # Wall collision
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        # Update body
        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > length:
            del snake_body[0]

        # Self collision
        for block in snake_body[:-1]:
            if block == snake_head:
                game_over = True

        # Draw everything
        screen.blit(background_img, (0, 0))
        screen.blit(food_img, (food_x, food_y))
        draw_snake(snake_body)

        # Food collision
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            length += 1

        # Score
        score = font.render(f"Score: {length - 1}", True, WHITE)
        screen.blit(score, [10, 10])

        pygame.display.update()
        clock.tick(10)


# Run game
game_loop()
