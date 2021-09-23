shape = input('Please insert geometric shape:')

if (shape == "circle"):
    radius = float(input("Please insert radius in cm:"))
    area = 3.14 * radius ** 2
    print('The area is ' + str(round(area, 2)) + ' cm^2')

elif (shape == 'square'):
    side = float(input("Please insert side length in cm:"))
    #TODO:

##TODO: triangle, rectangle
## Kolmnurk on võrdkülgne, pindala arvutada ühe külje pikkuse järgi!

## käima pannes peab rakendus küsima kasutajalt geomeetrilist kujundit, mille järgi soovitakse pindala arvutada.
## sisestades geomeetriline kujund, peab rakendus küsima vajalikud parameetrid, näiteks ringi puhul raadius, ruudu puhul ühe külje pikkus jne.
## Seejärel näitab rakendus välja arvutatud pindala.

## Kui kasutaja sisestab geomeetrilise kujundi, mida rakenduses defineeritud pole, peab rakendus näitama, et kujundit ei toetata vms.
