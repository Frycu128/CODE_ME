def is_in_list_bin(list_of_nb, nb):
    max_index = len(list_of_nb)-1
    middle_index = max_index // 2

    if list_of_nb[middle_index] >= nb:
        for i in range(middle_index):
            if list_of_nb[i] == nb:
                return True
    else:
        for i in range(middle_index, max_index):
            if list_of_nb[i] == nb:
                return True

    return False


data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 12
data.sort()

print(is_in_list_bin(data, elem))
