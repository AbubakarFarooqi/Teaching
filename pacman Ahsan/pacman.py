import pygame
import random
import time
import os

pygame.init()
ROWS = 24
COLS = 71
TILE = 16
WIDTH = COLS* TILE
HEIGHT = ROWS * TILE +32
FPS = 12

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
WALL_COLOR = (2,13,172)
YELLOW = (255,210,0)

GHOST_COLORS = [(250, 5, 5),(5, 197, 250),(250, 5, 246),(250, 127, 5)]

GHOST_1_X, GHOST_1_Y = 50,16 # horizontal

horizontal_ghost_dir = 1 # 1 -> right, -1 -> left


window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pac-Man")
font = pygame.font.SysFont("consolas", 18)
clock = pygame.time.Clock()

walls_rect = []
pacman_rect = None

def load_maze_from_file():
    if not os.path.exists(path="maze.txt"):
        exit(1)
    lines = []
    with open("maze.txt","r",encoding="utf8") as f:
        for row in range(ROWS):
            line = f.readline().rstrip("\n")
            if len(line) < COLS:
                line = line + " " * (COLS - len(line))
            lines.append(line)
    if len(lines) != ROWS:
        return None
    maze = [list(row) for row in lines]
    return maze


# def create_maze(maze):

def draw_maze(maze):
    for i in range(ROWS):
        for j in range(COLS):
            ch = maze[i][j]
            x = j*TILE
            y = i*TILE
            if ch in ('#','|','%'):
                pygame.draw.rect(window,WALL_COLOR,(x,y,TILE,TILE))
            elif ch == '.':
                pygame.draw.circle(window,WHITE,(x+TILE//2,y+TILE//2),max(1, TILE//6))

def draw_pacman(pacman_x,pacman_y):
    pygame.draw.circle(window,YELLOW, (pacman_x*TILE + TILE//2,pacman_y*TILE + TILE//2),TILE//2-1)

def is_wall(pacman_x,pacman_y,maze):
    if pacman_x < 0 or pacman_x >= COLS or pacman_y < 0 or pacman_y >= ROWS:
        return True
    return  maze[pacman_y][pacman_x] in ('|','#','%')

def draw_ghost(ghosts_positions):
    for position in ghosts_positions:
        pygame.draw.rect(window,GHOST_COLORS[0],(position[0] * TILE +2, position[1] * TILE +2,TILE-4,TILE-4))
        # position[0] -> x
        # position[1] -> y
        
def draw_score_and_lives(score,lives,padding,font):
    scores_text=f"Score: {score} Lives: {lives}"
    text_surf=font.render(scores_text,True, WHITE)
    text_rect=text_surf.get_rect()
    text_rect.bottomleft=(WIDTH - padding,padding)
    window.blit(text_surf,(8, ROWS * TILE + 4))

def is_food(pacman_x,pacman_y,maze):
    if maze[pacman_y][pacman_x] == '.':
        return True
    return False

def horizontal_ghost_movement(ghost_x,ghost_y):
    global horizontal_ghost_dir
    if horizontal_ghost_dir == 1:
        ghost_x += 1
        if ghost_x == COLS-3:
            horizontal_ghost_dir = -1
    if horizontal_ghost_dir == -1:
        ghost_x -= 1
        if ghost_x == 2:
            horizontal_ghost_dir = 1
    return ghost_x,ghost_y


def main():
    maze = load_maze_from_file()
    for y in range(1,ROWS-1):
        for x in range (1,COLS-1):
            if maze[y][x] == ' ':
                maze[y][x] = '.'
    
    font=pygame.font.SysFont(None,36)
    score = 0
    lives = 3
    


    pacman_x = 31
    pacman_y = 9

    ghost_1_x = GHOST_1_X
    ghost_1_y = GHOST_1_Y

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        keys = pygame.key.get_pressed()

        # Move Pac-Man while key is held down
        if keys[pygame.K_UP]:
            if not is_wall(pacman_x,pacman_y-1,maze):
                pacman_y -= 1
        if keys[pygame.K_DOWN]:
            if not is_wall(pacman_x,pacman_y+1,maze):
                pacman_y += 1
        if keys[pygame.K_LEFT]:
            if not is_wall(pacman_x-1,pacman_y,maze):
                pacman_x -= 1
        if keys[pygame.K_RIGHT]:
            if not is_wall(pacman_x+1,pacman_y,maze):
                pacman_x += 1
        
        if is_food(pacman_x,pacman_y,maze):
            maze[pacman_y][pacman_x] = ' '
            score += 1
                        
        window.fill(BLACK)
        ghost_1_x,ghost_1_y = horizontal_ghost_movement(ghost_1_x,ghost_1_y)
        draw_maze(maze=maze)
        draw_pacman(pacman_x,pacman_y)
        draw_score_and_lives(score,lives,10,font)
        draw_ghost([(ghost_1_x,ghost_1_y)])
        pygame.display.flip()
        clock.tick(15)
   

if __name__ == "__main__":
    main()