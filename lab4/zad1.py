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

    def __repr__(pkt):
        return f'Punkt({pkt.x}, {pkt.y})'

    def __str__(pkt):
        return f'([{pkt.x}, {pkt.y}])'

punkt1 = Punkt(1, 1)
punkt2 = Punkt(-2, 4)

print(f'Repr: {punkt1.__repr__()}')
print(f'Str: {punkt1.__str__()}')

# Odległość od początku układu współrzędnych
print(f'Odległość od początku: {punkt1.odleglosc()}')

# Dystans między dwoma punktami
print(f'Dystans między punktami: {punkt1.dystans(punkt2)}')
