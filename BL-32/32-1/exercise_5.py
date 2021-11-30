"""
  Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
  e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma
  função que retorne dois valores em uma tupla contendo a quantidade de latas
  de tinta a serem compradas e o preço total a partir do tamanho de uma parede
  (em m²).
"""
metros_lata = 18 / 3
preco_lata = 80.0


def calcular_latas(tamanho_parede):
    latas_a_comprar = round(tamanho_parede / metros_lata)
    valor_a_pagar = preco_lata * latas_a_comprar
    return (latas_a_comprar, valor_a_pagar)


parede = int(input("Digite o tamanho da parede em m²: "))

print(calcular_latas(parede))
