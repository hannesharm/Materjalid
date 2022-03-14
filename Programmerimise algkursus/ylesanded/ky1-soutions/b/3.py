import random

"""
Ülesanne: genereeri suvalise pikkusega list, mille sisuks on numbrid.
Listi esimene element on 1 ja järgmine 2, 3, 4 ....
Listi miinimumpikkus on 5, maksimumpikkus 20
prindi list välja
"""

l = []
for i in range(random.randint(5, 21)):
    l.append(i)

print(l)
