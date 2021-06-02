items = [1, 2.3, 0, "lala", {"Marta": 12}, (1, "jojo"), 14, 22222.111, "gimmie", {}, False]

try:
    index_nb = int(input("Type index oyu want [0 - 9]:  "))
    test = 1 / items[index_nb]
    print(f'The outcome is: {test}')
except (TypeError, ZeroDivisionError) as e:
    print(f'Error is {e}')
except (ValueError, IndexError) as e:
    print(f'Not correct index {e}')
