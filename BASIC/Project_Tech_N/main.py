import math

from create_txt import write_txt

from read_xlsx import load_data_to_list


# Making dict from file data with first column numbers as keys
def dict_with_parts(data):
    dict_from_data = {}
    for line in data[3:]:
        dict_from_data[line[0]] = line[1: 8]
    dict_from_data.pop(None)

    return dict_from_data


# Making a dict with subassemblys as keys and parts as values
def create_subassembly_dict(data):
    input_dict = dict_with_parts(data)
    output_dict = {}

    subassembly_nb = 0
    subassembly_parts = []

    for item in input_dict:
        if int(item[0]) > subassembly_nb:
            subassembly_parts.clear()
            subassembly_nb = int(item)
        else:
            subassembly_parts.append(input_dict[item])
            output_dict[input_dict[str(subassembly_nb)][0]] = subassembly_parts[0:]

    return output_dict


# Calculating mass for each retail from file
def mass_of_parts(subassembly):
    mass_list = []
    for part in subassembly:
        if part[0][0].lower() == 'b':
            part_clean = part[0].lower().replace('bl.', '').replace(' ', '') \
                .replace('Ø', '').replace('ø', '').split('x')

            if len(part_clean) == 3:
                mass_of_part = float(part_clean[0]) * ((float(part_clean[1]) + 10) / 1000) * \
                               ((float(part_clean[2]) + 10) / 1000) * 7.85 * part[6]
                mass_list.append([mass_of_part, part_clean[0], part[2]])

            elif len(part_clean) == 2:
                mass_of_part = float(part_clean[0]) * ((float(part_clean[1]) + 10) / 1000) * \
                               ((float(part_clean[1]) + 10) / 1000) * 7.85 * part[6]
                mass_list.append([mass_of_part, part_clean[0], part[2]])

        elif part[0][0].lower() == 'p':
            part_clean = part[0].lower().replace('pr.', '').replace('pręt', '').replace('pret', '').replace(' ', '') \
                .replace('Ø', '').replace('ø', '').split('x')

            mass_of_rod = math.pi * ((float(part_clean[0]) / 2) / 1000) ** 2 * ((float(part_clean[1]) + 5) * 7.85) \
                * part[6]
            mass_list.append([mass_of_rod, f'fi{part_clean[0]}', part[2]])

    return mass_list


# Making dict with every type of materials and sums up mass values
def dict_of_materials(mass_list):
    output_data = {}
    for item in mass_list:
        output_data_keys = list(output_data.keys())
        if output_data_keys.count(f'Blacha grubości {item[1]} w o gatunku {item[2]}') > 0:
            output_data[f'Blacha grubości {item[1]} w gatunku {item[2]}'] += item[0]
        elif output_data_keys.count(f'Pręt o średnicy {item[1]} w gatunku {item[2]}') > 0:
            output_data[f'Pręt o średnicy {item[1]} w gatunku {item[2]}'] += item[0]
        else:
            if item[1].isnumeric():
                output_data[f'Blacha grubości {item[1]} w gatunku {item[2]}'] = item[0]
            else:
                output_data[f'Pręt o średnicy {item[1]} w gatunku {item[2]}'] = item[0]

    for p in output_data:
        output_data[p] = round(output_data[p], 2)

    return output_data


input_data = load_data_to_list(f'{input("Podaj nazwę pliku do odczytu:")}.xlsx')
print('Program oblicza...')

construction_name = input_data[0][1]
construction_number = input_data[1][1]

subassembly_dict = create_subassembly_dict(input_data)
subassembly_dict_keys = list(subassembly_dict.keys())

mass_of_construction = []

for sub in subassembly_dict_keys:
    mass_of_subassembly = mass_of_parts(subassembly_dict[sub])
    print(mass_of_subassembly)
    mass_of_construction += mass_of_subassembly

write_txt(dict_of_materials(mass_of_construction), f'{construction_number} \n {construction_name} \n')
