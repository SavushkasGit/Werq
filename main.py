import pygame
import random

# Инициализация pygame
pygame.init()

# Установка размеров окна
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Установка заголовка окна
pygame.display.set_caption("Сорт яблонь")
bg = pygame.image.load("road.jpg")
FPS=120
sound = pygame.mixer.Sound("gonka.wav")


# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Определение позиции и размеров игрока
player_width = 50
player_height = 100
player_x = 375
player_y = 500

def end_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over. Press any key to play again.", True, WHITE)
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(text, text_rect)
    pygame.display.update()
# Определение позиции и размеров врагов
enemy_width = 65
enemy_height = 125
enemy_x = 200
enemy_y = 50

# Определение скорости игрока и врагов
player_speed = 0.3
enemy_speed = 0.25


# Главный цикл игры
running = True
while running:
    def end_screen():
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over. Press any key to play again.", True, WHITE)
        text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(text, text_rect)
        screen.fill(RED)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            waiting = False

    screen.blit(bg, (0, 0))
    player = pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    enemy = pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    #while True:
    sound.play(0)

    # Обработка движений игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        if player_x < 0:
            player_x = 0
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
        if player_x > screen_width - player_width:
            player_x = screen_width - player_width
    elif keys[pygame.K_UP]:
        player_y -= player_speed
        if player_y < 0:
            player_y = 0
    elif keys[pygame.K_DOWN]:
        player_y += player_speed
        if player_y > screen_height - player_height:
            player_y = screen_height - player_height

    # Обработка движений врагов
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_y = 0
        enemy_x = random.randint(0, screen_width - player_width)

    # Обработка столкновений игрока с врагами
    if player.colliderect(enemy):
        end_screen()

    # Обновление экрана
    pygame.display.update()

# Остановка pygame
pygame.quit()