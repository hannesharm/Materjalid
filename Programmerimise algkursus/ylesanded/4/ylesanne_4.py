# kasutage süntaksi nõudeid!

"""
Genereerib dictionary kahe listi põhjal
Võtab esimesest listist võtmed,
teisest listist väärtused
Kui etteantud listid on eripikkusega, siis tagastab tühja sõnastiku.
"""


def create_dict(a: list, b: list) -> dict:
    if len(a) != len(b):
        return {}
    ###
    return {}



l1 = [1, 3, 5]
l2 = ["s", "33", "kalamaja"]
l3 = ["a", "b", "c", "d"]
l4 = ["e", "f", "g", "h"]

print(create_dict(l1, l2))  # => {1: s, 3: 33, 5: kalamaja}
print(create_dict(l3, l4))  # => {a:e, b:f, c:g, d:h}
print(create_dict(l1, l3))  # => {}
