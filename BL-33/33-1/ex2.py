"""
Para exercitar nossa capacidade de abstração, vamos modelar algumas partes
de um software de geometria. Como poderíamos modelar um objeto retângulo?
🐦 Para ajudar, segue o exemplo do quadrado. Vamos utilizar a seguinte
notação para descrever nossas abstrações:

Nome da abstração
Quadrado

atributos/estados
- lado (tamanho)

comportamentos
- calcular area (lado * lado)
- calcular perímetro (4 * lado)
"""

"""
Nome da abstração - Retangulo

atributos
- altura
- base

comportamentos
- calcular area = (base * altura)
"""


class Retangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcularArea(self):
        return self.base * self.altura
