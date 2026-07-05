import pygame
import time
import random
import math
pygame.init()

HEIGHT = 400
WIDTH = 800

window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

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
enemies_bullet_dx = []
enemies_bullet_dy = []

enemy_1_x = 100
enemy_1_y = 30

enemy_2_x = 400
enemy_2_y = 30

enemy_direction =["left","right","left"]

enemy_3_x = 700
enemy_3_y = 30

lives = 10



enemies =[]
player_bullets = []

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,255,0)

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
    for i in range(len(enemies_bullet)):
        if player.colliderect(enemies_bullet[i]):
            enemies_bullet.pop(i)
            enemies_bullet_dx.pop(i)
            enemies_bullet_dy.pop(i)
            return True
    return False

def enemy_bullet_fire():
    enemy_index = random.randint(0, 20)
    if enemy_index < len(enemies):
        enemy = enemies[enemy_index]
        bx = enemy.x + (enemy_width // 2)
        by = enemy.y + 5 + enemy.height
        bullet = pygame.Rect(bx, by, bullet_height, bullet_width)

        target_x = player_x + (player_width // 2)
        target_y = player_y + (player_height // 2)
        diff_x = target_x - bx
        diff_y = target_y - by
        distance = math.hypot(diff_x, diff_y) or 1

        speed = 8
        enemies_bullet.append(bullet)
        enemies_bullet_dx.append((diff_x / distance) * speed)
        enemies_bullet_dy.append((diff_y / distance) * speed)


def move_enemy_bullet():
    for i in range(len(enemies_bullet) - 1, -1, -1):
        enemies_bullet[i].x += enemies_bullet_dx[i]
        enemies_bullet[i].y += enemies_bullet_dy[i]
        if (enemies_bullet[i].y > HEIGHT or enemies_bullet[i].y < 0
                or enemies_bullet[i].x < 0 or enemies_bullet[i].x > WIDTH):
            enemies_bullet.pop(i)
            enemies_bullet_dx.pop(i)
            enemies_bullet_dy.pop(i)

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

def draw_player_bullets():
    for bullet in player_bullets:
        pygame.draw.circle(window,RED,bullet.center,5)

def create_enemies():
    rect1 = pygame.Rect(enemy_1_x,enemy_1_y,enemy_height,enemy_width)
    rect2 = pygame.Rect(enemy_2_x,enemy_2_y,enemy_height,enemy_width)
    rect3 = pygame.Rect(enemy_3_x,enemy_3_y,enemy_height,enemy_width)
    enemies.append(rect1)
    enemies.append(rect2)
    enemies.append(rect3)
    

def draw_enemies():
    for rect in enemies:
        pygame.draw.rect(window,RED,rect)


def create_player():
    return pygame.Rect(player_x,player_y,player_height,player_width)

def draw_player(player_rect):
    pygame.draw.rect(window,BLUE,player_rect)
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
            running = False


        pygame.display.flip()
        window.fill(BLACK)
        clock.tick(50)