ex_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

try:
    new_item_index = int(input("Type index of item you want to change [0 - 9]:  "))
    new_item_value = input('Type new item value: ')
    ex_tuple[new_item_index] = new_item_value
except (TypeError, ZeroDivisionError) as e:
    print(f'Error is {e}')
except (ValueError, IndexError) as e:
    print(f'Not correct index or value {e}')
