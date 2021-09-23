def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


def calculate(a, b, operator):
    if (operator == '+'):
        return add(a, b)
    if (operator == '-'):
        return substract(a, b)
    if (operator == '*'):
        return multiply(a, b)
    if (operator == '/'):
        return divide(a, b)
    else:
        return "Operator can not be " + operator
        #raise ValueError("Operator can not be " + operator)

print(calculate(10, 2, '+'))
print(calculate(10, 2, 'a'))
print(calculate(10, 2, '-'))


