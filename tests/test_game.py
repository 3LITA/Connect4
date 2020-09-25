import pytest

from src.game import Game


@pytest.fixture
def game():
    return Game(6, 7, ['x', 'o'])


def test_game_not_ended(game):
    game.board = [
        ['o', 'x', ' ', ' ', ' ', ' ', ' '],
        ['x', 'o', ' ', 'x', ' ', ' ', ' '],
        ['o', 'x', 'o', 'o', 'x', ' ', ' '],
        ['x', 'o', 'x', 'x', 'o', ' ', ' '],
        ['o', 'x', 'o', 'o', 'x', ' ', ' '],
        ['x', 'o', 'x', 'x', 'o', 'x', 'x'],
    ]
    assert not game.check_endgame()


def test_endgame_vertical(game):
    game.board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['x', ' ', ' ', ' ', ' ', ' ', ' '],
        ['x', 'o', ' ', ' ', ' ', ' ', ' '],
        ['x', 'o', ' ', ' ', ' ', ' ', ' '],
        ['x', 'o', ' ', ' ', ' ', ' ', ' '],
    ]
    assert game.check_endgame()


def test_endgame_horizontal(game):
    game.board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', 'o', 'o', ' ', ' ', ' ', ' '],
        ['x', 'x', 'x', 'x', ' ', ' ', ' '],
    ]
    assert game.check_endgame()


def test_increasing_diagonal(game):
    game.board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'o', ' ', ' '],
        [' ', ' ', ' ', 'o', 'x', ' ', ' '],
        [' ', ' ', 'o', 'x', 'o', ' ', ' '],
        [' ', 'o', 'o', 'x', 'x', ' ', ' '],
        [' ', 'x', 'x', 'x', 'o', ' ', ' '],
    ]
    assert game.check_endgame()


def test_decreasing_diagonal(game):
    game.board = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'x', ' ', ' ', 'o', ' ', ' '],
        [' ', 'x', 'x', 'o', 'x', ' ', ' '],
        [' ', 'o', 'x', 'x', 'o', ' ', ' '],
        [' ', 'o', 'o', 'x', 'x', ' ', ' '],
        [' ', 'x', 'x', 'x', 'o', ' ', ' '],
    ]
    assert game.check_endgame()
