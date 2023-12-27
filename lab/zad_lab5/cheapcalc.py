""" cheapcalc - a cheap CLI calculator """
import sys
import cheapcalc_tools


def main(argv):
    """Parses CLI parameters and runs CheapCalc logic"""
    _, command, arg_left, arg_right = argv
    operations = {
        "add": cheapcalc_tools.add,
        "subtract": cheapcalc_tools.subtract,
        "multiply": cheapcalc_tools.multiply,
        "divide": cheapcalc_tools.divide
    }
    operation = operations[command]
    result = operation(float(arg_left), float(arg_right))
    print("The result is: ", result)


if __name__ == "__main__":
    main(sys.argv)
