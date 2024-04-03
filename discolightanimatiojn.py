import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Disco Light Animation")

# Colors
WHITE = (255, 255, 255)

# Create a clock object to control the frame rate
clock = pygame.time.Clock()


# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Generate random circles with random colors
    for _ in range(50):
        # Random position
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        # Random radius
        radius = random.randint(5, 20)
        # Random color
        color = random_color()
        # Draw the circle
        pygame.draw.circle(screen, color, (x, y), radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(10)  # Adjust the frame rate as needed

# Quit Pygame
pygame.quit()
