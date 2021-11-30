# Faça um programa que receba um nome e imprima o mesmo na vertical em escada
# invertida


def print_inverted_name(name):
    counter = len(name)
    while counter >= 0:
        print(name[:counter])
        counter -= 1


print_inverted_name("joao")
