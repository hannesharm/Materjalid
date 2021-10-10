from __future__ import annotations

class Row:

    def __init__(self, amount: float, price: float, name: str):
        self.amount = amount
        self.price = price
        self.name = name

    amount: float = 0
    price: float = 0
    name: str = None

    def get_total(self):
        return self.price * self.amount

    def __str__(self):
        return f"{self.name}, amount: {self.amount}, price: {self.price} "

def get_from_list(l: list, i: int) -> str|None:
    try:
        return l[i].strip()
    except IndexError:
        return None

def get_rows() -> list:
    result = []
    with open('sample1.csv') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split(",")

            item = Row(float(get_from_list(parts, 0)), float(get_from_list(parts, 1)), get_from_list(parts, 2))
            print("got item:", item)

            result.append(item)

    return result

def calculate_total(items: list) -> float:
    return sum(item.get_total() for item in items)

items = get_rows()
print("Calculating total...")
print("total:", calculate_total(items))

