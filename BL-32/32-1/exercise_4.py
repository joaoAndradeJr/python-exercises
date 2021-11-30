"""
  Crie uma função que receba uma lista de nomes e retorne
  o nome com a maior quantidade de caracteres.
"""

names_list = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

char_counter = 0
bigger_name = ""

for name in names_list:
    char_counter = len(name)
    if len(bigger_name) < char_counter:
        bigger_name = name


print(bigger_name)
