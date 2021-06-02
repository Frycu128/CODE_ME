import io


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        f.close()
    return text


def write_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('1060')
        f.read()
        return


def create_file(filename):
    with open(filename, 'x', encoding='utf-8') as f:
        f.close()
        return


try:
    print(read_file('not_exists.txt'))

except (FileNotFoundError, FileExistsError) as e:
    print(f'File not exists: {e}')

try:
    print(write_file('test_file.txt'))
except io.UnsupportedOperation as e:
    print(f'You can not read when writing! {e}')

try:
    print(create_file('test_file.txt'))
except FileExistsError as e:
    print(f'File is already exists! error: {e}')
