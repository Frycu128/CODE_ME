import csv
import random

quote = []

with open('quotes.csv', 'r', encoding='utf-8') as qr:
    quotes_read = csv.DictReader(qr)
    quotes_list = list(quotes_read)

    print(quotes_list)

    for row in quotes_read:
        print(row[1])
