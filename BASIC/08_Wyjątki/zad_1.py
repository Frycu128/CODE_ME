def check(result):
    try:
        x = 10 / result
        print(x)
        print('It is ok!')
    except ValueError as e:
        print('This is not a number')
        print(e)
    except ZeroDivisionError as e:
        print("You can't divide by 0")
        print('Temp result:', 0)
        print(e)
    except SyntaxError as e:
        print('It is string')
        print(e)
    except TypeError as e:
        print('No correct input format')
        print(e)


items = [13, "string", 2.45, 0, "e", True, False, [], {'key': 3}, (), {}]

for i in items:
    check(i)
