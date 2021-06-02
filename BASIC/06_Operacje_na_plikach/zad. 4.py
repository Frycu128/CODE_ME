import random


def random_quote(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        quote_content = f.readlines()
        q_ln = random.choice(quote_content).split(' - ')
        print(f'"{q_ln[0]}"'.center(150))
        print(f'Autor: {q_ln[1]}'.center(150))


print()

for i in range(3):
    print('*'*150)
    random_quote("cytaty.txt")

print('*' * 150)
