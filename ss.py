import pygame
import random
import time
pygame.init()
pygame.mixer.init()

HEIGHT = 600
WIDTH = 800


window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Shooter")

background = pygame.image.load('background.jpeg')
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

laser_sound = pygame.mixer.Sound('laser.mp3')
# bg_music = pygame.mixer.music.load('bg_music.mp3')
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play(-1)


FPS = 60
player_x = 200
player_y = HEIGHT-80
player_height = 100
player_width = 100

player_img = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img,(player_height,player_width))

player_bullet_image = pygame.image.load("player_bullet.png")
player_bullet_image = pygame.transform.scale(player_bullet_image,(30,40))


e1_x,e1_y = 100,30
e2_x,e2_y = 360,30
e3_x,e3_y = 640,30
eh,ew = 50,50
enemy_directions=[1,-1,1] # 1 = right, -1 = left
enemy_ranges = [[0,266],[267,532],[533,800]]


enemies = []

enemy_bullets = []
player_bullets = []

font = pygame.font.SysFont(None, 36)
padding = 10

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)


def move_enemy():
    for i in range(0,len(enemies)):
        if enemy_directions[i] == 1:
            enemies[i].x += 2
            if enemies[i].x + ew >= enemy_ranges[i][1]:
                enemy_directions[i] = -1
        if enemy_directions[i] == -1:
            enemies[i].x -= 2
            if enemies[i].x <= enemy_ranges[i][0]:
                enemy_directions[i] = 1

def create_player_bullet():
    if len(player_bullets) >=3:
        return
    bullet = pygame.Rect(player_x + 8, player_y -10 ,10,10)
    player_bullets.append(bullet)
    laser_sound.play(fade_ms=500)

def draw_player_bullets():
    for bullet in player_bullets:
        # pygame.draw.circle(window,GREEN,bullet.center,5)
        window.blit(player_bullet_image,bullet.topleft)


def create_enemy_bullets():
    if len(enemy_bullets)>=6:
        return
    enemy_idx = random.randint(0,20)
    if enemy_idx >=len(enemies):
        return
    enemy = enemies[enemy_idx]
    bullet = pygame.Rect(enemy.x + enemy.width // 2-2, enemy.y + enemy.height+4,10,10)
    enemy_bullets.append(bullet)

def draw_enemy_bullet():
    for bullet in enemy_bullets:
        pygame.draw.circle(window,RED,bullet.center,5)

def create_player():
    player = pygame.Rect(player_x,player_y,player_height,player_width)
    return player


def draw_player(player):
    # pygame.draw.rect(window,BLUE,player)
    window.blit(player_img,(player_x,player_y))



def control_player():
    global player_x
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -=5
    if keys[pygame.K_RIGHT] and player_x < WIDTH-player_width:
        player_x +=5

def create_enemies():
    enemy = pygame.Rect(e1_x,e1_y,eh,ew)
    enemies.append(enemy)
    enemy = pygame.Rect(e2_x,e2_y,eh,ew)
    enemies.append(enemy)
    enemy = pygame.Rect(e3_x,e3_y,eh,ew)
    enemies.append(enemy)

def display_enemies():
    for enemy in enemies:
        pygame.draw.rect(window,RED,enemy)

def move_enemy_bullets():
    for bullet in enemy_bullets:
        bullet.y += 5
        if bullet.y > HEIGHT:
            enemy_bullets.remove(bullet)

def move_player_bullets():
    for bullet in player_bullets:
        bullet.y -= 5
        if bullet.y < 0:
            player_bullets.remove(bullet)

def detect_player_hit(player):
    for bullet in enemy_bullets:
        if player.colliderect(bullet):
            enemy_bullets.remove(bullet)
            return True
    return False
def detect_enemy_hit():
    for bullet in player_bullets:
        for enemy in enemies:
            if enemy.colliderect(bullet):
                player_bullets.remove(bullet)
                enemies.remove(enemy)
                return True
    return False

def win_screen():
    window.fill(BLACK)
    window.blit(background,(0,0))
    text_surf = font.render("YOU WIN!", True, WHITE)
    text_rect = text_surf.get_rect(center=(400,300))
    window.blit(text_surf, text_rect)
    pygame.display.flip()
    
def lose_screen():
    window.fill(BLACK)
    window.blit(background,(0,0))
    text_surf = font.render("YOU LOSE!", True, WHITE)
    text_rect = text_surf.get_rect(center=(400,300))
    window.blit(text_surf, text_rect)
    pygame.display.flip()

def main():
    lives = 3
    running = True
    create_enemies()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    create_player_bullet()

        window.fill(BLACK)
        window.blit(background,(0,0))
        display_enemies()
        create_enemy_bullets()
        draw_enemy_bullet()
        move_enemy_bullets()
        player = create_player()
        draw_player(player=player)
        draw_player_bullets()
        move_player_bullets()
        move_enemy()
        control_player()
        if detect_player_hit(player=player) == True:
            lives -=1
            if lives == 0:
                running = False
        detect_enemy_hit()
        if len(enemies) == 0:
            running=False
        lives_text = f"Lives: {lives}"
        text_surf = font.render(lives_text, True, WHITE)
        text_rect = text_surf.get_rect()
        text_rect.topright = (WIDTH - padding, padding)
        window.blit(text_surf, text_rect)

        pygame.display.flip()
        clock.tick(FPS)
    if lives == 0:
        lose_screen()
    else:
        win_screen()
    time.sleep(2)
if __name__ == "__main__":
    main()