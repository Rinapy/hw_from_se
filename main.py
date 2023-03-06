from time import asctime


def one_1() -> None:
    """Задание 1 лабараторной №1"""
    print(one_1.__doc__)
    print('Silence is golden')


def one_2() -> None:
    """Задание 2 лабараторной №1."""
    print(one_2.__doc__)
    date = asctime().split()
    print(f'{date[0]}\n'
          f'{date[1]}\n'
          'Роман')


def one_3() -> None:
    """Задание 3 лабараторной №1."""
    print(one_3.__doc__)
    for i in range(1, 6):
        print('0' * i)


def one_4(str_long: int, colum_count: int) -> None:
    """Задание 4 лабараторной №1."""
    print(one_4.__doc__)
    for i in range(0, colum_count + 1):
        print('A' * str_long)


def one_5() -> None:
    """Задание 5 лабараторной №1."""
    print(one_5.__doc__)
    count = 10
    line = []
    for i in range(1, 5):
        if i == 1:
            line.append('*' + ' ' * int(count / 2) +
                        '*' + ' ' * int(count / 2) + '*')
            count -= 4
        elif i == 2:
            line.append(' ' * (i - 1) + '*' + ' ' * int(count / 2) + '*' +
                        ' ' * (i - 1) + '*' + ' ' * int(count / 2) + '*' + ' ' * (i - 1))
            count -= 4
        elif i == 3:
            line.append(' ' * (i - 1) + '*' + ' ' * int(count / 2) + '*' +
                        ' ' * (i) + '*' + ' ' * int(count / 2) + '*' + ' ' * (i - 1))
        else:
            line.append(' ' * (i - 1) + '*' + ' ' *
                        (i+1) + '*' + ' ' * (i - 1))
    for q in line:
        print(q)


def one_6() -> None:
    """Задание 6 лабараторной №1."""
    print(one_6.__doc__)
    print(1+2-4)


def one_7() -> None:
    """Задание 7 лабараторной №1."""
    print(one_7.__doc__)
    print((1 / 2) + (1 / 4))


def one_8(a: int, b: int) -> None:
    """Задание 8 лабараторной №1."""
    print(one_8.__doc__)
    print((a + (4 * b)) * (a - (3 * b)) + a ** 2)


def one_9(x: int) -> int:
    """Задание 9 лабараторной №1."""
    print(one_9.__doc__)
    print(abs(x) + x ** 5)


def one_10(*args) -> None:
    """Задание 10 лабараторной №1."""
    print(one_10.__doc__)
    for x in args:
        result = (x + 1) ** 2 + 3 * (x + 1)
        print(f'При x = {x}\n'
              f'x = {result:.2f}')


def main():
    line = '¯¯' * 10

    one_1()
    print(line)

    one_2()
    print(line)

    one_3()
    print(line)

    one_4(8, 5)
    print(line)

    one_5()
    print(line)

    one_6()
    print(line)

    one_7()
    print(line)

    one_8(2, 3)
    print(line)

    one_9(-2)
    print(line)

    x_list = [1.7, 3]
    one_10(*x_list)
    print(line)


if __name__ == '__main__':
    main()
