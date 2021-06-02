import random


def random_number():
    number = ''
    for nb in range(random.randrange(10, 90)):
        number += str(random.randrange(0, 9))
    number += number[len(number)-1]
    return number


def random_str(marks):
    random_string = ''
    for lenght in range(random.randrange(10, 90)):
        random_string += random.choice(marks)
    random_string += random_string[len(random_string) - 1]
    return random_string


def marks_in():
    marks = []
    for lenght in range(int(input('Podaj ile chcesz wprowadzić znaków: '))):
        marks.append(input(f'Podaj {lenght+1} znak: '))
    return marks
