import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gun Fire Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load gun image
gun_img = pygame.image.load('download.jpg')
gun_rect = gun_img.get_rect()

# Load fire image
fire_img = pygame.image.load('download.jpg')
fire_rect = fire_img.get_rect()

# Gun position
gun_rect.center = (WIDTH // 2, HEIGHT // 2)

# Fire position
fire_rect.center = (WIDTH // 2 + 50, HEIGHT // 2)

# Animation parameters
fire_animation_counter = 0
fire_animation_speed = 10
fire_animation_max = 10
fire_animation_trigger = 5
fire_active = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_active = True
                fire_animation_counter = 0

    screen.fill(WHITE)

    # Draw gun
    screen.blit(gun_img, gun_rect)

    # Draw fire animation
    if fire_active:
        screen.blit(fire_img, fire_rect)
        fire_animation_counter += 1
        if fire_animation_counter == fire_animation_trigger:
            fire_animation_counter = 0
            fire_rect.center = (WIDTH // 2 + 50, HEIGHT // 2)
        elif fire_animation_counter % fire_animation_speed == 0:
            fire_rect.center = (fire_rect.center[0] + 10, fire_rect.center[1])
            if fire_animation_counter == fire_animation_max:
                fire_active = False

    pygame.display.flip()
