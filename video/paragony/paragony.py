# słownik produktów dostępnych do kupienia
# klucze - nazwy produktów
# wartości - krotki z ceną w groszach i kategorią podatku
PRODUCTS = {
    'bananas': (499, 'B'),
    'milk': (299, 'A'),
    'oranges': (1803, 'E')
}

# słownik grup podatkowych
# klucze - grupy podatkowe
# wartości - procent podatku
TAXES = {
    'A': 12,
    'B': 8,
    'E': 22
}

# obecna data wypisywana na paragonie
DATE = '25.10.2023'


# argument - cena int w groszach np. 123
# return fstring '1.23'
def get_price(price):
    is_negative = price < 0
    if is_negative:
        price = -price
    zl = price // 100
    gr = price % 100
    if is_negative:
        return f'-{zl}.{gr:>02}'
    else:
        return f'{zl}.{gr:>02}'


# funkcja zwraca cenę całego zamówienia
# argument - {'milk': {'quant': 2, 'price': 598, 'tax': 70, 'group': 'A'}}
# return - cena int w groszach
def get_total_price(order):
    price = 0
    for item in order:
        price += order[item]['price'] * order[item]['quant']
    return price


# funkcaj zwraca podatek od całego zamówienia
# argument - {'milk': {'quant': 2, 'price': 598, 'tax': 70, 'group': 'A'}}
# return - podatek int w groszach
def get_total_tax(order):
    tax = 0
    for item in order:
        tax += order[item]['tax'] * order[item]['quant']
    return tax


def get_products_with_taxes(products, taxes):
    products_with_taxes = {}
    for product in products:
        tax_category = products[product][1]
        tax = int(taxes[tax_category] * products[product][0] / 100)
        products_with_taxes[product] = (products[product][0],
                                        tax, products[product][1])
    return products_with_taxes


def get_order(products_with_taxes):
    order = {}
    still_ordering = True
    while still_ordering:
        product = input("What's your order: ")
        if product == 'end':
            still_ordering = False
        elif product in products_with_taxes:
            order[product] = 0
            quant = int(input("Number of items: "))
            if quant > 0:
                order[product] = {'quant': quant}
                prod_quant = order[product]['quant']
                prod_price = products_with_taxes[product][0]
                prod_tax = products_with_taxes[product][1]
                order[product]['price'] = prod_quant * prod_price
                order[product]['tax'] = prod_quant * prod_tax
                order[product]['group'] = products_with_taxes[product][2]
            else:
                print('Wrong quantity!')
        else:
            print('There is no such item.')
    return order


def get_receipt(order, date):
    receipt = f'{date}\n-------------------------------\n'
    index = 1
    for product in order:
        price = get_price(order[product]['price'])
        receipt += f'{index:>3}. {order[product]["quant"]:2}x'\
            f' {product :15}{price:>5} {order[product]["group"]}\n'
        index += 1
    receipt += '-------------------------------\n'
    price = get_total_price(order)
    tax = get_total_tax(order)
    total = price + tax
    receipt += f'TOTAL PRICE:            {get_price(price):>5}\n'
    receipt += f'TOTAL TAX:              {get_price(tax):>5}\n'
    receipt += f'TOTAL:                  {get_price(total):>5}'
    return receipt


PRODUCTS_WITH_TAXES = (get_products_with_taxes(PRODUCTS, TAXES))
ORDER = {'milk': {'quant': 2, 'price': 598, 'tax': 70, 'group': 'A'}}
# get_order(PRODUCTS_WITH_TAXES)

print(get_receipt(ORDER, DATE))
