from catboost import CatBoostClassifier
import pickle
import pandas as pd



###game#####
import pygame
import random
import tkinter as tk
from tkinter import messagebox
# Maze dimensions
ROWS = 10
COLS = 10

# Cell types
WALL = '#'
EMPTY = ' '
PLAYER = 'P'
EXIT = 'E'

# Directions
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
over_font = pygame.font.Font('freesansbold.ttf', 64)
# Set up the display
WINDOW_SIZE = (600, 600)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Space Maze Game')

# Load images
player_image = pygame.image.load('./assets/player.png')
exit_image = pygame.image.load('./assets/door.png')
wall_image = pygame.image.load('./assets/obstacle.png')

# Scale images to fit the maze cells
cell_width = WINDOW_SIZE[0] // COLS
cell_height = WINDOW_SIZE[1] // ROWS
player_image = pygame.transform.scale(player_image, (cell_width, cell_height))
exit_image = pygame.transform.scale(exit_image, (cell_width, cell_height))
wall_image = pygame.transform.scale(wall_image, (cell_width, cell_height))

# Define the maze
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', 'E', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]


#maze = [
#    ['#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
#    [' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
#    [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
#    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
#    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
#    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
#    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
#    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
#    [' ', '#', '#', '#', '#', '#', ' ', 'E',' ', '#'],
#    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
#]
# Find player and exit positions
start_row, start_col = None, None
exit_row, exit_col = None, None
for row in range(ROWS):
    for col in range(COLS):
        if maze[row][col] == PLAYER:
            start_row, start_col = row, col
        elif maze[row][col] == EXIT:
            exit_row, exit_col = row, col

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    movement = None

    # Get player movement input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        movement = UP
    elif keys[pygame.K_DOWN]:
        movement = DOWN
    elif keys[pygame.K_LEFT]:
        movement = LEFT
    elif keys[pygame.K_RIGHT]:
        movement = RIGHT

    # Update player position
    if movement is not None:
        new_row = start_row
        new_col = start_col

        if movement == UP:
            new_row -= 1
        elif movement == DOWN:
            new_row += 1
        elif movement == LEFT:
            new_col -= 1
        elif movement == RIGHT:
            new_col += 1

        # Check if the new position is valid
        if 0 <= new_row < ROWS and 0 <= new_col < COLS and maze[new_row][new_col] != WALL:
            maze[start_row][start_col] = EMPTY
            start_row = new_row
            start_col = new_col
            maze[start_row][start_col] = PLAYER

            # Check if the player reached the exit
            if start_row == exit_row and start_col == exit_col:
                messagebox.showinfo('Congratulations!', 'You reached the exit.')
                running = False


            # Delay to slow down the movement (adjust the delay value as needed)
            pygame.time.delay(200)  # Delay for 200 milliseconds

    # Clear the screen
    window.fill(BLACK)

    # Draw the maze
    for row in range(ROWS):
        for col in range(COLS):
            x = cell_width * col
            y = cell_height * row
            if maze[row][col] == WALL:
                window.blit(wall_image, (x, y))
            elif maze[row][col] == PLAYER:
                window.blit(player_image, (x, y))
            elif maze[row][col] == EXIT:
                window.blit(exit_image, (x, y))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
