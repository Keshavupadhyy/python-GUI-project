import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Messi Animation")

# Load Messi image
messi = pygame.image.load("messi.png")
messi = pygame.transform.scale(messi, (100, 150))  # Adjust size as needed

# Set initial position
messi_x, messi_y = width // 2 - 50, height // 2 - 75

# Set initial speed
speed_x, speed_y = 5, 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move Messi
    messi_x += speed_x
    messi_y += speed_y

    # Bounce off the edges
    if messi_x <= 0 or messi_x >= width - 100:
        speed_x = -speed_x
    if messi_y <= 0 or messi_y >= height - 150:
        speed_y = -speed_y

    # Fill the background
    screen.fill((255, 255, 255))

    # Draw Messi
    screen.blit(messi, (messi_x, messi_y))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    pygame.time.Clock().tick(30)
