table = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def table_to_nice_string(grid):
    return "\n".join(["|".join(i) for i in grid])


def make_turn(x, y, sign, grid):
    grid[y - 1][x - 1] = sign


def get_user_input():
    choice = input("select square:")
    letters = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    y = int(choice[1])
    x = letters[choice[0]]
    return x, y


def get_win_status(grid, mark):
    return (mark == grid[0][0] == grid[1][1] == grid[2][2] or
            mark == grid[0][2] == grid[1][1] == grid[2][0] or
            mark == grid[0][0] == grid[0][1] == grid[0][2] or
            mark == grid[1][0] == grid[1][1] == grid[1][2] or
            mark == grid[2][0] == grid[2][1] == grid[2][2] or
            mark == grid[0][0] == grid[1][0] == grid[2][0] or
            mark == grid[0][1] == grid[1][1] == grid[2][1] or
            mark == grid[0][2] == grid[1][2] == grid[2][2])


current = 'x'
while True:
    print(table_to_nice_string(table))
    print("current player {0}".format(current))
    uc = get_user_input()
    make_turn(uc[0], uc[1], current, table)

    if get_win_status(table, current):
        print("winner: " + current)
        print(table_to_nice_string(table))
        break

    if current == 'x':
        current = 'o'
    else:
        current = 'x'

