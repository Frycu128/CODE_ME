def random_card_number():
    import random
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    cards_nb_len_visa = [13, 16]

    card_first_numbers_visa = ['4']

    card_first_numbers_mastercard = ['51', '55', '2221', '2720']

    card_first_numbers_americanexpress = ['34', '37']

    card_first_numbers = random.choice(card_first_numbers_visa + card_first_numbers_mastercard +
                                       card_first_numbers_americanexpress)
    number = str(card_first_numbers)

    if card_first_numbers_visa.count(card_first_numbers) == 1:
        for nb in range(random.choice(cards_nb_len_visa) - 1):
            number = number + random.choice(numbers)

    elif card_first_numbers_mastercard.count(card_first_numbers) == 1:
        for nb in range(16 - len(card_first_numbers)):
            number = number + random.choice(numbers)

    else:
        for nb in range(13):
            number = number + random.choice(numbers)

    return number


def is_visa(card_number):
    if card_number[0] == '4' and len(card_number)-1 in [13, 16]:
        return True
    else:
        return False


def is_mastercard(card_number):
    if (51 <= int(card_number[0:2]) <= 55 or 2221 <= int(card_number[0:4]) <= 2720) and len(card_number)-1 == 16:
        return True
    else:
        return False


def is_american_express(card_number):
    if card_number[0:2] in ['34', '37'] and len(card_number)-1 == 15:
        return True
    else:
        return False


def append_nb(filename, card_number):
    with open(filename, 'a+', encoding='utf-8') as f:
        f.write(card_number + '\n')


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.readlines()
        return content


def del_file(filename):
    import os
    os.remove(filename)


def clean_nb(txt):
    for letter in txt:
        if letter == '\n':
            txt.replace('\n', '')
    return txt


# Main program:
how_many_positions = 20

del_file('random_cards_list.txt')
del_file('visa.txt')
del_file('mastercard.txt')
del_file('americanexpress.txt')

for i in range(how_many_positions):
    append_nb('random_cards_list.txt', random_card_number())

card_numbers = read_file('random_cards_list.txt')

for card_nb in card_numbers:
    clean_nb(card_nb)
    if is_visa(card_nb):
        append_nb('visa.txt', card_nb)
    elif is_mastercard(card_nb):
        append_nb('mastercard.txt', card_nb)
    elif is_american_express(card_nb):
        append_nb('americanexpress.txt', card_nb)
