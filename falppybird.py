
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 30
GRAVITY = 1
BIRD_JUMP = -15
PIPE_WIDTH = 50
PIPE_HEIGHT = random.randint(100, 300)
PIPE_GAP = 150
PIPE_VELOCITY = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")
background_img = pygame.image.load("background.png")

# Resize images
bird_img = pygame.transform.scale(bird_img, (40, 40))
pipe_img = pygame.transform.scale(pipe_img, (PIPE_WIDTH, PIPE_HEIGHT))

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def reset_pipe():
    return WIDTH, random.randint(100, 300)

def game():
    bird_rect = bird_img.get_rect(center=(100, HEIGHT // 2))
    bird_velocity = 0

    pipe1 = pipe_img.get_rect(topleft=(WIDTH, 0))
    pipe2 = pipe_img.get_rect(topleft=reset_pipe())

    pipes = [pipe1, pipe2]

    score = 0
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity += BIRD_JUMP

        # Bird mechanics
        bird_velocity += GRAVITY
        bird_rect.centery += bird_velocity

        # Pipe mechanics
        for pipe in pipes:
            pipe.x -= PIPE_VELOCITY
            if pipe.right <= 0:
                pipe.x, pipe.y = reset_pipe()
                score += 1

            if bird_rect.colliderect(pipe):
                return score

        # Check if the bird hits the top or bottom
        if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT:
            return score

        # Draw everything
        screen.blit(background_img, (0, 0))
        screen.blit(bird_img, bird_rect)
        for pipe in pipes:
            screen.blit(pipe_img, pipe)

        # Display the score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    score = game()
    print(f"Your score: {score}")
    pygame.quit()
