#A mosaic animation inspired by an eagle 
import pygame 
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1600, 1400
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255),
          (128, 0, 0), (0, 128, 0), (0, 0, 128), (128, 128, 0), (128, 0, 128), (0, 128, 128)]

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Mosaic")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load eagle image
eagle_image = pygame.image.load("eagle.gif")
eagle_rect = eagle_image.get_rect()

# Initialize Pygame mixer for sound
pygame.mixer.init()
pygame.mixer.music.load("back_music.mp3")
pygame.mixer.music.set_volume(0.9)

# Function to create a random mosaic shape with harmonic movements
def draw_mosaic(x, y, size, time_elapsed, alpha):
    mosaic_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    color = random.choice(COLORS)
    pygame.draw.rect(mosaic_surface, color + (alpha,), (0, 0, size, size))
    screen.blit(mosaic_surface, (x, y))

# Function to create a random circle with harmonic movements
def draw_circle(x, y, radius, time_elapsed, alpha):
    circle_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    color = random.choice(COLORS)
    pygame.draw.circle(circle_surface, color + (alpha,), (radius, radius), radius)
    screen.blit(circle_surface, (x - radius, y - radius))

# Function to create a random line with harmonic movements
def draw_line(x1, y1, x2, y2, time_elapsed, alpha):
    line_surface = pygame.Surface((abs(x2 - x1), abs(y2 - y1)), pygame.SRCALPHA)
    color = random.choice(COLORS)
    pygame.draw.line(line_surface, color + (alpha,), (0, 0), (abs(x2 - x1), abs(y2 - y1)), random.randint(1, 5))
    screen.blit(line_surface, (min(x1, x2), min(y1, y2)))

# Function to draw an eagle with harmonic movements
def draw_eagle(x, y, time_elapsed):
    harmonic_movement = int(20 * (time_elapsed % 10) * (time_elapsed % 10))  # Increase the speed
    screen.blit(eagle_image, (x, y + harmonic_movement))


# Main game loop
running = True
background_color = BLACK
pygame.mixer.music.play(-1)  # Play background music indefinitely
start_time = time.time()
direction = 1  # 1 for moving from bottom to top, -1for moving from top to bottom

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                background_color = random.choice(COLORS)

    # Change the background color
    screen.fill(background_color)

    # Calculate time elapsed
    time_elapsed = time.time() - start_time

    # Draw mosaic shapes with harmonic movements in the background
    for _ in range(100):
        x = random.randint(0, WIDTH - 50)
        y = random.randint(0, HEIGHT - 50)
        size = random.randint(10, 50)
        alpha = random.randint(50, 150)
        draw_mosaic(x, y, size, time_elapsed, alpha)

    # Draw mosaic shapes with harmonic movements
    for _ in range(100):
        x = random.randint(0, WIDTH - 50)
        y = random.randint(0, HEIGHT - 50)
        size = random.randint(10, 50)
        alpha = random.randint(50, 150)
        draw_mosaic(x, y, size, time_elapsed, alpha)

    # Draw random circles with harmonic movements
    for _ in range(15):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(5, 30)
        alpha = random.randint(50, 150)
        draw_circle(x, y, radius, time_elapsed, alpha)

    # Draw random lines with harmonic movements
    for _ in range(5):
        x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        x2, y2 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        alpha = random.randint(50, 150)
        draw_line(x1, y1, x2, y2, time_elapsed, alpha)

    # Draw an eagle with harmonic movements
    eagle_x = WIDTH // 2 - eagle_rect.width // 2
    eagle_y = HEIGHT // 2 - eagle_rect.height // 2

    if eagle_y < 0 or eagle_y > HEIGHT - eagle_rect.height:
        direction *= -1  # Change direction when eagle reaches top or bottom

    eagle_y += direction * 5  # Adjust the speed as needed
    draw_eagle(eagle_x, eagle_y, time_elapsed)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Stop background music and quit Pygame
pygame.mixer.music.stop()
pygame.quit()
sys.exit()


