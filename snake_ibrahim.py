import pygame
import random

pygame.init()

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
CELL_SIZE = 40
window_width = 800
window_height = 800
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


def create_and_draw_apple(x,y):
    food = pygame.Rect(x,y,CELL_SIZE,CELL_SIZE)
    pygame.draw.rect(win,RED,food)

def draw_snake_body(snake_body):
    for block in snake_body:
        x = block[0]
        y = block[1]
        pygame.draw.rect(win,GREEN,pygame.Rect(x,y,CELL_SIZE,CELL_SIZE))
    


def snake_main():
    running = True
    x = window_width // 2
    y = window_height // 2
    score = 0
    #movement
    mx = 0
    my = 0

    food_x = (random.randrange(0,window_width-CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    food_y = (random.randrange(0,window_height-CELL_SIZE)// CELL_SIZE) * CELL_SIZE  

    snake_body = []
    length = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT and mx == 0:
                    mx = -CELL_SIZE
                    my = 0
                elif event.key == pygame.K_RIGHT and mx == 0:
                    mx = CELL_SIZE
                    my = 0
                elif event.key == pygame.K_UP and my == 0:
                    mx = 0
                    my = -CELL_SIZE
                elif event.key == pygame.K_DOWN and my == 0:
                    mx = 0
                    my = CELL_SIZE
        
        x += mx
        y += my

        win.fill(BLACK)
        snake_head = [x,y]
        snake_body.append(snake_head)

        if len(snake_body) > length:
            del snake_body[0]
        
        #SELF collision
        for block in snake_body[:-1]:
            if block == snake_head:
                running = False

        draw_snake_body(snake_body)
        create_and_draw_apple(food_x,food_y)

        #game walls collision
        if x >= window_width or x < 0 or y >= window_height or y < 0:
            running = False


        #Snake-Food Collision
        if x == food_x and y == food_y:
            food_x = (random.randrange(0,window_width-CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            food_y = (random.randrange(0,window_height-CELL_SIZE)// CELL_SIZE) * CELL_SIZE  
            length += 1
            score += 1


        pygame.display.flip()
        clock.tick(15)


if __name__ == "__main__":
    snake_main()