from __future__ import annotations

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

            row = [get_from_list(parts, 0), get_from_list(parts, 1), get_from_list(parts, 2),  get_from_list(parts, 3)]

            print("got row:", row)

            result.append(row)

    return result

def calculate_total(items: list) -> float:
    total = 0
    for item in items:
        total += float(item[1]) * float(item[2])
    return total

items = get_rows()
print(items)
print("Calculating total...")
print("total:", calculate_total(items))

