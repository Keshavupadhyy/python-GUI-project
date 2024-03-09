import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Shooter Game")
clock = pygame.time.Clock()

# Player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 8

# Balloons
balloon_speed = 3
balloon_radius = 30
balloons = []

# Bullets
bullet_speed = 10
bullets = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Sounds
pop_sound = pygame.mixer.Sound("pop.wav")
shoot_sound = pygame.mixer.Sound("shoot.wav")

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])

def draw_balloon(x, y):
    pygame.draw.circle(screen, RED, (x, y), balloon_radius)

def draw_bullet(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, 5, 10])

def draw_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_size // 2, player_y])
                shoot_sound.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Spawn new balloons
    if random.randint(0, 100) < 5:
        balloons.append([random.randint(0, WIDTH - balloon_radius * 2), 0])

    # Move and draw balloons
    for balloon in balloons:
        balloon[1] += balloon_speed
        draw_balloon(balloon[0], balloon[1])

        # Check for collision with bullets
        for bullet in bullets:
            if (
                bullet[0] < balloon[0] < bullet[0] + 5
                and bullet[1] < balloon[1] < bullet[1] + 10
            ):
                balloons.remove(balloon)
                bullets.remove(bullet)
                score += 1
                pop_sound.play()

        # Remove balloons that reach the top of the screen
        if balloon[1] > HEIGHT:
            balloons.remove(balloon)

    # Move and draw bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed
        draw_bullet(bullet[0], bullet[1])

        # Remove bullets that go off the screen
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Draw player and score
    screen.fill((0, 0, 0))
    draw_player(player_x, player_y)
    draw_score(score)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
