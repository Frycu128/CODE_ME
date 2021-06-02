

try:
    list_nb = input('Type few numbers separated with comma:')
    list_nb = list_nb.split(',')
    sum_item = 0
    for i in list_nb:
        sum_item += float(i)
    mid_item = sum_item/len(list_nb)
    print(mid_item)
except (TypeError, ValueError) as e:
    print(f'Error is {e}')
