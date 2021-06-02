def print_calendar(month_data):
    print(f'{month_data[0]}')
    for n in month_data[1]:
        print(f'{n:02d}', end=' ')
        if (n+1) % 7 == 0:
            print()
    print('\n')
    return


year_data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

for m in year_data:
    print_calendar(m)
