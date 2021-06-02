# 1. 1▹ Utwórz listę lists_to_dict zawierającą listy 2 elementowe. Przekształć ją w słownik dict_from_list.
lists_to_dict = [
    ['a', 10],
    ['b', 20],
    ['c', 30]
]
dict_from_list = dict(lists_to_dict)
print(dict_from_list)

# 2. Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe. Przekształć ją w słownik dict_from_tuples.
tuples_to_dict = [['kot', 'pies'], ['góra', 'dół'], ['prawo', 'lewo']]
dict_from_tuples = dict(tuples_to_dict)
print(dict_from_tuples)

# 3. Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją
n = 3
x = 5

tab = [[x] * n] * n
print(tab)

for i in range(n):
    print(tab[i])

# 4.  Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
# wypełnioną wynikami mnożenia wiersz × kolumna.
for y in range(1, 11):
    for x in range(1, 11):
        print(x * y, end="\t")
    print()

# 5. W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
pieces = "Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce"
pieces = pieces.lower()
pieces = pieces.replace(",", "")
pieces = pieces.split()
pieces = list(pieces)
print(pieces)

for i in pieces:
    j = pieces.count(i)
    if pieces.count(i) >= 0:
        pieces.remove(i)
    print(f'Słowo: {i} występuje: {j} razy.')

# 6. Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.
days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
nb = list(days.values())
print(nb)
for i in nb:
    if nb.count(i) > 0:
        nb.remove(i)
        if nb.count(i) > 0:
            nb.remove(i)
print(nb)

# 7. Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
for i in example_list:
    if example_list.count(i) > 1:
        example_list.remove(i)

example_tuple = tuple(example_list)
print(example_tuple)
high = 0
low = 10000000000
for n in range(len(example_tuple)):
    if example_tuple[n] > high:
        high = example_tuple[n]

for m in range(len(example_tuple)):
    if example_tuple[m] < low:
        low = example_tuple[m]

print(high, low)

# 8. Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich. Zapisz imiona w wersji
# anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

EU = {
    'Grait Britain': ['Olivia', 'Amelia', 'Isla', 'Ava', 'Emily', 'Isabella', 'Mia', 'Poppy', 'Ella', 'Lily'],
    'Austria': ['Anna', 'Hannah', 'Sophia', 'Emma', 'Marie', 'Lena', 'Sarah', 'Sophie', 'Laura', 'Mia'],
    'Belgium': ['Emma', 'Louise', 'Olivia', 'Elise', 'Alice', 'Juliette', 'Mila', 'Lucie', 'Marie', 'Camille'],
    'Netherlands': ['Anna', 'Emma', 'Tess', 'Sophie', 'Julia', 'Zoë', 'Evi', 'Mila', 'Sara', 'Eva'],
    'Ireland': ['Emily', 'Sophie', 'Emma', 'Grace', 'Lily', 'Sarah', 'Lucy', 'Ava', 'Chloe', 'Katie'],
    'Germany': ['Mia', 'Emma', 'Hannah', 'Sofia', 'Anna', 'Emilia', 'Lina', 'Marie', 'Lena', 'Mila'],
    'Scotland': ['Olivia', 'Emily', 'Isla', 'Sophie', 'Amelia', 'Jessica', 'Ava', 'Ella', 'Charlotte', 'Aria'],
    'Switzerland': ['Emma', 'Mia', 'Sofia', 'Lina', 'Lena', 'Lea', 'Lara', 'Emilia', 'Nina', 'Anna'],
    'Sweden': ['Alice', 'Maja', 'Lilly', 'Ella', 'Wilma', 'Ebba', 'Olivia', 'Astrid', 'Alma', 'Elsa'],
    'Croatia': ['Mia', 'Lucija', 'Sara', 'Ana', 'Ema', 'Petra', 'Lana', 'Nika', 'Marta', 'Elena']
}

names_list = list(EU['Grait Britain'] + EU['Austria'] + EU['Belgium'] + EU['Netherlands'] + EU['Ireland'] +
                  EU['Germany'] + EU['Scotland'] + EU['Switzerland'] + EU['Sweden'] + EU['Croatia'])

print(len(names_list))
print("Imiona które występujące w conajmniej 3 krajach:")
names_set = set(names_list)
names_unique_list = list(names_set)

for i in range(len(names_unique_list)):
    name = names_unique_list[i]
    if names_list.count(name) >= 3:
        print(f"{name}, ", end="")

# 9. 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi
# lub zaczynając od dużej litery)
a = input(f'Użytkowniku 1. Wpisz 4 przedmioty szkolne rozdielonych przecinkiem:')
b = input(f'Użytkowniku 2. Wpisz 4 przedmioty szkolne rozdielonych przecinkiem:')
c = input(f'Użytkowniku 3. Wpisz 4 przedmioty szkolne rozdielonych przecinkiem:')
d = input(f'Użytkowniku 4. Wpisz 4 przedmioty szkolne rozdielonych przecinkiem:')
e = input(f'Użytkowniku 5. Wpisz 4 przedmioty szkolne rozdielonych przecinkiem:')

a = a.lower()
b = b.lower()
c = c.lower()
d = d.lower()
e = e.lower()

a = list(a.split(','))
b = list(b.split(','))
c = list(c.split(','))
d = list(d.split(','))
e = list(e.split(','))

sum_all = (a + b + c + d + e)
allcp = sum_all.copy()
print(sum_all)

for i in allcp:
    for n in range(allcp.count(i) - 1):
        if allcp.count(i) > 1:
            allcp.remove(i)
print(allcp)
allcp2 = allcp.copy()
print(allcp2)
print(len(allcp2))

while len(allcp2) > 1:
    if sum_all.count(allcp2[1]) > sum_all.count(allcp2[0]) or sum_all.count(allcp2[1]) == sum_all.count(allcp2[0]):
        allcp2.remove(allcp2[0])
        print(allcp2)
    elif sum_all.count(allcp2[1]) < sum_all.count(allcp2[0]):
        allcp2.remove(allcp2[1])
        print(allcp2)

print(f'Najpopularniejszy przedmiot to: {allcp2}')

# 10. Użytkownik podaje dowolną liczbę N. Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie
# przyporządkowany jest jej kwadrat (n : n * n).
# Załóżmy, że użytkownik podał N = 8
Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
N = int(input('Wprowadź jakąś liczbę: '))
mydict = {}

for i in range(1, N + 1, 1):
    mydict[i] = i * i

print(mydict)
