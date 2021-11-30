"""
  Faça um programa que, dado um valor n qualquer, tal que n > 1,
  imprima na tela um quadrado feito de asteriscos de lado de tamanho n.
"""

number = int(input("type a integer number bigger than 1: "))

if number <= 1:
    print("invalid number")
else:
    ext_counter = 0
    while ext_counter < number:
        print("*" * number)
        ext_counter += 1
