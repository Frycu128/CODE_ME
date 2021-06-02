from txt_generator import marks_in, random_str, random_number


def longest_str(string_in):
    longest_string = ''
    newest_string = ''
    for nb in range(1, len(string_in)):
        if string_in[nb - 1] == string_in[nb]:
            newest_string += string_in[nb - 1]
        else:
            if len(newest_string) > len(longest_string):
                newest_string += string_in[nb - 1]
                longest_string = newest_string
                newest_string = ''
            else:
                continue
    return f'{longest_string}, {len(longest_string)}'


var = 'banannnnannnnnnnnnanananananaaaana'

print(longest_str(var))

print(longest_str(random_number()))

print(longest_str(random_str(marks_in())))
