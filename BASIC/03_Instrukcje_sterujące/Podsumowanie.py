# 1. Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.
names = input('Wpisz kilka imion rozdielonych przecinkiem:')
names = names.replace(' ', '').split(',')

for n in names:
    print('Hello', n.title(), '!')

# 2. Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).
text = input('Podaj jakiś tekst: ')
print(text[::2])

x = len(text)
for i in range(1, x, 2):
    print("{}".format(text[i]), end='')

# 3. W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.
textin = input('Podaj ciąg znaków: ')
x = 0
y = 0
z = 0
f = 0

for small in textin:
    if small.islower():
        x = x + 1
    if small.isdigit():
        y = y + 1
    if small.isupper():
        z = z + 1
    if not small.isalnum():
        f = f + 1

print('Małych liter jest:', x, 'Dużych liter jest:', z, 'Cyfr jest:', y, 'Znaków specjalnych i stacji:', f)

# 4.  Napisz grę - kamień (k) / papier (p) / nożyce (n).
import random
rund = int(input("Podaj liczbę rund: "))
seq = ('k', 'p', 'n')
AI = random.choice(seq)
x = 0
y = 0
for runda in range(1, rund+1, 1):
    shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")
    AI = random.choice(seq)
    if shoot == 'koniec':
        exit()
    if shoot == AI:
        print('Remis w', runda, 'rundzie!')

    elif shoot == 'k' and AI == 'p':
        print('Komputer wygrał', runda, 'rundę..')
        y = y + 1

    elif shoot == 'k' and AI == 'n':
        print('Wygrałeś ', runda, 'rundę!')
        x = x + 1

    elif shoot == 'p' and AI == 'n':
        print('Komputer wygrał', runda, 'rundę..')
        y = y + 1

    elif shoot == 'p' and AI == 'k':
        print('Wygrałeś ', runda, 'rundę!')
        x = x + 1

    elif shoot == 'n' and AI == 'k':
        print('Komputer wygrał', runda, 'rundę..')
        y = y + 1

    elif shoot == 'n' and AI == 'p':
        print('Wygrałeś ', runda, 'rundę!')
        x = x + 1

if x > y:
    print('Wygrałeś! Liczba wygranych rund =', x)
elif y > x:
    print('Przegałeś.. Liczba wygranych rund =', x)
else:
    print('Remis!')

# 5 Stwórz grę ciepło zimno.
import random

ran_nb = random.randint(1, 100)
last_user_nb_range = 10
print(ran_nb)

for round_nb in range(6):
    user_nb = input(f'[Runda{round_nb + 1}] Podaj liczbę całkowitą od 1 do 100: ')
    while not user_nb.isdigit():
        user_nb = input(f'{user_nb} nie jest liczbą od 1 do 100. Podaj liczbę: ')
    if int(user_nb) == ran_nb:
        print(f'Wygrałeś! Ukrytą liczbą było {ran_nb}.')
        exit()
    elif abs(int(user_nb)-ran_nb) > last_user_nb_range:
        print('Zimno..')
    elif abs(int(user_nb)-ran_nb) < last_user_nb_range:
        print('Ciepło!')
    else:
        print('Ta sama liczba co poprzednio!')
    last_user_nb_range = abs(int(user_nb)-ran_nb)

print("Przegrałeś! Nie odgadłeś ukrytej liczby..")
