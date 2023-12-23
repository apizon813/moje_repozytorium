import pytest
from lotto import LottoGame
from lotto_utils import check_player_numbers
from lotto_errors import (
    WrongCountOfNumbersError,
    NumbersNotInRangeError,
    NumbersNotUniqueError,
)


def test_set_player_numbers_default(monkeypatch):
    def return_six_numbers(f, t):
        return [1, 2, 3, 4, 5, 6]

    lotto_game = LottoGame(50, 6)
    assert not lotto_game.player_numbers()
    monkeypatch.setattr("lotto.sample", return_six_numbers)
    lotto_game._set_player_numbers()
    assert lotto_game.player_numbers() == {1, 2, 3, 4, 5, 6}


def test_set_player_numbers():
    lotto_game = LottoGame(50, 6)
    assert not lotto_game.player_numbers()
    lotto_game._set_player_numbers([1, 2, 3, 4, 5, 6])
    assert lotto_game.player_numbers() == {1, 2, 3, 4, 5, 6}


def test_draw_winning_numbers(monkeypatch):
    def return_six_numbers(f, t):
        return [1, 2, 3, 4, 5, 6]

    lotto_game = LottoGame(50, 6)
    monkeypatch.setattr("lotto.sample", return_six_numbers)
    assert not lotto_game.winning_numbers()
    lotto_game._draw_winning_numbers()
    assert lotto_game.winning_numbers() == {1, 2, 3, 4, 5, 6}


def test_check_player_numbers_valid():
    numbers = [1, 2, 3, 4, 5, 6]
    number_picks = 6
    limit_range = range(1, 50)
    check_player_numbers(numbers, number_picks, limit_range)


def test_check_player_numbers_invalid():
    number_picks = 6
    limit_range = range(1, 50)
    too_little_numbers = [1, 2, 3, 4]
    not_unique_numbers = [1, 2, 3, 4, 5, 5]
    numbers_not_in_range = [1, 100, 200, 300, 450, 2]

    with pytest.raises(WrongCountOfNumbersError):
        check_player_numbers(too_little_numbers, number_picks, limit_range)
    with pytest.raises(NumbersNotUniqueError):
        check_player_numbers(not_unique_numbers, number_picks, limit_range)
    with pytest.raises(NumbersNotInRangeError):
        check_player_numbers(numbers_not_in_range, number_picks, limit_range)
