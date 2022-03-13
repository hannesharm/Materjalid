# Muutujatele numbrilise (Integer) väärtuse omistamine
puuPikkus = 20
print(puuPikkus)
puuPikkus = puuPikkus + 10
print(puuPikkus)

print('-------')

# Muutujatele sõnalise (String) väärtuse omistamine
nimi = 'Hannes'
perenimi = 'Härm'
lause = 'Maja on roheline'
lause2 = "Maja on roheline"

taisnimi = nimi + perenimi
print(taisnimi)

print('-------')
# Muutujatele komaga arvulise väärtuse (Float) omistamine
tootehind = 0.1
teinetoode = 0.2
ostukorv = tootehind + teinetoode

# Komaga arvudega tehted ei ole tihti täpsed
print(ostukorv) # -> 0.30000000000000004

print('-------')

# Muutujatele tõeväärtuse omistamine
tomOnAlaealine = False
karlOnAlaealine = False
mariOnAlaealine = True

#näitab, kas tom on alaealine
print(tomOnAlaealine) # -> False

# Tõeväärtustega tehted:
# Järjekord ei ole siinkohal oluline.
# True and False = False. True and True = True. False and False = False.
# True or False = True. True or True = True. False or False = False.

print(karlOnAlaealine and mariOnAlaealine)  #näitab, kas karl ja mari mõlemad on alaealised
print('tulemus:')

# Järjekord muutub oluliseks siis, kui sõnasid 'and' ja 'or' kasutatakse koos.
print(tomOnAlaealine or karlOnAlaealine and mariOnAlaealine) # näitab kas tom või karl ja mari on alaealised.

print('--------')

# input võtab kasutajalt sisendi. Antud juhul küsib: Mis on sinu nimi?
# Peale lause 'Mis on sinu nimi?' küsimist jääb kood seisma ning kasutaja vastust ootama.
nimi = input('Mis on sinu nimi?')

# vastuse, kus kasutab kasutaja sisendit.
print('Tere ' + nimi + '!')

# küsib kasutajalt suvalist numbrit.
number = input('suvaline number:')

if (number.isdigit()): # vastus tuleb alati sõnalise väärtusena. Peame kontrollima, kas vastust on võimalik numbriks ümber teha.
    print('Tulemus = ' + str(int(number) + 3))
elif(nimi == 'Hannes'): # kui vastust ei olnud võimalik numbriks teha, kontrollib, mis oli nime sisend.
    print('Sa taun ei oska lugeda!')
else: # kui vastust ei olnud võimalik numbriks teha ning nimi ei olnud Hannes, siis näitame teadet 'Sisend ei ole number!'
    print('Sisend ei ole number!')
