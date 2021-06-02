import random


def kpn_judge(user, AI):
    user_win = 0
    AI_win = 0
    if user == 'koniec':
        exit()
    if user == AI:
        AI_win = 1
        user_win = 1
    elif user == 'k' and AI == 'p':
        AI_win = 1
    elif user == 'p' and AI == 'n':
        AI_win = 1
    elif user == 'n' and AI == 'k':
        AI_win = 1
    elif user == 'k' and AI == 'n':
        user_win = 1
    elif user == 'p' and AI == 'k':
        user_win = 1
    elif user == 'n' and AI == 'p':
        user_win = 1
    return user_win, AI_win


def kpn_game():
    print('*' * 60)
    print(f"Witaj w grze kamień(k)/ papier(p)/ nożyce(n)!")
    print('*' * 60, '\n')
    rund_nb = int(input("Podaj liczbę rund: "))
    print()
    seq = ('k', 'p', 'n')
    user = 0
    AI = 0
    draw = 0
    for rund in range(rund_nb):
        shoot = input(f"                     | RUNDA {rund+1 } |\n\n"
                      f"| Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")
        print('*'*60)
        while seq.count(shoot) <= 0:
            print(f'!!!!!!!!!!! "{shoot}"  nie jest możliwym wyborem.. !!!!!!!!!!!!!')
            print('*' * 60)
            shoot = input("Podaj jeden z symboli kamień (k) / papier (p) / nożyce (n): ")

        judge_verdict = kpn_judge(shoot, random.choice(seq))
        if judge_verdict[0] > judge_verdict[1]:
            print(f"Wygrałeś {rund+1} rundę!!!")
            print('*' * 60)
            user += 1
        elif judge_verdict[0] < judge_verdict[1]:
            print(f"Komputer wygrał {rund+1} rundę...")
            print('*' * 60)
            AI += 1
        else:
            print(f"Remis w {rund+1} rundzie!")
            print('*' * 60)
            draw += 1
        print(f"Wynik do tej pory to:\n"
              f"| {user} Zwycięstw   |\n"
              f"| {AI} Przegranych |\n"
              f"| {draw} Remisów)    |\n"
              f" {rund_nb-rund} rundy do końca..")
        print('*' * 60)
    print("\n")
    if user == AI:
        print("| Mecz zakończył się remisem! |")
        print('*' * 60)
    elif user > AI:
        print("|   !!!Zwyciężyłeś!!!   |")
    else:
        print("|   ...Przegrana...   |")
        print('*'*60)


kpn_game()
