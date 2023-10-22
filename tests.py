import unittest

import numpy as np

from main import Game


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.game = Game(x=3)

    def test_1(self):
        block = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]

        self.game.start_game(type="user", user_input=block)

        self.game._tick()
        self.assertEqual(self.game.board.tolist(), block)

        self.game._tick()
        self.assertEqual(self.game.board.tolist(), block)

    def test_2(self):
        blinker_phase1 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        blinker_phase2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

        self.game.start_game(type="user", user_input=blinker_phase1)

        self.game._tick()
        self.assertEqual(self.game.board.tolist(), blinker_phase2)

        self.game._tick()
        self.assertEqual(self.game.board.tolist(), blinker_phase1)


if __name__ == "__main__":
    unittest.main()
