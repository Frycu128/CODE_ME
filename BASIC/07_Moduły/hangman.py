import hangman_modules as hm


hidden_word = hm.random_word()
word_indication = ['-'] * len(hidden_word)
print(''.join(word_indication))

for game_round in range(1, 11):
    hidden_word_list = list(hidden_word)
    word_letter = input(f'Runda {game_round}! Podaj literę: ').lower()
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
        print(''.join(word_indication))
    if word_indication.count('-') == 0:
        print(f'Zwycięstwo! Odkryłeś ukryte słowo: {hidden_word}')
        exit()
print(f'Przegrana! Ukrytym słowem było: {hidden_word}')
