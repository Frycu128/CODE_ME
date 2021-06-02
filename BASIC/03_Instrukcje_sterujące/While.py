# 1. Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
temp_F = 0
while temp_F < 201:
    temp_C = (5.0/9.0) * (temp_F - 32)
    print('Temperatura w F =', temp_F, 'na C to:', round(temp_C, 2))
    temp_F = temp_F + 20

# 2. Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
shoot = int(input('Podaj liczbę od 0 do 20: '))
secretnb = 5
while not int(input("Pudło! Podaj inną liczbę od 0 do 20: ")) == secretnb:
    print('Pudło!')

print('Szczał w dziesiątkę!')
