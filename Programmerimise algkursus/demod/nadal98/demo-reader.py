def get_contents(path: str) -> list:
    f = open(path, 'r')

    res = []

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        parts = line.split(',')
        res.append((parts[0], parts[1]))
    f.close()

    res.sort(key=lambda x:x[0])

    return res


def get(cities: list, code: str) -> list:
    res = []

    for city in cities:
        if city[1] == code:
            res.append(city[0])

    return res

def get_better(cities: list, code: str) -> list:
    return [i[0] for i in filter(lambda city: city[1] == code, cities)]

def main():
    path = 'cities.csv'
    cities = get_contents(path)

    print(cities)

    print(get(cities, 'OH'))
    print(get_better(cities, 'OH'))

main()