import pygame
import random
import math
import os
from collections import deque

pygame.init()
# ---------- Config ----------
TILE = 16                   # tile size in pixels (adjustable)
COLS = 71
ROWS = 24
WIDTH = COLS * TILE
HEIGHT = ROWS * TILE + 32   # extra space for score/lives text
FPS = 12

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 210, 0)
WHITE = (255, 255, 255)
WALL_COLOR = (30, 80, 200)
GHOST_COLORS = [(200, 50, 50), (50, 200, 200), (200, 120, 200), (250,150,50)]

# Starting positions (matching the C++ coordinates)
PACKMAN_X = 31
PACKMAN_Y = 9
GHOST_1_X, GHOST_1_Y = 25, 19   # Random ghost
GHOST_2_X, GHOST_2_Y = 22, 14   # Vertical
GHOST_3_X, GHOST_3_Y = 50, 16   # Horizontal
GHOST_4_X, GHOST_4_Y = 10, 6    # Follower

# ---------- Maze loading ----------
def load_maze_from_file(path="maze.txt"):
    if not os.path.exists(path):
        return None
    lines = []
    with open(path, "r", encoding="utf8") as f:
        for _ in range(ROWS):
            line = f.readline().rstrip("\n")
            # pad or trim to COLS
            # if len(line) < COLS:
            #     line = line + " " * (COLS - len(line))
            lines.append(line)
    if len(lines) != ROWS:
        return None
    return lines

# fallback sample maze (simplified) — uses similar characters: '|' '#' '%' walls, '.' dots
def sample_maze():
    m = []
    for r in range(ROWS):
        row = list(" " * COLS)
        for c in range(COLS):
            # frame border
            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                row[c] = '#'
            else:
                row[c] = '.'
        m.append("".join(row))
    # create some inner walls (simple pattern)
    for r in range(2, ROWS-2, 4):
        for c in range(2, COLS-2):
            if c % 6 < 4:
                row = list(m[r])
                row[c] = '|'
                m[r] = "".join(row)
    # create some percent-blocks like C++ used
    for r in range(4, ROWS-4, 6):
        for c in range(6, COLS-6, 12):
            row = list(m[r])
            row[c] = '%'
            m[r] = "".join(row)
    # leave some empty space near original start positions
    return m

maze_lines = load_maze_from_file() 

# Convert maze to 2D list for mutability
Maze = [list(row) for row in maze_lines]

# Replace spaces with dots for pellets only where appropriate
for y in range(1, ROWS-1):
    for x in range(1, COLS-1):
        if Maze[y][x] == ' ':
            Maze[y][x] = '.'

# Ensure start positions are empty (no wall)
Maze[PACKMAN_Y][PACKMAN_X] = ' '
Maze[GHOST_1_Y][GHOST_1_X] = ' '
Maze[GHOST_2_Y][GHOST_2_X] = ' '
Maze[GHOST_3_Y][GHOST_3_X] = ' '
Maze[GHOST_4_Y][GHOST_4_X] = ' '

# ---------- Game state ----------
score = 0
lives = 4

# previous tile content for ghosts (to restore dots when ghost leaves)
prev_1 = Maze[GHOST_1_Y][GHOST_1_X]
prev_2 = Maze[GHOST_2_Y][GHOST_2_X]
prev_3 = Maze[GHOST_3_Y][GHOST_3_X]
prev_4 = Maze[GHOST_4_Y][GHOST_4_X]

# ghost increments for bouncing ghosts
inc_2 = -1
inc_3 = -1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man (Pygame port of packman.cpp)")
font = pygame.font.SysFont("consolas", 18)

clock = pygame.time.Clock()

# helpers
def is_wall(x, y):
    if x < 0 or x >= COLS or y < 0 or y >= ROWS:
        return True
    return Maze[y][x] in ('|', '%', '#')

def draw_maze():
    for y in range(ROWS):
        for x in range(COLS):
            ch = Maze[y][x]
            rx = x * TILE
            ry = y * TILE
            if ch in ('|', '#', '%'):
                pygame.draw.rect(screen, WALL_COLOR, (rx, ry, TILE, TILE))
            elif ch == '.':
                # small dot pellet centered
                pygame.draw.circle(screen, WHITE, (rx + TILE//2, ry + TILE//2), max(1, TILE//6))

def draw_text():
    txt = f"Score: {score}   Lives: {lives}"
    surf = font.render(txt, True, WHITE)
    screen.blit(surf, (8, ROWS * TILE + 4))

# ghost movement behaviors
def random_move(gx, gy):
    # choose a random valid direction; if none, stay
    choices = []
    if not is_wall(gx - 1, gy): choices.append((-1, 0))
    if not is_wall(gx + 1, gy): choices.append((1, 0))
    if not is_wall(gx, gy - 1): choices.append((0, -1))
    if not is_wall(gx, gy + 1): choices.append((0, 1))
    if choices:
        dx, dy = random.choice(choices)
        return gx + dx, gy + dy
    return gx, gy




def follower_move(gx, gy, px, py):
    """
    Find the ghost's next move toward player using BFS.
    Returns (next_gx, next_gy).
    """
    grid = Maze
    rows = len(grid)
    cols = len(grid[0])

    # Directions: up, down, left, right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    queue = deque()
    queue.append((gx, gy))
    visited = set([(gx, gy)])
    parent = { (gx, gy): None }

    # BFS
    while queue:
        x, y = queue.popleft()

        # If we've reached the player, stop search
        if (x, y) == (px, py):
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < cols and 0 <= ny < rows and
                grid[ny][nx] not in ('|','#','%') and
                (nx, ny) not in visited):

                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    # If no path was found, ghost stays still
    if (px, py) not in parent:
        return gx, gy

    # Reconstruct path backwards
    cur = (px, py)
    while parent[cur] != (gx, gy) and parent[cur] is not None:
        cur = parent[cur]

    # This 'cur' is the next step toward the player
    return cur


# def follower_move(gx, gy, px, py):
#     # compute squared distance for each neighbor (like your C++ logic)
#     candidates = []
#     if not is_wall(gx + 1, gy): candidates.append((gx + 1, gy))
#     if not is_wall(gx - 1, gy): candidates.append((gx - 1, gy))
#     if not is_wall(gx, gy - 1): candidates.append((gx, gy - 1))
#     if not is_wall(gx, gy + 1): candidates.append((gx, gy + 1))
#     # choose candidate that minimizes (dx^2 + dy^2)
#     best = (gx, gy)
#     bestd = 10**9
#     for cx, cy in candidates:
#         d = (cx - px)**2 + (cy - py)**2
#         if d < bestd:
#             bestd = d
#             best = (cx, cy)
#     return best

# ---------- Main loop ----------
packman_x = PACKMAN_X
packman_y = PACKMAN_Y
ghost1_x, ghost1_y = GHOST_1_X, GHOST_1_Y
ghost2_x, ghost2_y = GHOST_2_X, GHOST_2_Y
ghost3_x, ghost3_y = GHOST_3_X, GHOST_3_Y
ghost4_x, ghost4_y = GHOST_4_X, GHOST_4_Y

running = True
control_ghost = 1

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # move packman (one tile at a time; feel free to change to smooth pixel movement)
    if keys[pygame.K_LEFT]:
        if not is_wall(packman_x - 1, packman_y):
            packman_x -= 1
    if keys[pygame.K_RIGHT]:
        if not is_wall(packman_x + 1, packman_y):
            packman_x += 1
    if keys[pygame.K_UP]:
        if not is_wall(packman_x, packman_y - 1):
            packman_y -= 1
    if keys[pygame.K_DOWN]:
        if not is_wall(packman_x, packman_y + 1):
            packman_y += 1

    # collect pellet
    if Maze[packman_y][packman_x] == '.':
        Maze[packman_y][packman_x] = ' '
        score += 1

    # ghost updates (only update ghosts every other tick like original)
    if control_ghost % 2 == 0:
        # Ghost 1: random
        # restore prev tile
        Maze[ghost1_y][ghost1_x] = prev_1
        new_g1x, new_g1y = random_move(ghost1_x, ghost1_y)
        prev_1 = Maze[new_g1y][new_g1x]
        ghost1_x, ghost1_y = new_g1x, new_g1y
        Maze[ghost1_y][ghost1_x] = 'G'

        # Ghost 4: follower
        Maze[ghost4_y][ghost4_x] = prev_4
        new_g4x, new_g4y = follower_move(ghost4_x, ghost4_y, packman_x, packman_y)
        prev_4 = Maze[new_g4y][new_g4x]
        ghost4_x, ghost4_y = new_g4x, new_g4y
        Maze[ghost4_y][ghost4_x] = 'G'

        # Ghost 2: vertical bounce
        Maze[ghost2_y][ghost2_x] = prev_2
        if ghost2_y == 1:
            inc_2 = +1
        if ghost2_y == ROWS - 2:
            inc_2 = -1
        ghost2_y += inc_2
        prev_2 = Maze[ghost2_y][ghost2_x]
        Maze[ghost2_y][ghost2_x] = 'G'

        # Ghost 3: horizontal bounce
        Maze[ghost3_y][ghost3_x] = prev_3
        if ghost3_x == 1:
            inc_3 = +1
        if ghost3_x == COLS - 2:
            inc_3 = -1
        ghost3_x += inc_3
        prev_3 = Maze[ghost3_y][ghost3_x]
        Maze[ghost3_y][ghost3_x] = 'G'

    # Check collisions with ghosts
    collided = False
    if (packman_x, packman_y) in ((ghost1_x, ghost1_y), (ghost2_x, ghost2_y), (ghost3_x, ghost3_y), (ghost4_x, ghost4_y)):
        collided = True

    if collided:
        lives -= 1
        # reset packman position like the C++ code
        packman_x = PACKMAN_X
        packman_y = PACKMAN_Y
        # restore ghosts to their initial points and prev tiles
        ghost1_x, ghost1_y = GHOST_1_X, GHOST_1_Y
        ghost2_x, ghost2_y = GHOST_2_X, GHOST_2_Y
        ghost3_x, ghost3_y = GHOST_3_X, GHOST_3_Y
        ghost4_x, ghost4_y = GHOST_4_X, GHOST_4_Y
        prev_1 = Maze[ghost1_y][ghost1_x]
        prev_2 = Maze[ghost2_y][ghost2_x]
        prev_3 = Maze[ghost3_y][ghost3_x]
        prev_4 = Maze[ghost4_y][ghost4_x]

    # Draw
    screen.fill(BLACK)
    draw_maze()
    # draw packman as circle
    pygame.draw.circle(screen, YELLOW, (packman_x * TILE + TILE//2, packman_y * TILE + TILE//2), TILE//2 - 1)
    # draw ghosts (colored)
    pygame.draw.rect(screen, GHOST_COLORS[0], (ghost1_x * TILE + 2, ghost1_y * TILE + 2, TILE - 4, TILE - 4))
    pygame.draw.rect(screen, GHOST_COLORS[1], (ghost2_x * TILE + 2, ghost2_y * TILE + 2, TILE - 4, TILE - 4))
    pygame.draw.rect(screen, GHOST_COLORS[2], (ghost3_x * TILE + 2, ghost3_y * TILE + 2, TILE - 4, TILE - 4))
    pygame.draw.rect(screen, GHOST_COLORS[3], (ghost4_x * TILE + 2, ghost4_y * TILE + 2, TILE - 4, TILE - 4))

    draw_text()
    pygame.display.flip()

    control_ghost += 1

    # win/lose conditions
    if lives <= 0:
        print("Game Over! Final Score:", score)
        pygame.time.wait(1000)
        running = False

    # optional: end when all pellets gone
    any_pellets = any(Maze[r][c] == '.' for r in range(ROWS) for c in range(COLS))
    if not any_pellets:
        print("You cleared the maze! Score:", score)
        pygame.time.wait(1000)
        running = False

pygame.quit()
