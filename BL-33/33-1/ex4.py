# Vamos mudar um pouco nosso contexto para um sistema de
# vendas de uma cafeteria. Como podemos abstrair um
# pedido composto por vários itens?
# Qual seu nome, atributos e comportamentos?

"""
Nome da abstração
Pedido

atributos/estados
- cliente
- itens consumidos
- forma de pagamento
- descontos

comportamentos
- calcular total
- calcular total com descontos

-----

Nome da abstração
Item

atributos/estados
- nome
- preço

comportamentos
- alterar preço

"""


class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def alterarPreco(self, novoPreco):
        self.preco = novoPreco


class Pedido:

    total = 0

    def __init__(self, cliente, itens, pgto, desconto):
        self.client = cliente
        self.itens = itens
        self.pgto = pgto
        self.desconto = desconto

    def calcularTotal(self):
        for item in self.itens:
            self.total += item.preco

        if self.desconto > 0:
            return self.total - ((self.total / 100) * self.desconto)

        return self.total


cafe = Item("Café", 2.50)
bolo = Item("Bolo", 3.00)

print(cafe.nome)
print(cafe.preco)
print(bolo.nome)
print(bolo.preco)

cliente1 = Pedido("João", [cafe, bolo], "débito", 10)

print(cliente1.client)
for item in cliente1.itens:
    print(item.nome)
    print(item.preco)
print(cliente1.pgto)
print(cliente1.calcularTotal())
