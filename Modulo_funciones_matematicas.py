
def suma(op1,op2):
	resultado = op1+op2
	print("La suma de los dos valores es:  "
		, resultado)



def resta(op1,op2):
	resultado = op1-op2
	print("La resta de los dos valores es:  "
		, resultado)



def multiplicacion(op1,op2):
	resultado = op1*op2
	#print(
	#	"La multiplicacion de los dos valores es:  "
	#	, resultado)
	return resultado



def division(op1,op2):
	resultado = op1/op2
	print(
		"La division de los dos valores es:  "
		, resultado)


def potencia(base, exponente):
	resultado = op1**op2
	print(
		"La potencia de los dos valores es:  "
		, resultado)


def redondeo(op1):
	
	print(
		"El redondeo del valor es:  "
		, round(op1))


def factorial(op1):

	factor = 1
	
	for i in range(op1-1):
		factor = factor*op1
		op1 = op1-1
	
	return factor 		

def exponencial(op1, n):

	resultado = op1**n 
	
	return resultado

	