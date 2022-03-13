table = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def make_turn(x, y, sign, table):
    if table[x - 1][y - 1] == " ":
        table[x - 1][y - 1] = sign
        return True
    return False


def get_user_input():
    choice = input("select square: ")  ## a1 b3 c2
    x_variants = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    y = int(choice[1])
    x_letter = choice[0]
    x = x_variants[x_letter]

    return x, y

x, y = get_user_input()

if make_turn(x, y, "x", table):
    print("worked")
else:
    print("did not")

print(table)
