def calendar_print(days):
    for nb in days:
        if nb == 0:
            continue
        print(f'{nb:02d}', end=' ')
        if nb % 7 == 0:
            print()
    print('\n')
    return


data = [
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
data_dict = dict(data)

for month in data_dict.items():
    print(month[0])
    calendar_print(month[1])
