import pytest

from conway import Game


class TestSolution:
    @pytest.fixture
    def game(self):
        return Game(x=3)

    def test_1(self, game: Game):
        block = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]

        game.start_game(type="user", user_input=block)

        game._tick()
        assert game.board.tolist() == block

        game._tick()
        assert game.board.tolist() == block

    def test_2(self, game):
        blinker_phase1 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        blinker_phase2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

        game.start_game(type="user", user_input=blinker_phase1)

        game._tick()
        assert game.board.tolist() == blinker_phase2

        game._tick()
        assert game.board.tolist() == blinker_phase1
