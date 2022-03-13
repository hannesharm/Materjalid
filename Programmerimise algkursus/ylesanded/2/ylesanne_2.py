def isConvertibleToFloat(value):
    if value.isnumeric(): #-123.4
        return True
    else:
        return False

def isConvertibleToBool(value):
    return bool(value)

def isConvertibleToInt(value):
    if value.isdigit(): #-1234
        return True
    else:
        return False

def main():
    toCheck = input("Give me an input")
    if(isConvertibleToInt(toCheck)):
        print("Input can be converted to integer")
    elif (isConvertibleToFloat(toCheck)):
        print("Input can be converted to float")
    elif(isConvertibleToBool(toCheck)):
        print("Input can be converted to boolean")
    else:
        print("Input cannot be converted to anything")
main()