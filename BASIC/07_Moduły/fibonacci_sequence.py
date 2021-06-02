def find_value(n):
    fib_seq = [0, 1]
    for position in range(1, n+1):
        fib_seq.append((fib_seq[position]+fib_seq[position-1]))
    return fib_seq[n+1]


print(f'Zadany n-ty wyraz ciągu to: {find_value(50)}')
