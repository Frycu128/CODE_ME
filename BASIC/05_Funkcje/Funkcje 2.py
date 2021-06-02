# 1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego
# parametru.
def bmi_value(mass, height):
    bmi = mass / (height ** 2)
    return bmi


def bmi_opinion(bmi):
    if 12 <= bmi <= 18.5:
        print('Masz niedowagę.')
    elif 30 > bmi >= 25:
        print('Masz nadwagę.')
    elif 25 > bmi > 18.5:
        print('BMI w normie')
    elif bmi >= 30:
        print('To już otyłość..')
    else:
        print('Nie żyjesz albo masz same kości :P')


mass_person = int(input('Jaka jest Twoja waga [kg]'))
growth = float(input('Jaki jest Twój wzrost [m]'))

bmi_opinion(bmi_value(mass_person, growth))


# 2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość
# z 3 liczb. minimum_of(a, b, c).


def min_nb_in_list(a, b, c):
    if a < b < c:
        print(f"Najmniejszą liczbą jest {a}")
    elif b < a < c:
        print(f"Najmniejszą liczbą jest {b}")
    else:
        print(f"Najmniejszą liczbą jest {c}")


min_nb_in_list(3, 6, 10)


# 3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość ]
# z 3 liczb. maximum_of(a, b, c).


def max_nb_in_list(a, b, c):
    if a > b and a > c:
        print(f"Największą liczbą jest {a}")
    elif b > a and b > c:
        print(f"Największą liczbą jest {b}")
    else:
        print(f"Największą liczbą jest {c}")


max_nb_in_list(9, 5, 7)


# 4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna zwrócić
# komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.


def check_nb(min_value, max_value, nb):
    if max_value > nb > min_value:
        print(f'Liczba {nb} ZNAJDUJE się w zakresie liczb od {min_value} do {max_value}.')
    else:
        print(f'Liczba {nb} NIE ZNAJDUJE się w zakresie liczb od {min_value} do {max_value}.')


min_input = int(input("Podaj najniższą wartość zakresu: "))
max_input = int(input("Podaj najwyższą wartość zakresu: "))
nb_input = int(input("Podaj liczbę do sprawdzenia: "))

check_nb(min_input, max_input, nb_input)


# 5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji.


def cold_warm(nb_of_user, sweet_spot):
    range_to_ss = nb_of_user - sweet_spot
    if 10 >= range_to_ss > 0 and range_to_ss <= 10:
        print('Gorąco!!!')
    elif range_to_ss > 0 and 20 >= range_to_ss > 10:
        print('Ciepło...')
    elif range_to_ss < 0 and range_to_ss >= -10:
        print('Gorąco!!!')
    elif range_to_ss < 0 and -20 <= range_to_ss < -10:
        print('Ciepło...')
    elif range_to_ss > 20 or range_to_ss < -20:
        print('Zimno......')
    else:
        print(f'Trafiłeś! Uryta liczba to {sweet_spot} !')
        return exit()


hidden_nb = int(50)

for i in range(1, 11):
    shoot = int(input(f"Próba nr.{i}! Podaj liczbę: "))
    cold_warm(shoot, hidden_nb)

print(f"Niestety nie trafiłeś.. Ukrytą liczbą była liczba: {hidden_nb}")


# 6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
# -------------- Znajduje się w pliku K-N-P_game -----------------

# 7


def is_visa(card_number):
    if card_number[0] == '4' and len(card_number) in [13, 16]:
        return True
    else:
        return False


def is_mastercard(card_number):
    # numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
    if (51 <= int(card_number[0:2]) <= 55 or 2221 <= int(card_number[0:4]) <= 2720) and len(card_number) == 16:
        return True
    else:
        return False


def is_american_express(card_number):
    if card_number[0:2] in ['34', '37'] and len(card_number) == 15:
        return True
    else:
        return False


card_nb = 0

while len(card_nb) < 13 or len(card_nb) == 14 or len(card_nb) > 16 or not card_nb.isnumeric():
    print("Numer karty musi mieć 13, 15 albo 16 cyfr. Musi też być pisany ciągiem i zawierać same cyfry!")
    card_nb = input('Podaj nr. karty: ')

if is_visa(card_nb):
    print(f'Karta o numerze: {card_nb} to Visa Card')
elif is_mastercard(card_nb):
    print(f'Karta o numerze: {card_nb} to MasterCard')
elif is_american_express(card_nb):
    print(f'Karta o numerze: {card_nb} to American Express')
else:
    print(f'Karta o numerze: {card_nb} nie jest Visa Card, MasterCard ani American Express...')


# 8 + 9


def is_old(year_production):
    if 2021 - year_production >= 25:
        return True
    else:
        return False


def is_oryginal(org_precent):
    if org_precent >= 75:
        return True
    else:
        return False


car_info = {}.fromkeys(['Marka', 'Model', 'Rocznik', "czy_orgyginalny"])

print(car_info)

car_info['Marka'] = input("Podaj markę samochodu: ")
car_info['Model'] = input("Podaj model samochodu: ")
car_info['Rocznik'] = int(input("Podaj rocznik samochodu: "))
car_info['czy_oryginalny'] = int(
    input("Podaj jaki jest stosunek oryginalnych części do nieoryginalnych w procentach: "))

if is_old(car_info['Rocznik']) and is_oryginal(car_info['czy_oryginalny']):
    print(f'Gratulacje! Twój samochód', car_info['Marka'], 'może być zarejestrowany jako zabytek.')
elif is_old(car_info['Rocznik']) and not is_oryginal(car_info['czy_oryginalny']):
    print(f'Twój samochód', car_info['Marka'], 'ma za mało oryginalnych części.')
elif is_oryginal(car_info['czy_oryginalny']) and not is_old(car_info['Rocznik']):
    print(f'Twój samochód', car_info['Marka'], 'jest za młody na rejestrację.')
else:
    print(f'Twój samochód', car_info['Marka'],
          'jest jeszcze zbyt młody na rejestrację jako zabytek i ma za mało org. części.')

# 10
import random


def random_word():
    list_of_words = ['dom', 'mieszkanie', 'centrum', 'ulica', 'latarnia']
    word_random = random.choice(list_of_words)
    return word_random


hidden_word = random_word()
print(hidden_word)
word_indication = ['-'] * len(hidden_word)
print(word_indication)

for game_round in range(1, 11):
    hidden_word_list = list(hidden_word)
    word_letter = input(f'Runda {game_round}! Podaj literę: ').lower()
    print(word_letter)
    while word_letter.isdigit() or not len(word_letter) == 1:
        word_letter = input(f'{word_letter} nie jest pojedynczą literą! Podaj literę: ').lower()
    if hidden_word.count(word_letter) >= 1:
        print(f'Litera {word_letter} występuje w ukrytym wyrazie {hidden_word.count(word_letter)} razy.')
        for i in hidden_word_list:
            if i == word_letter:
                word_indication[hidden_word_list.index(word_letter)] = word_letter
                hidden_word_list[hidden_word_list.index(word_letter)] = 0
        print(''.join(word_indication))
    else:
        print(f'Litera {word_letter} nie występuje w ukrytym wyrazie.')
    if word_indication.count('-') == 0:
        print(f'Zwycięstwo! Odkryłeś ukryte słowo: {hidden_word}')
        exit()
print(f'Przegrana! Ukrytym słowem było: {hidden_word}')
