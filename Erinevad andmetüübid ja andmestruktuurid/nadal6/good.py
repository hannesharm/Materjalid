from __future__ import annotations

class Row:
    amount: float = 0
    price: float = 0
    name: str = None

    def __str__(self):
        return f"{self.name}, amount: {self.amount}, price: {self.price} "

def get_from_list(l: list, i: int) -> str|None:
    try:
        return l[i].strip()
    except IndexError:
        return None

def get_rows() -> list:
    result = []
    with open('sample2.csv') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split(",")

            item = Row()
            item.amount = float(get_from_list(parts, 0))
            item.price = float(get_from_list(parts, 1))
            item.name = get_from_list(parts, 2)
            print("got item:", item)

            result.append(item)

    return result

def calculate_total(items: list) -> float:
    total = 0
    for item in items:
        total += item.amount * item.price
    return total

items = get_rows()
print("Calculating total...")
print("total:", calculate_total(items))

