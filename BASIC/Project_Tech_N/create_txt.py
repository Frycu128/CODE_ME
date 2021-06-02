def write_txt(content, head):
    with open(f'{input("Podaj nazwę pliku z danymi wyjściowymi: ")}.txt', 'w', encoding='utf-8') as o:
        o.write(f'{head} \n')
        for line in content:
            o.write(f'{line}     : {content[line]}[kg]\n')
