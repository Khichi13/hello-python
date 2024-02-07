def hello(name):
    print("Hello,", name)


def while_loop():
    i = 0
    while True:
        print(i, end=', ')
        i += 1

        if i >= 10:
            break
    print()

def for_loop():
    for i in range(10):
        print(i, end=', ')
    print()


def conditions(n):
    if n > 5:
        print(f'{n} > 5')
    elif n < 5:
        print(f'{n} < 5')
    else:
        print(f'{n} == 5')