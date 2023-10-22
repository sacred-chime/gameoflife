from dataclasses import dataclass
from itertools import combinations
from typing import List

import numpy as np


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, new):
        return Point(x=self.x + new.x, y=self.y + new.y)

    def __sub__(self, new):
        return Point(x=self.x - new.x, y=self.y - new.y)


class Game:
    def __init__(self, x: int):
        self.board = np.zeros((x, x), dtype=int)
        self.length = x - 1

    def _generate_simple_board(self):
        for row in range(self.length):
            for col in range(self.length):
                if row % 2 == 0:
                    if col % 2 == 0:
                        self.board[row, col] = 1
                    elif col % 2 == 1:
                        self.board[row, col] = 0
                elif row % 2 == 1:
                    if col % 2 == 0:
                        self.board[row, col] = 0
                    elif col % 2 == 1:
                        self.board[row, col] = 1

    def _tick(self):
        def calculate_neighbors(point: Point) -> List[Point]:
            moves = [
                Point(x=i[0], y=i[1])
                for i in set(combinations([-1, 1, 0, -1, 1, 0], 2))
                if not (i[0] == 0 and i[1] == 0)
            ]

            neighbors = [point + i for i in moves]

            for neighbor in neighbors:
                if (
                    neighbor.x < 0
                    or neighbor.y < 0
                    or neighbor.x > self.length
                    or neighbor.y > self.length
                ):
                    neighbors.remove(neighbor)

            return neighbors

        print(calculate_neighbors(Point(0, 0)))

        return


if __name__ == "__main__":
    game = Game(x=3)
    print(game.board)

    game._generate_simple_board()
    print(game.board)

    game._tick()
