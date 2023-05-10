import pygame
import random
import threading
import time

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Concurrent Drawing")


# Define a list of colors
COLORS = [(255, 0, 0), (255, 128, 0), (255, 255, 0),
          (0, 255, 0), (0, 128, 255), (255, 0, 255)]


# Define a function for drawing a shape with a random color and size
def draw_shape():
    # Set the pen color and size to random values
    color = random.choice(COLORS)
    size = random.randint(10, 100)

    # Draw a random shape with a random size and color
    shape = random.choice(['circle', 'square', 'triangle'])
    if shape == 'circle':
        pygame.draw.circle(screen, color, (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)), size, size//10)
    elif shape == 'square':
        pygame.draw.rect(screen, color, (random.randint(0, WINDOW_WIDTH - size), random.randint(0, WINDOW_HEIGHT - size), size, size), size//10)
    elif shape == 'triangle':
        points = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range(3)]
        for i in range(3):
            # Draw each segment of the triangle in sequence
            pygame.draw.line(screen, color, points[i], points[(i+1)%3], size//10)
            pygame.display.update()
            time.sleep(1)

# Define a function for creating threads that draw shapes
def draw_thread():
    while True:
        # Draw a shape
        draw_shape()

        # Sleep for a random amount of time
        time.sleep(0.5)


# Create 10 threads for drawing shapes
threads = [threading.Thread(target=draw_thread) for i in range(10)]
for t in threads:
    t.start()

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the program
            pygame.quit()
            quit()

    # Update the screen
    pygame.display.update()