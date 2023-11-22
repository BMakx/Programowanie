cyfry_slownie = {
    '0': 'zero',
    '1': 'jeden',
    '2': 'dwa',
    '3': 'trzy',
    '4': 'cztery',
    '5': 'pięć',
    '6': 'sześć',
    '7': 'siedem',
    '8': 'osiem',
    '9': 'dziewięć'
}

def word(cyfra):
    return cyfry_slownie.get(cyfra, 'Niepoprawna cyfra')
cyfra = input("Podaj cyfrę (0-9): ")

wynik = word(cyfra)
print(f"{cyfra} = {wynik}")