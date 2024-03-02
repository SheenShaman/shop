def sequence(n: int):
    """
    Выводит n первых элементов последовательности 122333444455555… (число повторяется столько раз, чему оно равно)
    """
    line = ''
    for i in range(1, n + 1):
        line += (str(i) * i)

    return line


n = int(input('Введите число n: '))
print(sequence(n))
