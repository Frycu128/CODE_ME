# 1▹ Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
def r2(r):
    return 3.14 * r**2


print("Pole koła wynosi: ", r2(int(input('Podaj promień: '))))

# 2▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.


def even(number):
    verdict = []
    if number % 2 == 0:
        verdict.append("Jest parzysta!")
    else:
        verdict.append("Liczba nie jest parzysta..")
    return verdict


print(even(int(input("Podaj liczbę do sprawdzenia: "))))

# 3▹ Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.


def sum_nb(list_in):
    sum_out = 0
    for nb in range(len(list_in)):
        sum_out += list_in[nb]
    return sum_out


def input_nb(lenght):
    list_of_nb = []
    for i in range(1, lenght + 1):
        list_of_nb.append(int(input(f"Podaj {i}-ą liczbę: ")))
    return list_of_nb


how_much_nr = int(input("Ile liczb chcesz zsumować?"))

sum_of_nb = sum_nb(input_nb(how_much_nr))


print(f"Suma podanych {how_much_nr} liczb wynosi: {sum_of_nb}")


# 4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

def even_list_of_nb(numbers):
    verdict_list = []
    for nb in range(len(numbers)):
        if numbers[nb] % 2 == 0:
            verdict_list.append(numbers[nb])
    return verdict_list


def input_nb(lenght):
    list_of_nb = []
    for i in range(1, lenght + 1):
        list_of_nb.append(int(input(f"Podaj {i}-ą liczbę: ")))
    return list_of_nb


how_much_nr_to_check = int(input("Ile liczb chcesz sprawdzić czy są parzyste?"))
list_of_many_nb = input_nb(how_much_nr_to_check)

print(f"Liczby parzyste to: {even_list_of_nb(list_of_many_nb)}")
