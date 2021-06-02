import random

gifts = ['skarpeta', 'telefon', 'rękawiczki', 'słuchawki', 'komputer', 'sweter']
market = ['telefon', 'słuchawki', 'komputer']
wear_shop = ['skarpeta', 'rękawiczki', 'sweter']

gift = random.choice(gifts)

print(f'Losowym przezentem na dzisiaj jest: {gift}')

if market.count(gift) > 0:
    print(f'{gift} możesz kupić w sklepie z elektroniką.')
elif wear_shop.count(gift) > 0:
    print(f'{gift} możesz kupić w sklepie z odzieżą.')
else:
    print('Nie mam dla ciebie rady gdzie szukać tego prezentu..')
