class WrongCountOfNumbersError(Exception):
    def __init__(self, numbers, correct_numbers):
        super().__init__(
            f"Lotto machine requires {correct_numbers} numbers (got {numbers})"
        )
        self.numbers = numbers


class NumbersNotUniqueError(Exception):
    def __init__(self, numbers):
        super().__init__("Lotto machine requires unique numbers")
        self.numbers = numbers


class NumbersNotInRangeError(Exception):
    def __init__(self, numbers, range):
        super().__init__(
            f"Lotto machine requires numbers between {range.start}"
            f" and {range.stop - 1}"
        )
        self.numbers = numbers
