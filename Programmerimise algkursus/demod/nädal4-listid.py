a = [1, 3, 4, 5, 1, 42, 32, -4]
print(a)

print('----append----')
a.append(55)
print(a)

a[3] = 'vahetadud'

print('----at index----')
print(a[3])
print(a[-3])

print('----from index 3 to 6 (exclude)----')
print(a[3:6])

print('----from index 3 to end----')
print(a[2:])
print('----before index 2 (exclude)----')
print(a[:2])


a.pop(3)
print(a)

del a[4]
print(a)

print(len(a))

b = ['uus', 'veel uus', 'uuem']
c = a + b
print(c)
d = ['kala']
e = d * 10

print(e)

print('uus' in b)

if ('uus' in b):
    print('tee miskit')


l = [1, 2, 3, 4, 1, 1, 3, 4]

print(l.count(3))

l.insert(3, 10)
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(type(l))


s = 'abcd'
print(s[1])

for letter in s:
    print(s)
