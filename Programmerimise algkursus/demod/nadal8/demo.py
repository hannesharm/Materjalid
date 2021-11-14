l = ['a', 'b', 'c', 'd'] # list
l2 = ['d', 'e', 'f', 'g']
l3 = ['h', 'i', 'j']
d = {3 : 'a', 99 : 'b', 4 : 'c'} # dictionary

teine = l[1]
#print(teine)
element = d[4]
#print(element)

r = range(10)
#print(list(r))

#print(l)
#print(l2)
for index in range(len(l)):
    result = l[index] + l2[index]
    #print(result)


#print(l)
#print(list(range(len(l))))

#print(len(l))
#print(len(l3))

if(len(l) != len(l3)):
    l4 = []
    #print('not same length')


def create_string(l: list) -> str:
    res = ''
    for letter in l:
        res = letter + letter + res
    return res

print(create_string(['aa', 'bb', 'cc']))


print(8 % 5)