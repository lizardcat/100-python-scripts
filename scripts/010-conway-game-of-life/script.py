import random
import time
import os

WIDTH, HEIGHT = 40, 20
ALIVE = "O"
DEAD = " "


def random_grid(w, h, p=0.25):
    return [[1 if random.random() < p else 0 for _ in range(w)] for _ in range(h)]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_grid(grid):
    for row in grid:
        print("".join(ALIVE if cell else DEAD for cell in row))


def neighbors(grid, x, y):
    h = len(grid)
    w = len(grid[0])
    count = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx = (x + dx) % w  # wrap horizontally
            ny = (y + dy) % h  # wrap vertically
            count += grid[ny][nx]
    return count


def step(grid):
    h = len(grid)
    w = len(grid[0])
    new = [[0] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            n = neighbors(grid, x, y)
            if grid[y][x] == 1:
                new[y][x] = 1 if (n == 2 or n == 3) else 0
            else:
                new[y][x] = 1 if n == 3 else 0
    return new


def run(iterations=None, delay=0.1):
    grid = random_grid(WIDTH, HEIGHT, p=0.25)
    i = 0
    try:
        while True:
            clear_screen()
            print_grid(grid)
            time.sleep(delay)
            grid = step(grid)
            i += 1
            if iterations is not None and i >= iterations:
                break
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    # Example: run indefinitely. Set iterations=100 to run 100 generations.
    run(iterations=None, delay=0.12)
