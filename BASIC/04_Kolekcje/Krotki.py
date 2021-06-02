# 1.  Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę
# krotkę na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np.
# “Mój pies, rasy border collie wabi się Dyzio”.
dog = ('pies', 'malamut', 'atos')
(animal, kind, name) = dog
print(f'Moj {animal} rasy {kind} wabi się {name}.')

# 2. Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
dog = ('pies', 'malamut', 'atos', 'malamut', 'atos', 'atos')
dog = list(dog)
repeated = []

howmany = len(dog)

for i in dog:
    for j in dog[1:]:
        if i == j:
            dog.remove(i)
            if i not in repeated:
                repeated.append(i)

print(f"W krotce elemnty {repeated} się powtarzają.")

# 3. Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.
mynm = (99, 66, 33)
munm = list(mynm)
hmany = len(mynm)
num = hmany-1

for t in range(1, 11):
    shoot = int(input(f"[PRÓBA {t} /10] Podaj jakąś liczbę: "))
    if shoot in mynm:
        if num <= -1:
            break
        else:
            print(f"Trafiłeś liczbę o indeksie {munm.index(shoot)}! Zostały jeszcze {num} liczby do zgadnięcia.")
            num -= 1
    else:
        print("Pudło!")

if num == -1:
    print(f"Zagadłeś wszystkie liczby! --> {mynm}")
else:
    print(f"Zagadłeś tylko {hmany - num-1} liczby!")
