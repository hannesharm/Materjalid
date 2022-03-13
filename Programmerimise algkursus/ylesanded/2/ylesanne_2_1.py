"""
Andmetüüpide ülesanne
"""
def getFloatValue(value):
    try:
        return float(value)
    except ValueError:
        return 0.0

def getBooleanValue(value):
    ## TODO: lahendus siia:
    ## proovi etteantud väärtust teha boolean tüübiks ja tagasta see tulemus.
    ## rakendus ei tohi visata exceptionit!
    ## kui ei suudeta teha booleaniks, tagasta false
    return False

def getIntValue(value):
    ## TODO: lahendus siia:
    ## proovi etteantud väärtust teha integer tüübiks ja tagasta see tulemus.
    ## rakendus ei tohi visata exceptionit!
    ## kui ei suudeta teha integeriks, tagasta 0
    return 0

def main():
    text = input("Give me an input:")

    floatVal = getFloatValue(text)
    if floatVal != 0.0:
        print("Got float from text:", floatVal)

    intval = getIntValue(text)
    if intval != 0:
        print("Got int from text:", intval)

    boolVal = getBooleanValue(text)
    print("Got bool from text:", boolVal)

main()