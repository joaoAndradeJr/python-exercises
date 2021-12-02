"""
Escreva um programa que retorne uma lista com os valores numéricos de 1 a N,
mas com as seguintes exceções :
Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'
Ex: 3 -> [1, 2, "Fizz"] .
"""


def fizzBuzz(number):
    try:
        list_numbers = []
        counter = 1

        while (counter <= number):
            if (counter % 3 == 0 and counter % 5 == 0):
                list_numbers.append("FizzBuzz")
            elif (counter % 5 == 0):
                list_numbers.append("Buzz")
            elif (counter % 3 == 0):
                list_numbers.append("Fizz")
            else:
                list_numbers.append(counter)
            counter += 1

        return list_numbers
    except ValueError:
        return print("Type a valid number")
