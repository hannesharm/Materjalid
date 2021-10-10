a = {
    'maja': 4,
    'auto': 5,
    6: 'asjad',
    0: 1,
    True: False,
    'elemedid': [1, 2, 3],
}

print(a)

print(a['auto'])

print(len(a))

print(type(a))

a['pole'] = 'ei ole'

print(a)

del a['pole']

print(a)


b = {
    'f': 4,
    'a': 1,
    'b': 3,
}

if ('a' in b):
    print('olemas')

if ('g' not in b):
    print('ei ole')

print(list(b))
print(sorted(b))

c = dict(
    kala=3,
    maja=4,
    auto='kala',
    kivi=True,
)

print(c)

