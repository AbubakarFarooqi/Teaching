import pygame as pg
import random

pg.init()
screen_x, screen_y = 450, 300
window = pg.display.set_mode((screen_x, screen_y))
clock = pg.time.Clock()

background = pg.image.load("background.jpeg")  # replace with your image filename

# Optional: scale the image to fit the screen
player_img = pg.image.load("player.png") 
enemy_img = pg.image.load("enemy.png")
background = pg.transform.scale(background, (screen_x, screen_y))



WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

player_height = 50
player_width = 50
player_x = 200
player_y = screen_y - player_height -20

enemy_height = 50
enemy_width = 50
e1_x, e1_y = 100, 30
e2_x, e2_y = 220, 30
e3_x, e3_y = 340, 30


enemies_initial_x = [e1_x, e2_x, e3_x]
enemy_dir = [-1,1,-1]

enemies = []
enemy_bullets = []
player_bullets = []


def create_enemies():
    global enemy_img
    enemy_img = pg.transform.scale(enemy_img, (enemy_height, enemy_width))
    enemy = pg.Rect(e1_x, e1_y, enemy_height, enemy_width)
    enemies.append(enemy)
    enemy = pg.Rect(e2_x, e2_y, enemy_height, enemy_width)
    enemies.append(enemy)
    enemy = pg.Rect(e3_x, e3_y, enemy_height, enemy_width)
    enemies.append(enemy)

def display_enemies():
    for enemy in enemies:
        window.blit(enemy_img, enemy.topleft)


def enemy_bullet_fire():
    if len(enemy_bullets) >= 6:
        return
    enemy_idx = random.randint(0, 20)
    if enemy_idx >= len(enemies):
        return
    enemy = enemies[enemy_idx]
    bullet = pg.Rect(enemy.x + enemy.width // 2 - 2, enemy.y + enemy.height, 4, 10)
    enemy_bullets.append(bullet)

def draw_enemy_bullets():
    for bullet in enemy_bullets:
        # Use pg.draw.circle() to draw the bullet as a circle
        pg.draw.circle(window, RED, bullet.center, 2)  # Draw a circle at the bullet's center with radius 2
def create_player():
    global player_img
    player_img = pg.transform.scale(player_img, (player_height, player_width))
    return pg.Rect(player_x, player_y, player_height, player_width)
def draw_player(player):
    # pg.draw.rect(window, BLUE, player)
    window.blit(player_img, player.topleft)

def move_enemy_bullets():
    for bullet in enemy_bullets:
        bullet.y += 5
        if bullet.y > screen_y:
            enemy_bullets.remove(bullet)

def control_player():
    global player_x
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pg.K_RIGHT] and player_x < screen_x - player_width:
        player_x += 5

def detect_player_hit(player):
    for bullet in enemy_bullets:
        if player.colliderect(bullet):
            enemy_bullets.remove(bullet)
            return True
    return False


def player_bullet_fire():
    if len(player_bullets) >= 3:
        return
    bullet = pg.Rect(player_x + 8, player_y - 10, 4, 10)
    player_bullets.append(bullet)

def draw_player_bullets():
    for bullet in player_bullets:
        pg.draw.circle(window, GREEN, bullet.center, 2)

def move_player_bullets():
    for bullet in player_bullets:
        bullet.y -= 5
        if bullet.y < 0:
            player_bullets.remove(bullet)

def detect_enemy_hit():
    for bullet in player_bullets:
        for enemy in enemies:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                player_bullets.remove(bullet)
                return True
    return False

def move_enemy():
    for i in range(len(enemies)):
        if enemy_dir[i] == 1:
            enemies[i].x += 2
            if enemies[i].x >= enemies_initial_x[i]+50:
                enemy_dir[i] = -1
        else:
            enemies[i].x -= 2
            if enemies[i].x <= enemies_initial_x[i]-50:
                enemy_dir[i] = 1
        
if __name__ == "__main__":
    running = True
    create_enemies()
    lives = 3
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYUP:   # Key released
                if event.key == pg.K_SPACE:
                    player_bullet_fire()

        window.fill((0,0,0))
        window.blit(background, (0, 0))
        keys = pg.key.get_pressed()
        
        move_player_bullets()
        draw_player_bullets()
        move_enemy()
        display_enemies()
        enemy_bullet_fire()
        draw_enemy_bullets()
        player = create_player()
        draw_player(player)
        move_enemy_bullets()
        control_player()
        if detect_player_hit(player):
            lives -= 1
            print(f"Lives left: {lives}")
            if lives <= 0:
                print("Game Over")
                running = False
        detect_enemy_hit()


        pg.display.flip()
        clock.tick(60)
    pg.quit()