# Calcule a média aritmética dos valores contidos em uma lista.

list = [1, 4, 11, 21, 35, 24, 10, 6]


def media(arg):
    sum = 0
    for number in arg:
        sum += number

    return sum / len(list)


print(media(list))
