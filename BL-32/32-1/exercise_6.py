"""
  Crie uma função que receba os três lado de um triângulo e informe qual o tipo
  de triângulo formado ou "não é triangulo" , caso não seja possível formar um
  triângulo.
"""

def define_triangle(a, b, c):
	if (a < (b + c) and b < (a + c) and c < (a + b)):
  		if (a == b and b == c):
  			return "Triângulo Equilátero"
		if (a == b or a == c or c == b):
		    return "Trângulo Isósceles"
		return "Triângulo Escaleno"
	else:
  		return "Não é triângulo"
