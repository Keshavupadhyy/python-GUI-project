import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rounded Ring Animation")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the rounded ring
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 100)
    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 80)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
