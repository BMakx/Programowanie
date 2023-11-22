import pickle

męsI = []
żenI = []

def fplec(imie):
    if imie in ['Kosma', 'Barnaba', 'Bonawentura', 'Jarema', 'Kuba']:
        return 'męskie'
    if imie.endswith('a'):
        return 'żeńskie'
    else:
        return 'męskie'

try:
    with open('imiona.pkl', 'rb') as plik:
        dane = pickle.load(plik)
        męsI = dane['męskie']
        żenI = dane['żeńskie']
    print(f"Wczytano imiona z pliku.")

except FileNotFoundError:
    print(f"Plik imiona.pkl nie istnieje.")

for i in range(10):
    imie = input("Podaj imię: ")
    if imie.lower() == 'koniec':
        break
    if imie.isalpha() == False:
        print("To nie jest imię.")
        continue
    imie_cap = imie.capitalize()
    plec = fplec(imie_cap)

    if plec == 'męskie':
        if imie_cap in męsI:
            print(f"Imię {imie_cap} już jest na liście męskich imion.")
        else:
            męsI.append(imie_cap)
    elif plec == 'żeńskie':
        if imie_cap in żenI:
            print(f"Imię {imie_cap} już jest na liście żeńskich imion.")
        else:
            żenI.append(imie_cap)

print("Lista  imion męskich:")
print(męsI)

print("Lista  imion żeńskich:")
print(żenI)

męsI.sort()
żenI.sort()

print("Posortowana lista  imion męskich:")
for imie in męsI:
    print(imie)

print("Posortowana lista  imion żeńskich:")
for imie in żenI:
    print(imie)

lists = {'męskie': męsI, 'żeńskie': żenI}

with open('imiona.pkl', 'wb') as plik:
    pickle.dump(lists, plik)


