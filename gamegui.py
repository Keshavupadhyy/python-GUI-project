import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# Set up colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Set up the player
player_width, player_height = 50, 50
player_x, player_y = (width - player_width) // 2, height - player_height - 10

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += 5

    # Update the display
    screen.fill(white)
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
