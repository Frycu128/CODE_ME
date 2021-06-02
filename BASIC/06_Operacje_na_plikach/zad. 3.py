file = 'cytaty.txt'

with open(file, 'r', encoding='utf-8') as f:
    quote_content = f.readlines()

for i in range(5):
    print(quote_content[i])
