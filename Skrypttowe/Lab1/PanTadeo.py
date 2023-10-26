

samogloski2 = "AĄEĘIOUÓY"
spolgloski = "BCĆDFGHJKLŁŁMNŃPRSŚTWZŹŻ"
space = " "
other = ",.!?();:"

tekst = '''Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.
Panno Święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
(Gdy od płaczącej matki pod Twoję opiekę
Ofiarowany, martwą podniosłem powiekę
I zaraz mogłem pieszo do Twych świątyń progu
Iść za wrócone życie podziękować Bogu),
Tak nas powrócisz cudem na Ojczyzny łono.
Tymczasem przenoś moję duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym Niemnem rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych pszenicą, posrebrzanych żytem;
Gdzie bursztynowy świerzop, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane, jakby wstęgą, miedzą
Zieloną, na niej z rzadka ciche grusze siedzą.'''

tekst2 = tekst.upper()
tekst_split = tekst.split('\n')
wers1 = tekst_split[0] 
char = len(tekst)

c_samo = sum(tekst2.count(samo) for samo in samogloski2)
c_spol = sum(tekst2.count(spol) for spol in spolgloski)
c_space = sum(tekst2.count(space) for space in space)
c_other = sum(tekst2.count(other) for other in other)

print("Powyższy tekst składa się z " + str(char) + " znaków.")
print("Zawiera " +  str(c_samo) + " samogłosek." )
print("Zawiera " +  str(c_spol) + " spółgłosek." )
print("Zawiera " +  str(c_space) + " spacji." )
print("Zawiera " +  str(c_other) + " pozostałych znaków." )
print('')
print ("Tekst co dwie litery: " + tekst[::2])
print('')
print ("Tekst co trzy litery: " + tekst[::3])
print('')
print ("Tekst co siedem liter: " + tekst[::7])
print('')
print(wers1)
print(wers1.upper())
print(wers1.replace('Litwo!','Polsko!'))
