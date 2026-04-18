import pygame
import random
import time 

pygame.init()
clock=pygame.time.Clock()

WIDTH,HEIGHT=600,400
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

font=pygame.font.SysFont(None,65)
padding=10

BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
WHITE=(255,255,255)
CELL_SIZE=20

background_img=pygame.image.load("background.jpg")
background_img=pygame.transform.scale(background_img,(WIDTH,HEIGHT))
food_img=pygame.image.load("apple.png")
food_img=pygame.transform.scale(food_img,(CELL_SIZE,CELL_SIZE))
snakehead_img=pygame.image.load("snake_head copy 2.png")
snakehead_img=pygame.transform.scale(snakehead_img,(CELL_SIZE,CELL_SIZE))
snakebody_img=pygame.image.load("Screenshot 2025-11-01 213749.png")
snakebody_img=pygame.transform.scale(snakebody_img,(CELL_SIZE,CELL_SIZE))

def draw_snake_body(snake_body,direction):
    deg=0
    if direction == 'down':
        deg=0
    if direction == 'up':
        deg=180
    if direction == 'right':
        deg=90
    if direction == 'left':
        deg=-90
    for i, block in enumerate(snake_body):
        if i == len(snake_body)-1:
            window.blit(pygame.transform.rotate(snakehead_img,deg),(block[0],block[1]))
        else:
            window.blit(snakebody_img,(block[0],block[1]))

def draw_fruit(food_x,food_y):
    window.blit(food_img,(food_x,food_y))

def main():
    direction='down'
    x=WIDTH // 2
    y=HEIGHT // 2
    scores=0
    padding=10
    font=pygame.font.SysFont(None,36)
    food_x=round(random.randrange(0,WIDTH-CELL_SIZE) / CELL_SIZE) * CELL_SIZE
    food_y=round(random.randrange(0,WIDTH-CELL_SIZE) / CELL_SIZE) * CELL_SIZE

    mx=0
    my=0

    snake_body=[]
    length=1
    
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RIGHT and mx == 0:
                    direction='right'
                    mx=CELL_SIZE
                    my=0
                if event.key == pygame.K_LEFT and mx == 0:
                    direction='left'
                    mx=-CELL_SIZE
                    my=0
                if event.key == pygame.K_UP and my == 0:
                    direction='up'
                    mx=0
                    my=-CELL_SIZE
                if event.key == pygame.K_DOWN and my == 0:
                    direction='down'
                    mx=0
                    my=CELL_SIZE

        x += mx
        y += my

        if y < 0 or y >= HEIGHT:
            running=False
        if x < 0 or x >= WIDTH:
            running=False

        snake_head=[x,y]
        snake_body.append(snake_head)

        if len(snake_body) > length:
            del snake_body[0]

        for block in snake_body[:-1]:
            if block == snake_head:
                running=False

        window.fill(BLACK)
        window.blit(background_img, (0, 0))
        draw_snake_body(snake_body=snake_body,direction=direction)
        draw_fruit(food_x,food_y)

        if x == food_x and y == food_y:
            food_x=round(random.randrange(0,WIDTH-CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            food_y=round(random.randrange(0,HEIGHT-CELL_SIZE) / CELL_SIZE) * CELL_SIZE
            scores=scores+1
            length=length+1

        scores_text=f"Score: {scores}"
        text_surf=font.render(scores_text,True, WHITE)
        text_rect=text_surf.get_rect()
        text_rect.topright=(WIDTH - padding,padding)
        window.blit(text_surf, text_rect)

  

        pygame.display.flip()
        clock.tick(10)

    window.fill(BLACK)
    window.blit(background_img,(0,0))
    output_text = f"""You Lost!"""
    output_text2 = f"""Score: {scores}"""
    text_surf=font.render(output_text, True, WHITE)
    text_rect=text_surf.get_rect(center=(300,150))
    window.blit(text_surf,text_rect)
    text_surf=font.render(output_text2, True, WHITE)
    text_rect=text_surf.get_rect(center=(300,200))
    window.blit(text_surf,text_rect)
    pygame.display.flip()
    time.sleep(2)

if __name__ == "__main__":
    main()