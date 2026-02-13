import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont("comicsansms", 25)

# Clock
clock = pygame.time.Clock()


def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))


def message(text, color, y_offset=0):
    mesg = font.render(text, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3 + y_offset])


def game_loop():
    # Starting position
    x = WIDTH // 2
    y = HEIGHT // 2

    # Movement
    dx = 0
    dy = 0

    # Snake body and length
    snake_body = []
    length = 1

    # Food
    food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
    food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE

    # Game Over Flag
    game_over = False

    while True:
        while game_over:
            screen.fill(BLACK)
            message("Game Over! Press C to Play Again or Q to Quit", RED)
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

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -CELL_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = CELL_SIZE
                    dx = 0

        # Update snake position
        x += dx
        y += dy

        # Check wall collision
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        # Update snake body
        snake_head = [x, y]
        snake_body.append(snake_head)

        if len(snake_body) > length:
            del snake_body[0]

        # Check self collision
        for block in snake_body[:-1]:
            if block == snake_head:
                game_over = True

        # Draw everything
        screen.fill(BLACK)
        draw_snake(snake_body)
        pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y, CELL_SIZE, CELL_SIZE))

        # Check food collision
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            food_y = round(random.randrange(0, HEIGHT - CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            length += 1

        # Display score
        score = font.render(f"Score: {length - 1}", True, WHITE)
        screen.blit(score, [10, 10])

        pygame.display.update()
        clock.tick(10)


# Start game
game_loop()
