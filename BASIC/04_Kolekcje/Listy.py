# 1. Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Elementy na liście posortuj alfabetycznie,
# a następnie wyświetl.
trip = ['namiot', 'śpiwór', 'siekiera']
print(sorted(trip))

# 2. Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
few = []
fewpar = []

for i in range(1, 11):
    few.append(int(input(f"Podaj {i}-ą liczbę: ")))

fewpar = []
print(few)
for x in range(10):
    if few[x] % 2 == 0:
        fewpar.append(few[x])

print(f'Liczbami parzytymi są {fewpar}.')

# 3. Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
listln = input('Wpisz kilka liczb rozdielonych przecinkiem:')
listln = listln.split(',')

if listln[0] == listln[-1]:
    print('Taki sam.')
else:
    print("Różne.")
# 4. Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
few = input('Wpisz 10 liczb rozdielonych przecinkiem:')
few2 = few.split(',')
how_many = len(few2)
mid = int(how_many / 2)
print(few2, mid)
if few2[mid-1] == few2[mid]:
    print(f"Środkowe elementy {few2[mid-1]} oraz {few2[mid]} są takie same!")
else:
    print(f"Środkowe elementy {few2[mid-1]} oraz {few2[mid]} nie są takie same!")

# 5.Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie
# znajdować się imię, nazwisko, zawód, np:
# Dorota, Wellman, dziennikarka
# Adam, Małysz, sportowiec
# Robert, Lewandowski, piłkarz
# Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika
list2D = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
    ]
for row in list2D:
    print('-'.join(row))
