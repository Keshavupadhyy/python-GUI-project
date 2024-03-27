import pygame
import random
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")
clock = pygame.time.Clock()


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


def start_game():
    all_sprites = pygame.sprite.Group()
    cars = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    player_car = Car()
    all_sprites.add(player_car)
    cars.add(player_car)

    for i in range(8):
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # Game loop
    running = True
    while running:
        # Keep loop running at the right speed
        clock.tick(FPS)

        # Process input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()

        # Check for collisions
        hits = pygame.sprite.spritecollide(player_car, obstacles, False)
        if hits:
            messagebox.showinfo("Game Over", "You crashed! Try again.")
            running = False

        # Draw / render
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # After drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()


# GUI setup
root = tk.Tk()
root.title("Car Racing Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

root.mainloop()
