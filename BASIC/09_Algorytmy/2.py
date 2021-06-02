def sum_all_nb(nb_1, nb_2, n):
    sum_out = 0

    for nb in range(n):
        if nb % nb_1 == 0 or nb % nb_2 == 0:
            print(f"Jedna z wartości to: {nb}")
            sum_out += nb

    return sum_out


num_in = [5, 7, 21]

print(f'Suma wszystkich wielokrotności {num_in[0]} lub {num_in[1]} poniżej liczby N = {num_in[2]} '
      f'wynosi: {sum_all_nb(num_in[0], num_in[1], num_in[2])}')
