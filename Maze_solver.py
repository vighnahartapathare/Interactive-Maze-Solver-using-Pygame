import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

# Colors
DARK_INDIGO = '#1B1A55'     # Deep indigo/blue-violet
VERY_DARK_NAVY = '#03001C'  # Almost black, very dark blue
PALE_CYAN = '#76ABAE'       # Soft teal or desaturated cyan
FOREST_GREEN = '#00712D'    # Rich dark green
BRIGHT_RED = '#F93827'      # Vibrant red
LAVENDER_GRAY = '#9290C3'   # Muted lavender/grayish purple

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Maze Solver")

def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    stack = [(0, 0)]
    visited = set(stack)

    while stack:
        x, y = stack[-1]
        maze[x][y] = 0
        neighbors = [
            (x + dx, y + dy)
            for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]
            if 0 <= x + dx < rows and 0 <= y + dy < cols and (x + dx, y + dy) not in visited
        ]
        random.shuffle(neighbors)

        if neighbors:
            nx, ny = neighbors[0]
            visited.add((nx, ny))
            maze[(x + nx) // 2][(y + ny) // 2] = 0
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

def draw_maze(maze, path=None, start=None, end=None):
    for row in range(ROWS):
        for col in range(COLS):
            color = DARK_INDIGO if maze[row][col] == 0 else VERY_DARK_NAVY
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if path:
        for x, y in path:
            pygame.draw.rect(screen, PALE_CYAN, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if start:
        pygame.draw.rect(screen, FOREST_GREEN, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if end:
        pygame.draw.rect(screen, BRIGHT_RED, (end[1] * CELL_SIZE, end[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def solve_maze(maze, start, end):
    stack = [start]
    visited = set()
    parent = {}

    while stack:
        x, y = stack.pop()

        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]

        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and maze[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))
                parent[(nx, ny)] = (x, y)

                # Animate search
                pygame.draw.rect(screen, LAVENDER_GRAY, (ny * CELL_SIZE, nx * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.display.flip()
                time.sleep(0.002)

    return []

def get_cell_from_mouse(pos):
    x, y = pos
    return y // CELL_SIZE, x // CELL_SIZE

def main():
    maze = generate_maze(ROWS, COLS)
    start = end = None
    path = []
    selecting = True

    running = True
    while running:
        screen.fill(VERY_DARK_NAVY)
        draw_maze(maze, path, start, end)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    maze = generate_maze(ROWS, COLS)
                    start = end = None
                    path = []
                    selecting = True

            elif event.type == pygame.MOUSEBUTTONDOWN and selecting:
                cell = get_cell_from_mouse(pygame.mouse.get_pos())
                if maze[cell[0]][cell[1]] == 1:
                    continue
                if not start:
                    start = cell
                elif not end and cell != start:
                    end = cell
                    path = solve_maze(maze, start, end)
                    selecting = False

    pygame.quit()

if __name__ == "__main__":
    main()
