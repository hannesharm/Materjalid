def sum_dict_1(dictionary):
    result = 0

    for element in dictionary:
        result += dictionary[element]

    return result

def sum_dict_2(dictionary):
    result = 0

    for element in dictionary.values():
        result += element

    return result

def sum_dict_3(dictionary):
    return sum(dictionary.values())

d1 = dict(
    pasta=250,
    oad=200,
    suhkruherned=150,
    sidrun=50,
    kikerherned=250
)

print(sum_dict_1(d1))
print(sum_dict_2(d1))
print(sum_dict_3(d1))