import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gun Fire Animation")

# Set up colors
white = (255, 255, 255)

# Load gun and bullet images
gun_image = pygame.image.load("gun.png")  # Replace "gun.png" with the path to your gun image
bullet_image = pygame.image.load("bullet.png")  # Replace "bullet.png" with the path to your bullet image

# Get the rect of the gun image
gun_rect = gun_image.get_rect()

# Initialize bullet variables
bullet_x = width // 2
bullet_y = height - 50
bullet_speed = 10
bullet_fired = False

# Set up background
background_image = pygame.image.load("")  # Replace "background.jpg" with the path to your background image
background_rect = background_image.get_rect()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not bullet_fired:
            bullet_fired = True

    # Move the bullet if fired
    if bullet_fired:
        bullet_y -= bullet_speed

    # Update the screen
    screen.blit(background_image, background_rect)
    screen.blit(gun_image, (width // 2 - gun_rect.width // 2, height - gun_rect.height))
    screen.blit(bullet_image, (bullet_x, bullet_y))

    # Check if the bullet is off the screen
    if bullet_y < 0:
        bullet_y = height - 50
        bullet_fired = False

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    pygame.time.Clock().tick(60)
