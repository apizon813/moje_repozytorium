from random import sample

from lotto_config import LOTTO_LIMIT, NUMBER_PICKS
from lotto_utils import check_player_numbers


class LottoGame:
    """Lotto game representation"""

    def __init__(self, limit: int, number_picks: int):
        """Create a new instance of lotto game."""
        self._player_numbers = set()
        self._winning_numbers = set()
        self._limit_range = range(1, limit + 1)
        self._number_picks = number_picks

    def player_numbers(self):
        """Return the player's numbers."""
        return self._player_numbers

    def winning_numbers(self):
        """Return the winning numbers."""
        return self._winning_numbers

    def _draw_winning_numbers(self):
        """Draw the winning numbers at random out of given range."""
        self._winning_numbers = set(sample(self._limit_range, self._number_picks))

    def _set_player_numbers(self, numbers=None):
        """Set the players numbers or draw them if none were given"""
        if not numbers:
            self._player_numbers = set(sample(self._limit_range, self._number_picks))
        else:
            check_player_numbers(numbers, self._number_picks, self._limit_range)
            self._player_numbers = set(numbers)

    def _matching_numbers(self):
        """Return a subset of player's numbers matching the winning ones."""
        return self._player_numbers.intersection(self._winning_numbers)

    def play(self, numbers=None):
        """Play a round of lotto"""
        self._set_player_numbers(numbers)
        self._draw_winning_numbers()
        matching_numbers = self._matching_numbers()
        return self._results(matching_numbers)

    def _results(self, numbers):
        """Return text description of the results of the round."""
        winning_numbers_str = (
            f"Wylosowane liczby to: "
            f"{', '.join(str(i) for i in self._winning_numbers)}\n"
        )
        player_numbers_str = (
            f"Trafiłeś poprawnie liczby: {', '.join(str(i) for i in numbers)}"
            if len(numbers)
            else "Brak trafionych cyfr"
        )
        return winning_numbers_str + player_numbers_str


def main():
    lotto_game = LottoGame(LOTTO_LIMIT, NUMBER_PICKS)
    while True:
        numbers = None
        print("Witaj w Lotto")
        print("1 - wybierz wlasne liczby")
        print("2 - chybil trafil")
        option = input("> ").strip()
        if not (option == "1" or option == "2"):
            print("Bledna opcja. Sprobuj ponownie")
            continue
        if option == "1":
            print(
                f"Podaj {NUMBER_PICKS} różnych liczb z zakresu od "
                f"1 do {LOTTO_LIMIT} (oddzielonych spacjami)"
            )
            numbers = input("> ").strip()
            numbers = [int(i) for i in numbers.split(" ")]
        results = lotto_game.play(numbers)
        print(results)


if __name__ == "__main__":
    main()
