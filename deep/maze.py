import random

TOP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def initialize(board, n):
    for i in range(n * n):
        board.append('*')

def index(x, y, n):
    return y * n + x

def check_board(x, y, n):
    return 0 <= x < n and 0 <= y < n

def draw(board, n):
    for y in range(n):
        for x in range(n):
            print(board[index(x, y, n)], end='')
        print()

def generate_maze(board, n, x, y):
    board[index(x, y, n)] = ' '

    directions = [TOP, RIGHT, DOWN, LEFT]
    random.shuffle(directions)

    for direction in directions:
        dx, dy = 0, 0
        if direction == TOP:
            dy = -1
        elif direction == DOWN:
            dy = 1
        elif direction == RIGHT:
            dx = 1
        elif direction == LEFT:
            dx = -1

        x2 = x + (dx << 1)
        y2 = y + (dy << 1)

        if check_board(x2, y2, n) and board[index(x2, y2, n)] == '*':
            board[index(x2 - dx, y2 - dy, n)] = ' '
            generate_maze(board, n, x2, y2)

def find_path_bfs(board, n):
    queue = [(1, 1)]
    board[index(1, 1, n)] = 'A'

    visited = [False] * (n * n)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        current = queue.pop(0)
        visited[index(current[0], current[1], n)] = True

        for i in range(4):
            nx = dx[i] + current[0]
            ny = dy[i] + current[1]

            if (0 <= nx < n and 0 <= ny < n and not visited[index(nx, ny, n)] and board[index(nx, ny, n)] != '*'):
                queue.append((nx, ny))

    board[index(current[0], current[1], n)] = 'B'

def create_maze_2d(n):
    if n % 2 == 0:
        n += 1
    board = []

    initialize(board, n)
    generate_maze(board, n, 1, 1)
    find_path_bfs(board, n)
    draw(board, n)

if __name__ == "__main__":
    random.seed()
    n = 13
    create_maze_2d(n)
