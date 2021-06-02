# 1. Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Wyświetl nazwę właśnie spakowanego
# przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”
things = ['śpiwór', 'namiot', 'latarka']
for thing in things:
    print('Pod namiot zabieram ', thing)

for i in range(3):
    print('Pod namiot zabieram ', things[i])

print('Great, we are ready')

# 2. Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać.
# Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.
parts = ['masło', 'cebula', 'jajka']
for i in parts:
    print('Dodaj na patelnię', i, '.')
    if i == 'masło':
        print('Aż się rozpuści.')
    elif i == 'cebula':
        print('Smaż aż się zarumieni.')
    elif i == 'jajka':
        print('Przypraw solą i pieprzem. Smaż do ścięcia i podawaj jeszcze ciepłe. Smacznego!')

# 3. Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
sum_number = 0

for nr in range(1, 11):
    sum_number = sum_number + nr
    if nr == 10:
        print(sum_number)
    else:
        print(sum_number, end=', ')

# 4. Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).
number = int(input('Podaj jakąć liczbę: '))
if number > 8 or number < 0:
    print('Liczba nie może być większa niż 8 ani mniejsza od 0.')
elif number == 0:
    print('0! = 1')
    print('Silnia z liczby 0 wynosi 1')
elif number == 1:
    print('1! = 1')
    print('Silnia z liczby 1 wynosi 1')
elif number == 2:
    print('2! = 1 * 2 = 2')
    print('Silnia z liczby 2 wynosi 2')
elif number == 3:
    print('3! = 1 * 2 * 3 = 6')
    print('Silnia z liczby 3 wynosi 6')
elif number == 4:
    print('4! = 1 * 2 * 3 * 4 = 24')
    print('Silnia z liczby 4 wynosi 24')
elif number == 5:
    print('5! = 1 * 2 * 3 * 4 * 5 = 120')
    print('Silnia z liczby 5 wynosi 120')
elif number == 6:
    print('6! = 1 * 2 * 3 * 4 * 5  * 6 = 720')
    print('Silnia z liczby 6 wynosi 720')
elif number == 7:
    print('7! = 1 * 2 * 3 * 4 * 5  * 6 * 7 = 5040')
    print('Silnia z liczby 7 wynosi 5040')
else:
    print('8! = 1 * 2 * 3 * 4 * 5  * 6 * 7 * 8 = 40320')
    print('Silnia z liczby 8 wynosi 40320')
