l = [1, 2, 3]
for item in l:
    print(item)

condition = True
counter = 0

while condition:
    counter += 1
    print(counter)
    if (counter == 100):
        condition = False


with open('some.txt', 'a') as f:
    while True:
        f.write('adbfdopja[f')
