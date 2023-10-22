import random
from dataclasses import dataclass
from itertools import combinations
from typing import List, Literal

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
        self.length = x

    def start_game(
        self,
        type: Literal["simple", "random", "user"],
        **kwargs,
    ):
        if type == "simple":
            self._generate_simple_board()
        elif type == "random":
            self._generate_random_board()
        elif type == "user":
            user_input = kwargs.get("user_input", None)
            assert user_input, "user_input must be provided if user type is selected."
            assert isinstance(user_input, list)
            self._set_user_input_board(user_input=user_input)

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

    def _generate_random_board(self):
        for row in range(self.length):
            for col in range(self.length):
                self.board[row, col] = random.randint(0, 1)

    def _set_user_input_board(self, user_input: List[List[bool]]):
        assert len(user_input) == self.length
        assert len(user_input[0]) == self.length

        for row in range(self.length):
            for col in range(self.length):
                self.board[row, col] = user_input[row][col]

    def _tick(self):
        def get_neighboring_points(point: Point) -> List[Point]:
            moves = [
                Point(x=i[0], y=i[1])
                for i in set(combinations([-1, 1, 0, -1, 1, 0], 2))
                if not (i[0] == 0 and i[1] == 0)
            ]

            neighbors = [point + i for i in moves]
            valid_neighbors = []

            for neighbor in neighbors:
                if (neighbor.x in range(0, self.length)) and (
                    neighbor.y in range(0, self.length)
                ):
                    valid_neighbors.append(neighbor)

            return valid_neighbors

        def get_alive_neighbor_count(point: Point) -> int:
            count = 0
            neighboring_points = get_neighboring_points(point=point)
            for point in neighboring_points:
                if self.board[point.x][point.y] == 1:
                    count += 1
            return count

        new_board = np.zeros((self.length, self.length), dtype=int)

        for row in range(self.length):
            for col in range(self.length):
                alive_neighbor_count = get_alive_neighbor_count(
                    point=Point(x=row, y=col)
                )

                if self.board[row][col] == 1 and alive_neighbor_count <= 1:
                    new_board[row][col] = 0

                if self.board[row][col] == 1 and alive_neighbor_count >= 4:
                    new_board[row][col] = 0

                if self.board[row][col] == 1 and alive_neighbor_count in range(2, 4):
                    new_board[row][col] = 1

                if self.board[row][col] == 0 and alive_neighbor_count == 3:
                    new_board[row][col] = 1

        self.board = new_board
