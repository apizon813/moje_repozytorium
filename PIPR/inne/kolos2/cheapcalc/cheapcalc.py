import sys

import cheapcalc_tools

NUM_ARGS = 4
OPERATIONS = {
    "add": cheapcalc_tools.add,
    "subtract": cheapcalc_tools.subtract,
    "multiply": cheapcalc_tools.multiply,
    "divide": cheapcalc_tools.divide,
}


def print_help_msg() -> None:
    """Prints a help message"""
    print("Correct usage: python3 cheapcalc.py [COMMAND] [ARG1] [ARG2]")
    print("ARG1 and ARG2 should be floats")
    print("Legal values of COMMAND are:")
    for command in OPERATIONS:
        print(" > ", command)


def _format_args(arg_left: str, arg_right: str) -> tuple[float, float]:
    """Formats string arguments for cheapcalc operations"""
    return float(arg_left), float(arg_right)


def _validate_args_number(argv: list[str], num_args: int = NUM_ARGS) -> None:
    """Validates number of arguments for cheapcalc"""
    if len(argv) != num_args:
        raise ValueError(f"wrong number of arguments, expected {num_args}")


def _validate_command(command: str, operations=OPERATIONS) -> None:
    """Checks if cheapcalc was ran using a legal commad"""
    if command not in operations:
        raise ValueError(f"Unknown command: {command}")


def parse_args(argv: list[str], operations=OPERATIONS):
    """Returns a tuple of formatted arguments for running cheapcalc.
    Raises ValueError if arguments are invalid"""
    _validate_args_number(argv)
    _, command, arg_left, arg_right = argv
    _validate_command(command)
    operation = operations[command]
    num_left, num_right = _format_args(arg_left, arg_right)
    return operation, num_left, num_right


def main(argv: list[str]):
    """Parses CLI parameters and runs CheapCalc logic"""
    try:
        operation, arg_left, arg_right = parse_args(argv)
    except ValueError as ex:
        print("Argument error: ", ex)
        print_help_msg()
        return
    try:
        result = operation(arg_left, arg_right)
    except ZeroDivisionError:
        print("Can't divide by 0")
        return
    print(result)  # consider return(result)


if __name__ == "__main__":
    main(sys.argv)
