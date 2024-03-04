import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
BULLET_SIZE = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 5

# Enemies
enemies = []

# Bullets
bullets = []
bullet_speed = 7


# Function to draw the player, enemies, and bullets
def draw_objects():
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move the player
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
        player.x += player_speed

    # Shoot bullets
    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(player.x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, player.y, BULLET_SIZE, BULLET_SIZE)
        bullets.append(bullet)

    # Move bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Create enemies
    if random.randint(1, 50) == 1:
        enemy = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE)
        enemies.append(enemy)

    # Move enemies
    for enemy in enemies:
        enemy.y += 5
        if enemy.colliderect(player):
            pygame.quit()
            sys.exit()

    # Check for collisions between bullets and enemies
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Update the display
    draw_objects()
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)
