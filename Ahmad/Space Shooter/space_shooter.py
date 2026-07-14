import pygame
import time
import random

pygame.init()

HEIGHT = 400
WIDTH = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

# Fonts for the end screens
big_font = pygame.font.Font(None, 80)
small_font = pygame.font.Font(None, 36)

total_numbers_of_enemies = 1
player_height = 50
player_width = 50
player_x = WIDTH // 2
player_y = HEIGHT - 70
enemy_height = 50
enemy_width = 50
bullet_height = 5
bullet_width = 10
enemies_bullet =[]

player_ship_image = pygame.image.load("player.png")
enemy_ship_image = pygame.image.load("enemy.png")
background_image = pygame.image.load("background.jpeg")

#Music and Sounds

bg_music = pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1) # -1 means it will run forever
pygame.mixer.set_num_channels(16)

bullet_shoot_sound = pygame.mixer.Sound("laser.mp3")

player_ship_image = pygame.transform.scale(player_ship_image,(player_height,player_width))
enemy_ship_image = pygame.transform.scale(enemy_ship_image,(enemy_height,enemy_width))
background_image = pygame.transform.scale(background_image,(WIDTH,HEIGHT))


enemy_1_x = 100
enemy_1_y = 30

enemy_2_x = 400
enemy_2_y = 30

enemy_direction =["left","right","left"]

enemy_3_x = 700
enemy_3_y = 30

lives = 3



enemies =[]
player_bullets = []





RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

def is_enemy_collided_with_other(enemy):
    for other_enemy in enemies:
        if other_enemy != enemy and other_enemy.colliderect(enemy):
            return True
        return False


def move_enemy():
    for i,enemy in enumerate(enemies):
        direction = enemy_direction[i]
        if direction == "left":
            enemy.x = enemy.x - 5
            
            if is_enemy_collided_with_other(enemy):
                enemy_direction[i] = "right"
            if enemy.x <= 0:
                enemy_direction[i] = "right"
        else:
            enemy.x = enemy.x + 5
            if is_enemy_collided_with_other(enemy):
                enemy_direction[i] = "left"
            if enemy.x >= WIDTH:
                enemy_direction[i] = "left"

            

def derect_player_hit(player):
    for bullet in enemies_bullet:
        if player.colliderect(bullet):
            enemies_bullet.remove(bullet)
            return True
    return False

def move_enemy_bullet():
    for bullet in enemies_bullet:
        bullet.y = bullet.y + 8
        if bullet.y > HEIGHT:
            enemies_bullet.remove(bullet)


def enemy_bullet_fire():
    enemy_index = random.randint(0,20)
    if enemy_index < len(enemies):
        enemy = enemies[enemy_index]
        bullet = pygame.Rect(enemy.x + (enemy_width//2),enemy.y+5+enemy.height,bullet_height,bullet_width)
        enemies_bullet.append(bullet)

def draw_enemy_bullets():
    for bullet in enemies_bullet:
        pygame.draw.circle(window,GREEN,bullet.center,5)



def derect_enemy_hit():
    for bullet in player_bullets:
        for enemy in enemies:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                player_bullets.remove(bullet)
                break

def move_player_bullets():
    for bullet in player_bullets:
        bullet.y = bullet.y -8
        if bullet.y < 0:
            player_bullets.remove(bullet)

def create_player_bullet():
    if len(player_bullets) == 1:
        return
    bullet = pygame.Rect(player_x + (player_width//2),player_y -10,bullet_height,bullet_width)
    player_bullets.append(bullet)
    bullet_shoot_sound.set_volume(1.0)
    bullet_shoot_sound.play(fade_ms=500)

def draw_player_bullets():
    for bullet in player_bullets:
        # pygame.draw.circle(window,RED,bullet.center,5)
        cx, cy = bullet.center
        for _ in range(4):
            x = cx + random.randint(-20, 20)
            y = cy + random.randint(-20, 20)
            pygame.draw.circle(window, (255, 255, 200), (x, y), 2)
        window.blit(enemy_ship_image,(bullet.x,bullet.y))
        # window.blit(enemy_ship_image, bullet)  

def create_enemies():
    rect1 = pygame.Rect(enemy_1_x,enemy_1_y,enemy_height,enemy_width)
    rect2 = pygame.Rect(enemy_2_x,enemy_2_y,enemy_height,enemy_width)
    rect3 = pygame.Rect(enemy_3_x,enemy_3_y,enemy_height,enemy_width)
    enemies.append(rect1)
    enemies.append(rect2)
    enemies.append(rect3)
    

def draw_enemies():
    for rect in enemies:
        # pygame.draw.rect(window,RED,rect)
        window.blit(enemy_ship_image,(rect.x,rect.y))


def create_player():
    return pygame.Rect(player_x,player_y,player_height,player_width)

def draw_text_centered(text, font, color, center_y):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(WIDTH // 2, center_y))
    window.blit(surface, rect)
 
 
def draw_game_over_screen():
    window.fill(BLACK)
    window.blit(background_image,(0,0))
    draw_text_centered("GAME OVER", big_font, RED, HEIGHT // 2 - 50)
 
 
def draw_win_screen():
    window.fill(BLACK)
    window.blit(background_image,(0,0))
    draw_text_centered("YOU WIN!", big_font, YELLOW, HEIGHT // 2 - 50)

def draw_player(player_rect):
    # pygame.draw.rect(window,BLUE,player_rect)
    window.blit(player_ship_image,(player_x,player_y))
if __name__ == "__main__":
    running = True
    create_enemies()
    while running:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                running = False
             if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                create_player_bullet()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and (player_x-5) > 0 :
            player_x = player_x - 5
        if keys_pressed[pygame.K_RIGHT] and (player_x+5+player_width) < WIDTH :
            player_x = player_x + 5
        player_rect = create_player()
        draw_player(player_rect)
        draw_enemies()
        draw_player_bullets()
        move_player_bullets()
        derect_enemy_hit()
        enemy_bullet_fire()
        draw_enemy_bullets()
        move_enemy_bullet()
        move_enemy()
        is_hit_by_bullet =derect_player_hit(player_rect)

        if is_hit_by_bullet == True:
            lives = lives -1
        if lives == 0:
            draw_game_over_screen()
            running = False
            pygame.display.flip()
            time.sleep(5)
        if len(enemies) == 0:
            draw_win_screen()
            running = False
            pygame.display.flip()
            time.sleep(5)

        pygame.display.flip()
        window.fill(BLACK)
        window.blit(background_image,(0,0))
        clock.tick(50)