from lotto_errors import (
    WrongCountOfNumbersError,
    NumbersNotInRangeError,
    NumbersNotUniqueError,
)


def check_player_numbers(numbers, number_picks, limit_range):
    _if_correct_number_picks(numbers, number_picks)
    _if_unique(numbers, number_picks)
    _if_in_range(numbers, limit_range)


def _if_correct_number_picks(numbers, number_picks):
    if len(numbers) != number_picks:
        raise WrongCountOfNumbersError(numbers, number_picks)


def _if_unique(numbers, number_picks):
    if len(set(numbers)) != number_picks:
        raise NumbersNotUniqueError(numbers)


def _if_in_range(numbers, limit_range):
    if not all(i in limit_range for i in numbers):
        raise NumbersNotInRangeError(numbers, limit_range)
