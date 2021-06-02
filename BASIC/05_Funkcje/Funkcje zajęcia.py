#1
def ask_about_mood():
    question = 'How are you?'
    print(question)


def show(user_response):
    print('^^^', user_response, '^^^')

# main part of the code
print('*********')
ask_about_mood()

response = input('--> answer here: ')
show(response)
print('-----END----')

#2
def pair():
    howmany = int(input('ile książek? '))
    bookcol =[]
    for book in range(howmany):
        title = input("podaj tytuł: ")
        grades = int(input("podaj ocenę:"))
        bookcol.append([title, grades])
    return bookcol

books = pair()

print(books)

#3
def pair():
    howmany = int(input('ile książek? '))
    bookcol =[]
    for book in range(howmany):
        title = input("podaj tytuł: ")
        grades = int(input("podaj ocenę:"))
        bookcol.append([title, grades])
    return bookcol

books = pair()

print(books)

def show(bookcol):
    nr = int(input("Podaj nr: "))
    if nr-1 > len(bookcol):
        print("za duża liczba")
    index = nr - 1
    print(books[index])

show(books)

#4
def r2(r):
    return 3.14 * r**2

print(r2(int(input('podaj r: '))))