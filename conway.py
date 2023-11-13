import random
from dataclasses import dataclass
from itertools import combinations
from typing import List, Literal, Optional

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
        user_input: Optional[List[List[int]]] = None,
    ):
        if type == "simple":
            self._generate_simple_board()
        elif type == "random":
            self._generate_random_board()
        elif type == "user":
            assert isinstance(
                user_input, list
            ), "user_input must be provided if user type is selected."
            self._set_user_input_board(user_input=user_input)

    def _generate_simple_board(self):
        for row in range(self.length):
            for col in range(self.length):
                if (row + col) % 2 == 0:
                    self.board[row, col] = 1
                else:
                    self.board[row, col] = 0

    def _generate_random_board(self):
        for row in range(self.length):
            for col in range(self.length):
                self.board[row, col] = random.randint(0, 1)

    def _set_user_input_board(self, user_input: list):
        assert len(user_input) == self.length
        assert len(user_input[0]) == self.length

        for row in range(self.length):
            for col in range(self.length):
                self.board[row, col] = user_input[row][col]

    def _tick(self):
        def get_alive_neighbor_count(point: Point) -> int:
            moves = [
                Point(x=i[0], y=i[1])
                for i in set(combinations([-1, 1, 0, -1, 1, 0], 2))
                if not (i[0] == 0 and i[1] == 0)
            ]

            potential_neighbors = [point + move for move in moves]
            # Remove OOB points
            valid_neighbors = [
                neighbor
                for neighbor in potential_neighbors
                if 0 <= neighbor.x < self.length and 0 <= neighbor.y < self.length
            ]

            count = 0
            for neighbor in valid_neighbors:
                if self.board[neighbor.x, neighbor.y] == 1:
                    count += 1
            return count

        def calculate_new_board_state(current_state: int, alive_neighbor_count: int):
            if current_state == 1:
                if alive_neighbor_count <= 1:
                    return 0
                elif alive_neighbor_count >= 4:
                    return 0
                elif alive_neighbor_count in range(2, 4):
                    return 1

            if current_state == 0 and alive_neighbor_count == 3:
                return 1

            return current_state

        alive_neighbor_count_board = np.zeros((self.length, self.length), dtype=int)
        for row in range(self.length):
            for col in range(self.length):
                alive_neighbor_count = get_alive_neighbor_count(
                    point=Point(x=row, y=col)
                )
                alive_neighbor_count_board[row, col] = alive_neighbor_count

        get_new_board = np.vectorize(calculate_new_board_state)
        self.board = get_new_board(self.board, alive_neighbor_count_board)
