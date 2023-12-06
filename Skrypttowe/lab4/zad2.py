import math

class Punkt:
    def __init__(pkt, x=0, y=0):
        pkt.x = x
        pkt.y = y

    def odleglosc(pkt):
        return math.sqrt(pkt.x**2 + pkt.y**2)

    def dystans(pkt, inny_punkt):
        dx = pkt.x - inny_punkt.x
        dy = pkt.y - inny_punkt.y
        return math.sqrt(dx**2 + dy**2)
    
    def przesun(pkt, wektor):
        pkt.x += wektor[0]
        pkt.y += wektor[1]

    def __repr__(pkt):
        return f'Punkt({pkt.x}, {pkt.y})'

    def __str__(pkt):
        return f'({pkt.x}, {pkt.y})'

class Kolo(Punkt):
    def __init__(pkt, x=0, y=0, promien=1):
        super().__init__(x, y) # wywołanie klasy ktrórej dziedziczymy
        pkt.promien = promien

    def __repr__(pkt):
        return f'Kolo({pkt.x}, {pkt.y}, promien={pkt.promien})'

    def __str__(pkt):
        return f'Środek: ({pkt.x}, {pkt.y}), Promień: {pkt.promien}'
    
    def obwod(pkt):
        return 2 * math.pi * pkt.promien

    def pole(pkt):
        return math.pi * pkt.promien**2
    
    def przesun(pkt, wektor):
        super().przesun(wektor)
    
    def cz_wsp(pkt, inne_kolo):
        odleglosc_miedzy_srodkami = pkt.dystans(inne_kolo)
        suma_promieni = pkt.promien + inne_kolo.promien

        if odleglosc_miedzy_srodkami > suma_promieni:
            return 'Brak punktów wspólnych'
        elif odleglosc_miedzy_srodkami == suma_promieni:
            return 'Jeden punkt wspólny'
        else:
            return 'Koła się przecinają'

punkt1 = Punkt(2, 3)
punkt2 = Punkt(-1, 2)
kolo1 = Kolo(1, 1, 1)

print(f'Repr punktu: {punkt1.__repr__()}')
print(f'Str punktu: {punkt1.__str__()}')

print(f'Odległość punktu od początku: {punkt1.odleglosc()}')

print(f'Dystans między punktami: {punkt1.dystans(punkt2)}')

print(f'Repr koła: {kolo1.__repr__()}')
print(f'Str koła: {kolo1.__str__()}')
print(f'Obwód koła: {kolo1.obwod()} j')
print(f'Pole koła: {kolo1.pole()} j^2')
kolo1.przesun((1, 1)) #przesuwamy o wektor (1, 1)
print(f'Nowe współrzędne koła: {kolo1.__str__()}')
print(f'{kolo1.cz_wsp(Kolo(2, 1, 1))}.')