# E como poderíamos definir um círculo? Qual seu nome, atributos e
# comportamentos?

"""
Nome da abstração - Circulo

atributos
- raio

comportamentos
- cacular area (pi * raio²)
"""


class Circulo:
    PI = 3.1415

    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return self.PI * pow(self.raio, 2)
