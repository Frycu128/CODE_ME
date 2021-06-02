start = ''
    while start == '':
        start = words[random.randint(0, len(words)-1)]["starts"]
        quote.append(start)

    middle = ''
    while middle == '':
        middle = words[random.randint(0, len(words))]["middles"]
        quote.append(middle)

    qualifier = ''
    while qualifier == '':
        qualifier = words[random.randint(0, len(words))]["qualifiers"]
        quote.append(qualifier)

    finish = ''
    while finish == '':
        finish = words[random.randint(0, len(words))]["finishes"]
        quote.append(finish)

    random_quote = ''.join(quote)
    print(f'\nThe random quote for today is: \n',
          '*'*70, '\n',
          f'{random_quote}'.center(70), '\n',
          '*'*70)