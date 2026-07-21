"""
Pac-Man clone using pygame — written with functions only (no classes).
Controls: Arrow keys to move. Eat all pellets to win. Avoid the ghosts!
Power pellets (big dots) let you eat ghosts for a short time.
Press R to restart after game over / win. ESC to quit.

Requires: pip install pygame
"""

import pygame
import random
import sys

# ---------------------------------------------------------------
# Constants
# ---------------------------------------------------------------
TILE = 24                       # pixel size of one maze tile
FPS = 60
PLAYER_SPEED = 2                # pixels per frame (must divide TILE)
GHOST_SPEED = 2
FRIGHTENED_TIME = 6 * FPS       # frames ghosts stay frightened

# Maze legend:  # wall   . pellet   o power pellet   ' ' empty   P player   G ghost
MAZE_LAYOUT = [
    "###################",
    "#........#........#",
    "#o##.###.#.###.##o#",
    "#.................#",
    "#.##.#.#####.#.##.#",
    "#....#...#...#....#",
    "####.### # ###.####",
    "   #.#   G   #.#   ",
    "####.# ## ## #.####",
    "    .  #GGG#  .    ",
    "####.# ##### #.####",
    "   #.#       #.#   ",
    "####.# ##### #.####",
    "#........#........#",
    "#.##.###.#.###.##.#",
    "#o.#.....P.....#.o#",
    "##.#.#.#####.#.#.##",
    "#....#...#...#....#",
    "#.######.#.######.#",
    "#.................#",
    "###################",
]

ROWS = len(MAZE_LAYOUT)
COLS = len(MAZE_LAYOUT[0])
WIDTH = COLS * TILE
HEIGHT = ROWS * TILE + 40       # extra room for score bar

# Colors
BLACK = (0, 0, 0)
BLUE = (33, 33, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
PELLET_COLOR = (255, 184, 174)
FRIGHT_COLOR = (50, 50, 255)
GHOST_COLORS = [(255, 0, 0), (255, 184, 255), (0, 255, 255), (255, 184, 82)]

DIRS = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
    "none": (0, 0),
}


# ---------------------------------------------------------------
# Maze / state setup
# ---------------------------------------------------------------
def build_state():
    """Parse the maze layout and return a fresh game-state dictionary."""
    walls = set()
    pellets = set()
    power_pellets = set()
    player_start = (1, 1)
    ghost_starts = []

    for r, row in enumerate(MAZE_LAYOUT):
        for c, ch in enumerate(row):
            if ch == "#":
                walls.add((c, r))
            elif ch == ".":
                pellets.add((c, r))
            elif ch == "o":
                power_pellets.add((c, r))
            elif ch == "P":
                player_start = (c, r)
            elif ch == "G":
                ghost_starts.append((c, r))

    ghosts = []
    for i, (gc, gr) in enumerate(ghost_starts):
        ghosts.append({
            "x": gc * TILE, "y": gr * TILE,
            "dir": "left",
            "color": GHOST_COLORS[i % len(GHOST_COLORS)],
            "home": (gc, gr),
            "eaten": False,
        })

    return {
        "walls": walls,
        "pellets": pellets,
        "power_pellets": power_pellets,
        "player": {
            "x": player_start[0] * TILE,
            "y": player_start[1] * TILE,
            "dir": "none",
            "next_dir": "none",
            "start": player_start,
            "mouth": 0,
        },
        "ghosts": ghosts,
        "score": 0,
        "lives": 3,
        "fright_timer": 0,
        "game_over": False,
        "won": False,
    }


# ---------------------------------------------------------------
# Movement helpers
# ---------------------------------------------------------------
def tile_of(px, py):
    """Grid tile of a pixel position (top-left based)."""
    return px // TILE, py // TILE


def on_grid(px, py):
    """True when a sprite is perfectly aligned to the tile grid."""
    return px % TILE == 0 and py % TILE == 0


def is_wall(walls, c, r):
    c %= COLS  # wrap horizontally (tunnel)
    if r < 0 or r >= ROWS:
        return True
    return (c, r) in walls


def can_move(walls, px, py, direction):
    """Can a sprite at (px, py) start moving in direction from a grid position?"""
    if direction == "none":
        return False
    dx, dy = DIRS[direction]
    c, r = tile_of(px, py)
    return not is_wall(walls, c + dx, r + dy)


def step(entity, direction, speed):
    dx, dy = DIRS[direction]
    entity["x"] += dx * speed
    entity["y"] += dy * speed
    # horizontal tunnel wrap
    entity["x"] %= WIDTH


# ---------------------------------------------------------------
# Update logic
# ---------------------------------------------------------------
def update_player(state):
    p = state["player"]
    walls = state["walls"]

    if on_grid(p["x"], p["y"]):
        # try queued turn first
        if can_move(walls, p["x"], p["y"], p["next_dir"]):
            p["dir"] = p["next_dir"]
        # stop if current direction is blocked
        if not can_move(walls, p["x"], p["y"], p["dir"]):
            p["dir"] = "none"

    if p["dir"] != "none":
        step(p, p["dir"], PLAYER_SPEED)
        p["mouth"] = (p["mouth"] + 1) % 20

    # eat pellets when centered on a tile
    if on_grid(p["x"], p["y"]):
        pos = tile_of(p["x"], p["y"])
        if pos in state["pellets"]:
            state["pellets"].remove(pos)
            state["score"] += 10
        elif pos in state["power_pellets"]:
            state["power_pellets"].remove(pos)
            state["score"] += 50
            state["fright_timer"] = FRIGHTENED_TIME
            for g in state["ghosts"]:
                g["eaten"] = False

    if not state["pellets"] and not state["power_pellets"]:
        state["won"] = True


def ghost_options(walls, g):
    """Legal directions for a ghost at a grid intersection, no reversing."""
    opposite = {"up": "down", "down": "up", "left": "right", "right": "left"}
    opts = []
    for d in ("up", "down", "left", "right"):
        if d == opposite.get(g["dir"]):
            continue
        if can_move(walls, g["x"], g["y"], d):
            opts.append(d)
    if not opts:  # dead end — allow reversing
        opts = [opposite.get(g["dir"], "left")]
    return opts


def choose_ghost_dir(state, g):
    """Chase the player (or flee when frightened) with a greedy choice,
    plus some randomness so ghosts don't all behave identically."""
    opts = ghost_options(state["walls"], g)
    if random.random() < 0.25:
        return random.choice(opts)

    p = state["player"]
    frightened = state["fright_timer"] > 0 and not g["eaten"]
    best, best_score = opts[0], None
    for d in opts:
        dx, dy = DIRS[d]
        nx = (g["x"] + dx * TILE) % WIDTH
        ny = g["y"] + dy * TILE
        dist = (nx - p["x"]) ** 2 + (ny - p["y"]) ** 2
        score = -dist if frightened else dist  # flee = maximize distance
        if best_score is None or score < best_score:
            best, best_score = d, score
    return best


def update_ghosts(state):
    for g in state["ghosts"]:
        if on_grid(g["x"], g["y"]):
            g["dir"] = choose_ghost_dir(state, g)
        speed = GHOST_SPEED if state["fright_timer"] == 0 else max(1, GHOST_SPEED - 1)
        if can_move(state["walls"], g["x"], g["y"], g["dir"]) or not on_grid(g["x"], g["y"]):
            step(g, g["dir"], speed)

    if state["fright_timer"] > 0:
        state["fright_timer"] -= 1


def reset_positions(state):
    p = state["player"]
    p["x"], p["y"] = p["start"][0] * TILE, p["start"][1] * TILE
    p["dir"] = p["next_dir"] = "none"
    for g in state["ghosts"]:
        g["x"], g["y"] = g["home"][0] * TILE, g["home"][1] * TILE
        g["dir"] = "left"
        g["eaten"] = False
    state["fright_timer"] = 0


def check_collisions(state):
    p = state["player"]
    for g in state["ghosts"]:
        if abs(g["x"] - p["x"]) < TILE * 0.6 and abs(g["y"] - p["y"]) < TILE * 0.6:
            if state["fright_timer"] > 0 and not g["eaten"]:
                g["eaten"] = True
                g["x"], g["y"] = g["home"][0] * TILE, g["home"][1] * TILE
                state["score"] += 200
            elif state["fright_timer"] == 0 or g["eaten"]:
                state["lives"] -= 1
                if state["lives"] <= 0:
                    state["game_over"] = True
                else:
                    reset_positions(state)
                return


# ---------------------------------------------------------------
# Drawing
# ---------------------------------------------------------------
def draw_maze(screen, state):
    for (c, r) in state["walls"]:
        pygame.draw.rect(screen, BLUE, (c * TILE, r * TILE, TILE, TILE), border_radius=4)
    for (c, r) in state["pellets"]:
        pygame.draw.circle(screen, PELLET_COLOR,
                           (c * TILE + TILE // 2, r * TILE + TILE // 2), 3)
    for (c, r) in state["power_pellets"]:
        pygame.draw.circle(screen, PELLET_COLOR,
                           (c * TILE + TILE // 2, r * TILE + TILE // 2), 7)


def draw_player(screen, state):
    p = state["player"]
    cx, cy = int(p["x"]) + TILE // 2, p["y"] + TILE // 2
    radius = TILE // 2 - 2
    pygame.draw.circle(screen, YELLOW, (cx, cy), radius)

    # simple animated mouth (a black wedge)
    if p["dir"] != "none" and p["mouth"] < 10:
        dx, dy = DIRS[p["dir"]]
        tip = (cx + dx * radius, cy + dy * radius)
        side = (dy * radius // 2, dx * radius // 2)
        a = (cx + side[0], cy + side[1])
        b = (cx - side[0], cy - side[1])
        pygame.draw.polygon(screen, BLACK, (tip, a, b))


def draw_ghosts(screen, state):
    frightened = state["fright_timer"] > 0
    blink = frightened and state["fright_timer"] < 2 * FPS and (state["fright_timer"] // 15) % 2 == 0
    for g in state["ghosts"]:
        x, y = int(g["x"]), int(g["y"])
        if frightened and not g["eaten"]:
            color = WHITE if blink else FRIGHT_COLOR
        else:
            color = g["color"]
        body = pygame.Rect(x + 2, y + 2, TILE - 4, TILE - 4)
        pygame.draw.rect(screen, color, body, border_radius=8)
        # eyes
        pygame.draw.circle(screen, WHITE, (x + TILE // 3, y + TILE // 3), 4)
        pygame.draw.circle(screen, WHITE, (x + 2 * TILE // 3, y + TILE // 3), 4)
        pygame.draw.circle(screen, BLACK, (x + TILE // 3, y + TILE // 3), 2)
        pygame.draw.circle(screen, BLACK, (x + 2 * TILE // 3, y + TILE // 3), 2)


def draw_hud(screen, state, font):
    bar_y = ROWS * TILE + 8
    score_text = font.render(f"Score: {state['score']}", True, WHITE)
    lives_text = font.render(f"Lives: {state['lives']}", True, WHITE)
    screen.blit(score_text, (10, bar_y))
    screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, bar_y))


def draw_center_text(screen, font, text, color):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    bg = rect.inflate(30, 20)
    pygame.draw.rect(screen, BLACK, bg)
    pygame.draw.rect(screen, color, bg, 2)
    screen.blit(surf, rect)


# ---------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------
def handle_input(state, event):
    p = state["player"]
    key_map = {
        pygame.K_UP: "up", pygame.K_DOWN: "down",
        pygame.K_LEFT: "left", pygame.K_RIGHT: "right",
    }
    if event.key in key_map:
        p["next_dir"] = key_map[event.key]


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pac-Man (functions only)")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 20, bold=True)
    big_font = pygame.font.SysFont("arial", 32, bold=True)

    state = build_state()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r and (state["game_over"] or state["won"]):
                    state = build_state()
                handle_input(state, event)

        if not state["game_over"] and not state["won"]:
            update_player(state)
            update_ghosts(state)
            check_collisions(state)

        screen.fill(BLACK)
        draw_maze(screen, state)
        draw_player(screen, state)
        draw_ghosts(screen, state)
        draw_hud(screen, state, font)

        if state["game_over"]:
            draw_center_text(screen, big_font, "GAME OVER — press R", (255, 60, 60))
        elif state["won"]:
            draw_center_text(screen, big_font, "YOU WIN! — press R", (60, 255, 60))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()