import random


def random_quote(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        quote_content = f.readlines()
        q_ln = random.choice(quote_content).split(' - ')
        print(f'"{q_ln[0]}"'.center(150))
        print(f'Autor: {q_ln[1]}'.center(150))


list_choice = input(f'Czy chcesz podać nazwę swojego pliku z cytatami i autorami? (TAK/NIE):')
list_choice = list_choice.lower()
while not list_choice == 'tak' and not list_choice == 'nie':
    list_choice = input(f'Musisz wybrać czy chcesz podać nazwę swojego pliku z cytatami i autorami? (TAK/NIE):')
    list_choice = list_choice.lower()

print()

if list_choice == 'tak':
    file = input('Podaj nazwę pliku z cytatami: ')
else:
    print('*' * 150)
    print('Cytat na dziś to:')
    file = 'cytaty.txt'

random_quote(file)
print('*' * 150)
