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

DIRS = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
    "none": (0, 0),
}

GHOST_COLORS = [(255,0,0),(255,184,255),(0,255,255),(255,184,82)]
BLUE = (0,0,255)
PALLET_COLOR = (255,184,174)
YELLOW = (255, 255, 0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PLAYER_SPEED = 2
window = pygame.display.set_mode((WIDTH,HEIGHT))


def build_state():
    walls = set()
    pallets = set()
    power_pallets = set()
    player_start = (1,1)
    ghost_starts = []

    for r,row in enumerate(MAZE_LAYOUT):
        for c,ch, in enumerate(row):
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
                              
    return{
        "walls":walls,
        "pallets":pallets,
        "power_pallets":power_pallets,
        "player":{
            "x":player_start[0] * TILE,
            "y":player_start[1] * TILE,
            "dir":"none",
            "next_dir":"none",
            "start":player_start,
            "mouth":0,
        },
        "ghosts":ghosts,
        "score":0,
        "lives":3,
        "fright_timer":0,
        "game_over":False,
        "won":False
    }

def draw_maze(state):
    for (c,r) in state["walls"]:
        pygame.draw.rect(window,BLUE,(c * TILE,r*TILE,TILE,TILE),border_radius = 4)
    for (c,r) in state["pallets"]:
        pygame.draw.circle(window,PALLET_COLOR,(c*TILE+TILE//2,r*TILE+TILE//2),3)
    
    for (c,r) in state["power_pallets"]:
        pygame.draw.circle(window,PALLET_COLOR,(c*TILE+TILE//2,r*TILE+TILE//2),7)

def draw_player(state):
    player = state["player"]
    cx,cy = int(player["x"]) + TILE//2, player["y"] + TILE //2
    radius = TILE//2 -2
    pygame.draw.circle(window,YELLOW,(cx,cy),radius)

    if player['dir'] != "none" and player['mouth']<10:
        dx,dy = DIRS[player["dir"]]
        tip = (cx+dx*radius,cy+dy*radius)
        side = (dy*radius // 2, dx * radius //2)
        a = (cx+side[0],cy+side[1])
        b = (cx-side[0],cy-side[1])
        pygame.draw.polygon(window,BLACK,(tip,a,b))


def draw_hud(state):
    font = pygame.font.SysFont('arial',20,bold=True)
    bar_y = ROWS*TILE+8
    score_text = font.render(f"Score: {state["score"]}",True,WHITE)
    lives_text = font.render(f"Lives: {state["lives"]}",True,WHITE)
    window.blit(score_text,(10,bar_y))
    window.blit(lives_text,(WIDTH-lives_text.get_width()-10,bar_y))

def draw_ghosts(state):
    for g in state["ghosts"]:
        x = int(g["x"])
        y = int(g["y"])
        color = g["color"]
        
        body = pygame.Rect(x+2,y+2,TILE-4,TILE-4)
        pygame.draw.rect(window,color,body,border_radius = 8)
        #Eyes
        pygame.draw.circle(window,WHITE,(x+TILE//3,y+TILE//3),4)
        pygame.draw.circle(window,WHITE,(x+2*TILE//3,y+TILE//3),4)
        pygame.draw.circle(window,BLACK,(x+TILE//3,y+TILE//3),2)
        pygame.draw.circle(window,BLACK,(x+2*TILE//3,y+TILE//3),2)


# This function will only find the direction of movement but it will not move the player
def handle_input(state,event):
    player = state["player"]
    key_map={

        pygame.K_UP: "up",
        pygame.K_DOWN:"down",
        pygame.K_LEFT:"left",
        pygame.K_RIGHT:"right"
    }
    if event.key in key_map:
        player["next_dir"]=key_map[event.key]

#Supporting Functions
def tile_of(px,py):
    return px//TILE,py//TILE

def on_grid(px,py):
    return px % TILE == 0 and py % TILE == 0

def is_wall(walls,c,r):
    c = c % COLS
    if r < 0 or r >= ROWS:
        return True
    return (c,r) in walls

def can_move(walls,px,py,direction):
    if direction == "none":
        return False
    dx,dy = DIRS[direction]
    c,r = tile_of(px,py)
    return not is_wall(walls,c+dx,r+dy)

def step(entity,direction,speed):
    dx, dy = DIRS[direction]
    entity['x'] += dx * speed
    entity['y'] += dy * speed

    entity['x'] %= WIDTH


# MOve player + check whether player eats the player
def update_player(state):
    player = state["player"]
    walls = state["walls"]

    if on_grid(player['x'],player['y']):
        # is allowed to move
        if can_move(walls,player['x'],player['y'],player['next_dir']):
            player['dir'] = player['next_dir']
        if not can_move(walls,player['x'],player['y'],player['dir']):
                    player['dir'] = 'none'

    if player['dir'] != 'none':
        step(player,player['dir'],PLAYER_SPEED)        
        player['mouth'] = (player['mouth']+1)%20

    # eat pallets
    if on_grid(player['x'],player['y']):
        pos = tile_of(player['x'],player['y'])
        if pos in state['pallets']:
            state['pallets'].remove(pos)
            state['score'] += 10
             
    if not state["pallets"]:
        state["won"] = True


def main():
    running = True
    state = build_state()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                handle_input(state,event)
        update_player(state)
        window.fill(BLACK)
        draw_maze(state)
        draw_player(state)
        draw_hud(state)
        draw_ghosts(state)
        
        pygame.display.flip()
        

if __name__ == "__main__":
    main()




