import pygame
import random

pygame.init()
HEIGHT = 400 
WIDTH = 600
CELL_SIZE = 20
FPS = 10
window = pygame.display.set_mode((WIDTH,HEIGHT)) 

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,65)

# Colors
RED = (255, 0, 0)
GREEN = (0.255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)


def draw_snake(snake_body):
    # we will change the code
   
    for body_part in snake_body:
        snake_rect = pygame.Rect(body_part[0],body_part[1],20,20)
        pygame.draw.rect(window,RED,snake_rect)

def draw_food(x_food,y_food):
    rect=(x_food,y_food,20,20)
    pygame.draw.rect(window,RED,rect)

def main():
    
    scores = 0
    direction = 'left'

    x_snake = WIDTH/2
    y_snake = HEIGHT/2

    x_food = random.randrange(0,WIDTH-CELL_SIZE,CELL_SIZE)
    y_food = random.randrange(0,HEIGHT-CELL_SIZE,CELL_SIZE)

    snake_body = []
    length = 1 # will be equal to body parts


    mx=0
    my=0
    running = True
    while running: #Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and direction != 'left':
                    direction = 'right'
                    my = 0
                    mx = CELL_SIZE
                if event.key == pygame.K_LEFT and direction != 'right':
                    direction = 'left'
                    my = 0
                    mx = -CELL_SIZE
                if event.key == pygame.K_UP and direction != 'down':
                    direction = 'up'
                    my = -CELL_SIZE
                    mx = 0
                if event.key == pygame.K_DOWN and direction != 'up':
                    direction = 'down'
                    my = CELL_SIZE
                    mx = 0
        # coordinates of snake head
        x_snake = x_snake + mx 
        y_snake = y_snake + my

        snake_head = [x_snake,y_snake]
        snake_body.append(snake_head)

        window.fill(BLACK)
        draw_snake(snake_body)
        draw_food(x_food,y_food)
        
        if x_snake == x_food and y_snake == y_food:
            score += 1
            x_food = random.randrange(0,WIDTH-CELL_SIZE,CELL_SIZE)
            y_food = random.randrange(0,HEIGHT-CELL_SIZE,CELL_SIZE)
        if x_snake < 0 or x_snake >= WIDTH or y_snake < 0 or y_snake >= HEIGHT:
            running = False

        #Displaying Scores
        scores_text = f"Scores: {scores}"
        text_surf = font.render(scores_text,True,WHITE)
        text_rect = text_surf.get_rect()
        text_rect.topleft = (0,20)
        window.blit(text_surf,text_rect)


        clock.tick(FPS)
        pygame.display.flip() # updates your frame

if __name__ == "__main__":
    main()