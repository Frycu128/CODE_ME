from field_area import circle, rectangle, triangle

how_many = input('Z ilu figur składa się powierchnia? : ')
while not how_many.isdigit():
    how_many = input('Z ilu figur składa się powierchnia? : ')

types_list = ['prostokąt', 'kwadrat', 'koło', 'trójkąt']

total_field = 0

for field in range(int(how_many)):
    field_type = input(f'Podaj {field+1} figurę [koło/ prostokąt/ trójkąt]: ')
    while types_list.count(field_type) == 0:
        field_type = input(f'Podaj {field+1} figurę [koło/ prostokąt/ trójkąt]: ')
    if field_type == types_list[0] or field_type == types_list[1]:
        total_field += rectangle(int(input('Podaj wymiar [a]:')), int(input('Podaj wymiar [b]:')))
    elif field_type == types_list[2]:
        total_field += circle(int(input('Podaj promień [r]:')))
    else:
        total_field += triangle(input('Podaj wymiar [a]:'), input('Podaj wysokość trójkąta [h]:'))

print(total_field)
