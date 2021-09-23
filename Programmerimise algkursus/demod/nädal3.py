"""a = "kala"
print(type(a))

b = 3
print(type(b))

c = 3.2
print(type(c))

d = True
print(type(d))


inp = input("anna sisend")
print(inp)
print(type(inp))

print("3.3" + "2.4")
print(3.3 + 2.4)
print(3.4 + 3)

num = input("anna number")
print(int(num) + 3)

print("-------------")
"""
def isFloat(a):
    print("In start of fuction isFloat")
    print("a type is ", type(a))
    try:
        print("Trying to convert a to float")
        float(a)
        print("Success")
        return True
    except ValueError:
        print("Coult not convert a to float")
        return False

num = input("anna number")
if (isFloat(num)):
    area = 3.14 * float(num) ** 2
    print('The area is ' + str(round(area, 2)) + ' cm^2')
else:
    print("ei ole number")

num2 = input("anna number")
if (isFloat(num2)):
    area = 3.14 * float(num2) ** 2
    print('The area is ' + str(round(area, 2)) + ' cm^2')
else:
    print("ei ole number")



print([*range(1,10), *range(21, 30)])