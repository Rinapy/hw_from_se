from time import asctime


def one_one() -> str:
    """Задание 1 лабараторной №1"""
    print(one_one.__doc__)
    return print('Silence is golden')


def one_two() -> str:
    """Задание 2 лабараторной №1."""
    print(one_two.__doc__)
    date = asctime().split()
    return print(f'{date[0]}\n'
                 f'{date[1]}\n'
                 'Роман'
                 )


def one_three() -> str:
    """Задание 3 лабараторной №1."""
    print(one_three.__doc__)
    for i in range(1, 6):
        print('0' * i)


def one_four(str_long: int, colum_count: int) -> str:
    """Задание 4 лабараторной №1."""
    print(one_four.__doc__)
    for i in range(0, colum_count + 1):
        print('A' * str_long)


def one_five() -> str:
    """Задание 5 лабараторной №1."""
    print(one_five.__doc__)
    count = 10
    line = []
    for i in range(1, 5):
        if i == 1:
            line.append('*' + ' ' * int(count / 2) + '*' + ' ' * int(count / 2) + '*')
            count -= 4
        elif i == 2:
            line.append(' ' * (i - 1) + '*' + ' ' * int(count / 2) + '*' + ' ' * (i - 1) + '*' + ' ' * int(count / 2) + '*' + ' ' * (i - 1))
            count -= 4
        elif i == 3:
            line.append(' ' * (i - 1) + '*' + ' ' * int(count / 2) + '*' + ' ' * (i) + '*' + ' ' * int(count / 2) + '*' + ' ' * (i - 1)) 
        else :
            line.append(' ' * (i - 1) + '*' + ' ' * (i+1) + '*' + ' ' * (i - 1))
    for q in line:
        print(q)
            


def main():
    line = '¯¯' * 10

    one_one()
    print(line)

    one_two()
    print(line)

    one_three()
    print(line)

    one_four(8, 5)
    print(line)

    one_five()
    print(line)


if __name__ == '__main__':
    main()
