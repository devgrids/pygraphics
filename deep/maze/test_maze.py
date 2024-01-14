import sys
sys.path.append('C:\\dev\\deep')

from pygraphics.config import *
import maze

def main():
    random.seed()
    n = 15
    board = maze.create(n)
    maze.draw(board, n)

    System.camera.set_projection_matrix(0, n-1, 0, n-1)

    def handle():
        delta_time = System.time_manager.get_delta_time()
        for y in range(n):
            for x in range(n):          
                if board[maze.index(x, y, n)] == '*':
                    System.draw_pixel(x,y)

    System.loop(handle)

if __name__ == "__main__":
    main()

