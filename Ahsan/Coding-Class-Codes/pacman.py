import pygame
import random
import os
import time
from collections import deque


pygame.init()
ROWS = 24
TILE = 16
COLS = 71
WIDTH = COLS* TILE
HEIGHT = ROWS * TILE +32
FPS = 12
clock=pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
WALL_COLOR = (2,13,172)
YELLOW = (255,210,0)

GHOST_COLORS = [(250, 127, 5),(250, 5, 5),(5, 197, 250),(250, 5, 246)]

GHOST_1_X,GHOST_1_Y = 50,16
GHOST_2_X,GHOST_2_Y = 8,10
GHOST_3_X,GHOST_3_Y = 29,20
GHOST_4_X,GHOST_4_Y = 10,4
horizontal_ghost_dir = 1
vertical_ghost_dir = 1
following_ghost_dir = 1

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pacman")

def load_maze_from_file():
    if not os.path.exists("maze.txt"):
        exit(1)
    lines = []
    with open ("maze.txt","r",encoding="utf8") as f:
        for row in range (ROWS):
            line = f.readline().rstrip("\n")
            lines.append(line)
    maze = [list(row) for row in lines]
    return maze
        
def draw_maze(maze):
    for i in range (ROWS):
        for j in range (COLS):
            ch = maze [i][j]
            x = j*TILE
            y = i*TILE
            if ch in ('#','|','%'):
                pygame.draw.rect(window,WALL_COLOR,(x,y,TILE,TILE))
            elif ch == '.':
                pygame.draw.circle(window,WHITE,(x+TILE//2,y+TILE//2),TILE//6)

def draw_pacman(pacman_x,pacman_y,):
    pygame.draw.circle(window,YELLOW, (pacman_x*TILE + TILE//2,pacman_y*TILE + TILE//2),TILE//2)


def is_wall(pacman_x,pacman_y,maze):
      if pacman_x < 0 or pacman_x >= COLS or pacman_y < 0 or pacman_y >= ROWS:
            return True
      if maze[pacman_y][pacman_x] in ('|','#','%'):
           return True
      return False

def draw_ghost(ghost_positions):
    for i,position in enumerate(ghost_positions):
        pygame.draw.rect(window,GHOST_COLORS[i],(position[0] * TILE +2, position[1] * TILE +2, TILE-4,TILE-4))

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

def vertical_ghost_movement(ghost_x,ghost_y):
    global vertical_ghost_dir
    if vertical_ghost_dir == 1:
        ghost_y += 1
        if ghost_y == ROWS-1:
            vertical_ghost_dir = -1
    if vertical_ghost_dir == -1:
        ghost_y -= 1
        if ghost_y == 3:
            vertical_ghost_dir = 1
    return ghost_x,ghost_y


move_follower = True
def follower_ghost(ghost_x,ghost_y,px,py,maze):
    global move_follower
    
    move_follower = not move_follower
    if not move_follower:
        return ghost_x,ghost_y

    
    
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    queue = deque()
    queue.append((ghost_x,ghost_y))
    visited = set([(ghost_x,ghost_y)])
    parent = {(ghost_x,ghost_y):None}

    while queue:
        x,y = queue.popleft()

        if (x,y) == (px,py):
            break

        for dx,dy in directions:
            nx,ny = x+dx, y+dy
            if (0 <= nx < COLS and 0<= ny < ROWS and maze[ny][nx] not in ('|','#','%') and (nx,ny) not in visited):
                visited.add((nx,ny))
                parent[(nx,ny)] = (x,y)
                queue.append((nx,ny))
    
    if (px,py) not in parent:
        return ghost_x,ghost_y

    curr = (px,py)
    while parent[curr] != (ghost_x,ghost_y) and parent[curr] is not None:
        curr = parent[curr]

    return curr

def random_ghost(gx, gy,maze):
    # choose a random valid direction; if none, stay
    chance = random.randint(0,1)
    if chance == 0:
        return gx,gy
    choices = []
    if not is_wall(gx - 1, gy,maze): choices.append((-1, 0))
    if not is_wall(gx + 1, gy,maze): choices.append((1, 0))
    if not is_wall(gx, gy - 1,maze): choices.append((0, -1))
    if not is_wall(gx, gy + 1,maze): choices.append((0, 1))
    if choices:
        dx, dy = random.choice(choices)
        return gx + dx, gy + dy
    return gx, gy

def main():

    maze = load_maze_from_file()
    for y in range(1,ROWS-1):
        for x in range (1,COLS-1):
            if maze[y][x] == ' ':
                maze[y][x] = '.'
    pacman_x = 31
    pacman_y = 9

    ghost_1_x = GHOST_1_X
    ghost_1_y = GHOST_1_Y
    ghost_2_x = GHOST_2_X
    ghost_2_y = GHOST_2_Y
    ghost_3_x = GHOST_3_X
    ghost_3_y = GHOST_3_Y
    ghost_4_x = GHOST_4_X
    ghost_4_y = GHOST_4_Y

    score=0
    padding=10
    font=pygame.font.SysFont(None,36)
    lives=3
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        keys = pygame.key.get_pressed()
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
        ghost_2_x,ghost_2_y = vertical_ghost_movement(ghost_2_x,ghost_2_y)
        ghost_3_x,ghost_3_y = random_ghost(ghost_3_x,ghost_3_y,maze)
        ghost_4_x,ghost_4_y = follower_ghost(ghost_4_x,ghost_4_y,pacman_x,pacman_y,maze)
        draw_maze(maze=maze)
        draw_pacman(pacman_x,pacman_y)
        draw_score_and_lives(score,lives,padding,font)
        draw_ghost([(ghost_1_x,ghost_1_y),(ghost_2_x,ghost_2_y),(ghost_3_x,ghost_3_y),(ghost_4_x,ghost_4_y)])
        # detect collision with ghost
        if (pacman_x,pacman_y) in ((ghost_1_x,ghost_1_y),(ghost_2_x,ghost_2_y),(ghost_3_x,ghost_3_y),(ghost_4_x,ghost_4_y)):
            lives -= 1
            pacman_x = 31
            pacman_y = 9

            ghost_1_x = GHOST_1_X
            ghost_1_y = GHOST_1_Y
            ghost_2_x = GHOST_2_X
            ghost_2_y = GHOST_2_Y
            ghost_3_x = GHOST_3_X
            ghost_3_y = GHOST_3_Y
            ghost_4_x = GHOST_4_X
            ghost_4_y = GHOST_4_Y

        if not any(maze[r][c] == '.' for r in range(ROWS) for c in range(COLS)):
            running = False
            #game win screen
            pygame.time.wait(1000)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()