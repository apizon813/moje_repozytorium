from typing import Callable, Optional, Sequence, Tuple

from errors import NegativeDegreeError, RepeatedTermError, ZeroCoefficientError


class Polynomial:
    """Polynomial representation"""

    def __init__(self, terms: Optional[Sequence[Tuple[int, float]]] = None):
        """Create a new polynomial given a list of (degree, coefficient)."""
        if terms is None:
            self._terms = {}
            return
        self._terms = dict(sorted(terms, reverse=True))
        if len(terms) != len(self._terms):
            raise RepeatedTermError("Terms in polynomial should be unique")
        if 0 in self._terms.values():
            raise ZeroCoefficientError("Coefficient can't be zero!")
        if any(x < 0 for x in self._terms):
            raise NegativeDegreeError("Degree can't be negative")

    @staticmethod
    def _term_to_string(degree: int, coefficient: float) -> str:
        """Convert a single term to string representation."""
        term = "+" if coefficient > 0 else "-"
        term += str(abs(coefficient)) if abs(coefficient) != 1 else ""
        term += "1" if coefficient == 1 and degree == 0 else ""
        term += "x" if degree > 0 else ""
        term += f"^{degree}" if degree > 1 else ""
        return term

    def __str__(self) -> str:
        result = ""
        for term in self._terms.items():
            result += self._term_to_string(*term)
        if not result:
            return "0"
        return result if result[0] != "+" else result[1:]

    def degree(self) -> int:
        """Return degree of the polynomial."""
        return None if not self._terms else next(iter(self._terms))

    def coefficient(self, degree: int) -> float:
        """Return coefficient for the given degree."""
        return self._terms.get(degree, 0)

    def value(self, x: float) -> float:
        """Calulate the value of polynomial in a given point."""
        return sum(
            coefficient * x**degree for degree, coefficient in self._terms.items()
        )

    def _combine(
        self, other: "Polynomial", combine_function: Callable[[float, float], float]
    ) -> "Polynomial":
        """Combine two polynomials given a specific function."""
        # This function is heavily commented to help students better understand
        # what is going on in here. In general if you don't understand how does
        # a part of this code work then run it under debugger and try to get an
        # intuition for it

        # First we create two sets with degrees for each of the polynomials
        self_keys = set(self._terms.keys())
        other_keys = set(other._terms.keys())

        result_dict = {}
        # We now iterate over all possible degrees
        for degree in self_keys.union(other_keys):
            # We combine coefficients by calling the combination function, if
            # degree isn't present in either polynomial we substitute
            # coefficient value with 0
            combined = combine_function(
                self.coefficient(degree), other.coefficient(degree)
            )
            # And only add this term if the combined coefficient is not zero
            if combined != 0:
                result_dict[degree] = combined

        # To get the final Polynomial we convert the results from dictionary
        # form to the list of tuples using the fact that `dict.items` is an
        # iterator over tuples (key, value)
        return Polynomial(list(result_dict.items()))

    def add(self, other: "Polynomial") -> "Polynomial":
        """Add two polynomials."""

        def _add(a: float, b: float) -> float:
            return a + b

        return self._combine(other, _add)
        # or more succinctly using lambda:
        #  return self._combine(other, lambda a, b: a + b)

    def subtract(self, other: "Polynomial") -> "Polynomial":
        """Subtract ``other`` polynomial from ``self``."""

        def _subtract(a: float, b: float) -> float:
            return a - b

        return self._combine(other, _subtract)
        # or more succinctly using lambda:
        #  return self._combine(other, lambda a, b: a - b)
