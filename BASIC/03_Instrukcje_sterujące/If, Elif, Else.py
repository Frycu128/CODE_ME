# 1. Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty
# i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.
a = int(input('Podaj liczbę:'))
if a % 3 == 0:
    print('Twoja liczba jest podzielna przez 3')
else:
    print('Twoja liczba nie jest podzielna przez 3')

# 2. Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100,
# wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
first = int(input("Podaj pierwszą liczbę całkowitą: "))
second = int(input("Podaj drugą liczbę całkowitą: "))
fcsum = first + second
if fcsum <= 100:
    print('Koniec')
else:
    print(fcsum)

# 3. Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od
# wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i
# mniej - nie warta uwagi.
a = int(input('Na ile od 1 do 10 oceniasz pierwszą książkę?'))
b = int(input('Na ile od 1 do 10 oceniasz drugą książkę?'))
c = int(input('Na ile od 1 do 10 oceniasz trzecią książkę?'))

if (a+b+c)/3 > 7:
    print('bardzo dobry')
elif (a+b+c)/3 == 7 or (a+b+c)/3 >= 5:
    print('przeciętna')
elif (a+b+c)/3 <= 4:
    print('nie warta uwagi')

# 4. Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz
# czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.
many = 'abrakadabra69'
if len(many) >= 5 and many.count('a') > 0:
    print(many.replace('a', 'z'))

# 5. Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość
# conajmniej 8 znaków. Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w
# zależności od rodzaju błędu.
password = input('Podaj hasło:')

if password.islower():
    print('Hasło musi zawierać co najmniej jedną dużą literę.')

if len(password) < 8:
    print('Hasło ma za mało znaków')

if password.isalpha():
    print('Hasło musi zawierać cyfry.')

elif password.isdigit():
    print('Hasło musi zawierać litery')

elif not password.isalnum():
    print('Hasło nie może zawierać spacji ani znaków specjalnych')

# 6.Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl
# komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.
shoot = int(input('Podaj numer od 0 do 100 : '))
if shoot == 5:
    print('gratulacje!')
else:
    print('pudło!')


# 7. Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności
# od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
mass = int(input('Jaka jest Twoja waga [kg]'))
height = float(input('Jaki jest Twój wzrost [m]'))

BMI = int(mass/(height**2))
print('Moje BMI=', BMI)

if 12 <= BMI <= 18.5:
    print('Masz niedowagę.')
elif 30 > BMI >= 25:
    print('Masz nadwagę.')
elif 25 > BMI > 18.5:
    print('BMI w normie')
elif BMI >= 30:
    print('To już otyłość..')
else:
    print('Nie żyjesz albo masz same kości :P')

# 8. Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę.
# Wyświetl liczby od największej do najmniejszej.
one = int(input(['Podaj pierwszą z trzech cyfr: ']))
two = int(input(['Podaj drugą z trzech cyfr: ']))
three = int(input(['Podaj trzecią z trzech cyfr: ']))

if one < two:
    x = one
    one = two
    two = x
if one < three:
    x = one
    one = three
    three = x
if two < three:
    x = two
    two = three
    three = x

print('Ciąg liczb od największej do najmniejszej to :', one, two, three)
