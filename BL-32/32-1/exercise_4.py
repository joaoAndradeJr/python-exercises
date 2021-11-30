"""
  Crie uma função que receba uma lista de nomes e retorne
  o nome com a maior quantidade de caracteres.
"""

names_list = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


def search_bigger_name(names):
    char_counter = 0
    bigger_name = ""
    for name in names:
        char_counter = len(name)
        if len(bigger_name) < char_counter:
            bigger_name = name
    return bigger_name


print(search_bigger_name(names_list))
