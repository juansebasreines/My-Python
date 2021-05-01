
def suma(op1,op2):
	resultado = op1+op2
	print("La suma de los dos valores es:  "
		, resultado)
	return resultado


def resta(op1,op2):
	resultado = op1-op2
	print("La resta de los dos valores es:  "
		, resultado)
	return resultado


def multiplicacion(op1,op2):
	resultado = op1*op2
	"""print(
		"La multiplicacion de los dos valores es:  "
		, resultado)"""
	return resultado



def division(op1,op2):
	resultado = op1/op2
	print(
		"La division de los dos valores es:  "
		, resultado)
	return resultado


def potencia(base, exponente):
	resultado = op1**op2
	print(
		"La potencia de los dos valores es:  "
		, resultado)
	return resultado


def redondeo(op1):
	
	resultado = round(op1)
	
	print(
		"El redondeo del valor es:  "
		, resultado)
	return resultado


def factorial(op1):

	factor = 1
	
	for i in range(op1-1):
		factor = factor*op1
		op1 = op1-1
	
	return factor 		

def exponencial(op1, n):

	resultado = op1**n 
	
	return resultado

	
def repetidor(repeticiones):
	
	resultado = 1

	for i in range(1,repeticiones+1):
		
		a = int(input("escribe un numero rept: ")) 
		
		b = int(input("escribe otro numero rept: "))
		
		resultado = resultado * multiplicacion(a,b)

		factorial(resultado)

	return resultado 

	print(resultado)	

def Arreglo_sin_repeticion(num_total, num_arreglos):
	
	numerador = factorial(num_total)

	denominador = factorial(num_total - num_arreglos)
	 
	print("el arreglo sin repeticion de", num_total ,  
		" \n tomados de a ", num_arreglos ,"\n es" 
		, int(numerador/denominador))

def Arreglo_con_repeticion(num_total, num_arreglos):

	resultado = exponencial(num_total, num_arreglos)

	print("el arreglo de ", num_total, 
	  "\n tomados de a ", num_arreglos,
 	  "\n con repetición es ", resultado)

def permutacion_sin_repeticion(num_total, num_arreglos):

	resultado = factorial(num_total)
			
	print(" la permutación de ", num_total, 
 	  "\n  sin repetición es ", resultado)

def permutacion_con_repeticion(num_total, num_arreglos):

	repeticiones = int(input("""ponga el numero de valores que se repiten """))		
				
	denominador = repetidor(repeticiones)
			
	resultado = factorial(num_total)/denominador 

	print(resultado)

def Combinacion_sin_repeticion(num_total, num_arreglos):
	
	numerador = factorial(num_total)
	
	denominador1 = factorial(num_total - num_arreglos)

	denominador2 = multiplicacion(denominador1, num_arreglos)
	 
	print("el combinación sin repeticion de", num_total, 
	  
		" \n tomados de a ", num_arreglos, 
		"\n es", int(numerador/denominador2))

def Combinacion_con_repeticion(num_total, num_arreglos):
	
	numerador1 = num_total + (num_arreglos - 1)

	numerador2 = factorial(numerador1)

	denominador1 = factorial(numerador1 - num_arreglos)

	fact_num_arreglos = factorial(num_arreglos)

	denominador2 = multiplicacion(denominador1, fact_num_arreglos)
	 
	print("\n el combinación con repeticion de", num_total, 
  
	"\n tomados de a ", num_arreglos, 
	"\n es" , int(numerador2/denominador2))

