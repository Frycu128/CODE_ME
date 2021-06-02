#1 Otwórz dowolny plik np. tekst.txt i wklej do niego fragment inwokacji Pana Tadeusza

filename = 'tekst.txt'

with open(filename, 'r', encoding='utf-8') as f:
  content = f.read()
  print(content)

with open('save.txt', 'w') as f:
  f.write('Line 1\n')
  f.write('Line 2\n')
  f.write('Line 3\n')
  f.write('Line 4')

# Wymuś otwarcie pliku Pan Tadeusz w innym kodowaniu niż utf-8:

with open('tekst.txt', 'r', encoding='cp1252') as fopen:
  content = fopen.read()
print(content)
