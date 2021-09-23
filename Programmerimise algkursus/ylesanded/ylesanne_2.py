def isConvertibleToFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isConvertibleToBool(value):
    #TODO: check if value is boolean type
    # example value is "True" or "False"
    # returns True, if is boolean
    return False

def isConvertibleToInt(value):
    #TODO: check if value is integer type
    # example value is "3436"
    # returns True, if is integer
    return False

def main():
    toCheck = input("Give me an input")
    if (isConvertibleToFloat(toCheck)):
        print("Input can be converted to float")
    elif(isConvertibleToInt(toCheck)):
        print("Input can be converted to integer")
    elif(isConvertibleToBool(toCheck)):
        print("Input can be converted to boolean")
    else:
        print("Input cannot be converted to anything")
main()