#muutujate nimed:
#ok:
car_count = 3
#not ok:
carCount = 3

#funkstiooninimed:
#ok:
def get_car_count_still_not_ok(cars):
    return 4
#not ok:
def getCarCount(cars):
    return 4


#sisendi ja väljundi näitamine funktsioonides:
def get_person_count(persons: list) -> int:
    return 0

def sum_of_names(name1: str, name2: str) -> str:
    return name1 + name2

def get_car_count(cars: list) -> int:
    return 4

