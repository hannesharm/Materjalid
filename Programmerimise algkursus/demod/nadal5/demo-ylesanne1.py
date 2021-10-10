def generate(n):
    result = {}

    for i in range(n):
        result[i + 1] = (i + 1) ** 2

    return result


print(generate(1)) # {1: 1}
print(generate(2)) # {1: 1, 2: 4}
print(generate(5)) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(generate(1000))
