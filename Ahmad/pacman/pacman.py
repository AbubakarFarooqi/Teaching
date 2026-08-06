import pygame

pygame.init()

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

TILE = 24
HEIGHT = ROWS * TILE + 40
WIDTH = COLS * TILE

GHOST_COLORS = [(255,0,0),(255,184,255),(0,255,255),(255,184,82)]
window = pygame.display.set_mode((WIDTH,HEIGHT))


def build_state():
    walls = set()
    pallets = set()
    power_pallets = set()
    player_start = (1,1)
    ghost_starts = []

    for r,row in enumerate(MAZE_LAYOUT):
        for c,ch, in enumerate(MAZE_LAYOUT):
            if ch == '#':
                walls.add((c,r))
            elif ch == ".":
                pallets.add((c,r))
            elif ch == "o":
                power_pallets.add((c,r))
            elif ch == "P":
                player_start = (c,r)
            elif ch == "G":
                ghost_starts.append((c,r))

    ghosts = []

    for i ,(gc,gr) in enumerate(ghost_starts):
        ghosts.append(
            {
                "x": gc * TILE,
                "y": gr * TILE,
                "dir":"left",
                "color":GHOST_COLORS[i % len(GHOST_COLORS)],
                "eaten":False
            }
        )
                              








running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False