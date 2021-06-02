def factorial_rek(n):
    if n > 1:
        return n * factorial_rek(n - 1)
    elif n <= 1:
        return 1


def factorial_iter(n):
    factorial_out = 1

    if n <= 1:
        return 1
    else:
        for i in range(2, n + 1):
            factorial_out = factorial_out * i

    return factorial_out


n_nb = 1

print(factorial_iter(n_nb), factorial_rek(n_nb))
