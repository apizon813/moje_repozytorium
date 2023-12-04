from receipts.client import Client
from receipts.item import Item
from receipts.receipt_position import ReceiptPosition
from receipts.price import Price
from receipts.receipt import Receipt

SECTIONS = 7


class TextColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def section(header="", num=0, sections=SECTIONS, line_length=30):
    print(
        f"{TextColors.OKBLUE}>{TextColors.BOLD} [ {num}/{sections} ] {TextColors.ENDC}",
        end="",
    )
    print(f"{TextColors.OKBLUE}{header.capitalize()}...{TextColors.ENDC}")


def print_ok():
    print(
        f"{TextColors.OKBLUE}> {TextColors.BOLD}{TextColors.OKGREEN}[ OK ]{TextColors.ENDC}"
    )


if __name__ == "__main__":

    print(f"{TextColors.OKGREEN}{TextColors.BOLD}> [ START ] {TextColors.ENDC}")

    section("creating some data...", num=1)
    toilet_paper = Item(name="toilet paper", price=Price((1100)))
    soap = Item(name="soap", price=Price(900))
    rice = Item(name="rice", price=Price.from_float(4.50))
    bananas = Item(name="bananas", price=Price((700)))
    yogurt = Item(name="yogurt", price=Price((550)))
    oranges = Item(name="oranges", price=Price.from_float(12.50))

    if soap.name != "soap":
        raise NotImplementedError

    receipt_a = Receipt(
        [
            ReceiptPosition(3, Item(name="matches", price=Price(100))),
            ReceiptPosition(
                4.2, Item(name="edible gold", price=Price.from_float(1200.99))
            ),
        ]
    )

    if len(receipt_a) != 2:
        raise NotImplementedError

    receipt_b = Receipt(
        [
            ReceiptPosition(1, soap),
            ReceiptPosition(3.5, bananas),
            ReceiptPosition(2, yogurt),
            ReceiptPosition(3, rice),
            ReceiptPosition(2, oranges),
        ]
    )

    receipt_c = Receipt([ReceiptPosition(1, toilet_paper)])
    print_ok()

    section("printing some receipts", num=2)
    print(receipt_a)
    print(">>> total price: ", receipt_a.total_price)
    print(receipt_b)
    for position in receipt_b:
        print(position)
    print_ok()

    section("positions sorted by prices, ascending", num=3)
    sorted_by_prices = sorted(receipt_a)
    for position in sorted_by_prices:
        print(position)
    print_ok()

    section("most expensive positions", num=4)
    top_expensive_positions = receipt_b.top_expensive_positions(num_positions=2)
    print(top_expensive_positions)
    print_ok()

    section("creating and printing a client...", num=5)
    client = Client("John", 1, receipts=[receipt_a, receipt_b, receipt_c])
    print(str(client))
    print(">>> total spending: ", client.total_spending)
    print_ok()

    section("client's receipts sorted by length", num=6)
    receipts_by_length = sorted(client.receipts, key=lambda receipt: len(receipt))
    for receipt in receipts_by_length:
        print(receipt)
    print_ok()

    section("client's receipts sorted by total price, descending", num=7)
    receipts_by_price = sorted(
        client.receipts, key=lambda receipt: receipt.total_price, reverse=True
    )

    for receipt in receipts_by_price:
        print(receipt)
    print_ok()

    print(f"{TextColors.OKGREEN}{TextColors.BOLD}> [ SUCCESS ]{TextColors.ENDC}")
