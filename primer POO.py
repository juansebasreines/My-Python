import math 

def CalcularRaiz(num1):
	if num1>0:
		
		return math.sqrt(num1)

	else:
		raise TypeError ("No se pueden números negativos")

op1 = int(input("Escribe un número: "))

try:
	print(CalcularRaiz(op1))
	valor = CalcularRaiz(op1)

except TypeError as NúmeroNegativo:
	print(NúmeroNegativo)
		 

print("La raíz de " + str(op1) + " es " + str(valor))