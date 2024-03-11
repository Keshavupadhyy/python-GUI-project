import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Advanced Robot Animation")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Robot parameters
robot_width = 50
robot_height = 100
robot_x = width // 2 - robot_width // 2
robot_y = height // 2 - robot_height // 2
robot_angle = 0

# Limb parameters
limb_length = 25
limb_width = 10
arm_angle = 0
leg_angle = 0

# Eye parameters
eye_radius = 5

# Background parameters
background_color = (135, 206, 250)
ground_color = (34, 139, 34)

# Main game loop
clock = pygame.time.Clock()

def draw_robot():
    # Draw the body
    rotated_robot = pygame.transform.rotate(pygame.Surface((robot_width, robot_height)), robot_angle)
    rect = rotated_robot.get_rect(center=(robot_x + robot_width // 2, robot_y + robot_height // 2))
    screen.blit(rotated_robot, rect.topleft)

    # Draw arms
    arm1_end = (robot_x + robot_width // 4 + limb_length * math.cos(math.radians(arm_angle)),
                robot_y + robot_height // 4 + limb_length * math.sin(math.radians(arm_angle)))
    arm2_end = (robot_x + 3 * robot_width // 4 + limb_length * math.cos(math.radians(-arm_angle)),
                robot_y + robot_height // 4 + limb_length * math.sin(math.radians(-arm_angle)))
    pygame.draw.line(screen, black, (robot_x + robot_width // 4, robot_y + robot_height // 4), arm1_end, limb_width)
    pygame.draw.line(screen, black, (robot_x + 3 * robot_width // 4, robot_y + robot_height // 4), arm2_end, limb_width)

    # Draw legs
    leg1_end = (robot_x + robot_width // 2 + limb_length * math.cos(math.radians(leg_angle)),
                robot_y + robot_height + limb_length * math.sin(math.radians(leg_angle)))
    leg2_end = (robot_x + robot_width // 2 + limb_length * math.cos(math.radians(-leg_angle)),
                robot_y + robot_height + limb_length * math.sin(math.radians(-leg_angle)))
    pygame.draw.line(screen, black, (robot_x + robot_width // 2, robot_y + robot_height), leg1_end, limb_width)
    pygame.draw.line(screen, black, (robot_x + robot_width // 2, robot_y + robot_height), leg2_end, limb_width)

    # Draw the eyes
    eye1_pos = (robot_x + robot_width // 4, robot_y + robot_height // 4)
    eye2_pos = (robot_x + 3 * robot_width // 4, robot_y + robot_height // 4)
    pygame.draw.circle(screen, red, eye1_pos, eye_radius)
    pygame.draw.circle(screen, red, eye2_pos, eye_radius)

# Background
background_image = pygame.image.load("background.jpg")
background_rect = background_image.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot_x -= 5
    if keys[pygame.K_RIGHT]:
        robot_x += 5
    if keys[pygame.K_UP]:
        robot_y -= 5
    if keys[pygame.K_DOWN]:
        robot_y += 5

    # Update limb angles for animation
    arm_angle += 1
    leg_angle += 1

    # Scroll the background
    background_rect.y += 2
    if background_rect.y > height:
        background_rect.y = 0

    # Clear the screen
    screen.fill(background_color)

    # Draw the background
    screen.blit(background_image, background_rect)
    pygame.draw.rect(screen, ground_color, (0, height - 50, width, 50))

    # Draw the robot
    draw_robot()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
