

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        return content


def clean_text(txt):
    exepction_list = ['!', '.', ',', '-', ':', "'", "(", ")", ';']
    clear_text = ''
    for letter in txt:
        if letter == '\n':
            clear_text = clear_text + ' '
        elif exepction_list.count(letter) == 0:
            clear_text = clear_text + letter
    return clear_text


def longest_word(txt):
    longest_word_out = ['a']
    word_list = txt.split(' ')
    for word in word_list:
        if len(word) > len(longest_word_out[0]):
            longest_word_out.clear()
            longest_word_out.append(word)
        elif len(word) == len(longest_word_out[0]):
            longest_word_out.clear()
            longest_word_out.append(word)
    return longest_word_out


text = read_file('tekst.txt')
text = clean_text(text)
print(f'Najdłuższe słowo to: "{longest_word(text)[0]}"')
