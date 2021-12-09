# Que tal agora então modelarmos uma televisão?

"""
Nome da abstração - Televisão

atributos
- tamanho
- resolução
- tipo
- cor
- marca
- modelo

comportamentos
- aumentar volume
- diminuir volume
- trocar canal
- ligar/desligar
"""


class Televisao:

    volume = 10
    canal = 5
    ligar = False

    def __init__(self, tamanho, resolucao, tipo, cor, marca, modelo):
        self.tamanho = tamanho
        self.resolucao = resolucao
        self.tipo = tipo
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    def aumentarVolume(self):
        self.volume += 2
        return self.volume

    def diminuirVolume(self):
        self.volume -= 2
        return self.volume

    def ligarDesligar(self):
        self.ligar = not self.ligar
        return self.ligar

    def trocarCanal(self, param):
        if param == "up":
            self.canal += 1
            return self.canal
        self.canal -= 1
        return self.canal


tv = Televisao(55, "4K", "Led", "Preto", "LG", "55TVLGLED")

print(tv.marca)
print(tv.modelo)
print(tv.tamanho)
print(tv.tipo)
print(tv.resolucao)
print(tv.ligarDesligar())
print(tv.aumentarVolume())
print(tv.diminuirVolume())
print(tv.trocarCanal("up"))
print(tv.trocarCanal("down"))
