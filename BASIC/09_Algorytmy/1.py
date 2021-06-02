def nwd(a, b):
    while not b == 0:
        c = a % b
        a, b = b, c

    return a


print(f'Największy wspólny dzielnik wynosi: {nwd(100, 50)}')
