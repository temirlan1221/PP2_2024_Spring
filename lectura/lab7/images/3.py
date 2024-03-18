import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set ball properties
BALL_RADIUS = 25
BALL_SIZE = (BALL_RADIUS * 2, BALL_RADIUS * 2)

# Set initial ball position
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2

# Set movement speed
MOVE_SPEED = 20

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - MOVE_SPEED >= BALL_RADIUS:
                    ball_y -= MOVE_SPEED
            elif event.key == pygame.K_DOWN:
                if ball_y + MOVE_SPEED <= SCREEN_HEIGHT - BALL_RADIUS:
                    ball_y += MOVE_SPEED
            elif event.key == pygame.K_LEFT:
                if ball_x - MOVE_SPEED >= BALL_RADIUS:
                    ball_x -= MOVE_SPEED
            elif event.key == pygame.K_RIGHT:
                if ball_x + MOVE_SPEED <= SCREEN_WIDTH - BALL_RADIUS:
                    ball_x += MOVE_SPEED

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
