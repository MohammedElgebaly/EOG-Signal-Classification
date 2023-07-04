import random

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

# Create the maze
maze = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# Add walls
for row in range(ROWS):
    for col in range(COLS):
        if random.random() < 0.3:  # Adjust wall density here
            maze[row][col] = WALL

# Add player and exit
start_row = random.randint(0, ROWS - 1)
start_col = random.randint(0, COLS - 1)
maze[start_row][start_col] = PLAYER

exit_row = random.randint(0, ROWS - 1)
exit_col = random.randint(0, COLS - 1)
maze[exit_row][exit_col] = EXIT

# Game loop
while True:
    # Print the maze
    for row in maze:
        print(' '.join(row))
    print()

    # Get user input
    move = input("Enter your move (w/a/s/d): ")

    # Update player position
    new_row = start_row
    new_col = start_col

    if move == UP:
        new_row -= 1
    elif move == DOWN:
        new_row += 1
    elif move == LEFT:
        new_col -= 1
    elif move == RIGHT:
        new_col += 1

    # Check if the new position is valid
    if 0 <= new_row < ROWS and 0 <= new_col < COLS and maze[new_row][new_col] != WALL:
        maze[start_row][start_col] = EMPTY
        start_row = new_row
        start_col = new_col
        maze[start_row][start_col] = PLAYER

        # Check if the player reached the exit
        if start_row == exit_row and start_col == exit_col:
            print("Congratulations! You reached the exit.")
            break
    else:
        print("Invalid move. Try again.")

