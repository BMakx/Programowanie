list = []

for i in range(10):
    name = input("Podaj imię: ")
    if name.lower() == 'koniec':
        break
    if  name.isalpha() == False:
        print("To nie name")
        continue #inaczej dodaje do listy2
    namecap = name.capitalize()
    if namecap in list:
        print(f"Imię {namecap} już jest.")
    else:
        list.append(namecap)
print(list)
print("Lista zapisanych imion")

list.sort()
print("\nPosortowana lista zapisanych imion:")
for name in list:
    print(name)

with open('imiona.txt', 'w') as plik:
    for name in list:
        plik.write(name + '\n')