"""TECNICAS DE CONTEO 


	
ARREGLOS
	
	ARREGLO SIN REPETICION (ARREGLO SIMPLE)
		 	
	 	Am,n   = LA FORMULA ES  m!/(m-n)!
	
	 	donde 
	 	m = numero de elementos en total  
	 	n = numero de orden de los arreglos 
	 	(cuantos hay que hallar)
		
		por ejemplo 
		
		A4,2= 12  o A4,3=24

	ARREGLO CON REPETICION 

		Am,n   = LA FORMULA ES m**n 
		m = numero de elementos en total  
	 	n = numero de orden de los arreglos 
	 	(cuantos veces se repite)

	 	por ejemplo 

		A4,2= 16  o A4,3=64

PERMUTACIONES  (IMPORTA EL ORDEN)

	PERMUTACION SIN REPETICION 
		
		Pm      = LA FORMULA ES M!(FACTORIAL DE M)
		m = numero de elementos en total  

		por ejemplo 

		P4=24  o P3=6
	
	PERMUTACION CON REPETICION 

			Pn **n1,n2..
			LA FORMULA ES LA DE ABAJO 
				n!
	n1!x n2! x ... x [n(k-1)]! x [n(k)]!
			
			EXPLICACION 

			Lo que hace es que 
			n = es el numero de todos los elementos 
			n1,n2,..,[n(k)]! = la cantidad de veces que
				un elemento se repite 

			por ejemplo

			cuantas palabras se pueden construir con la 
			palabra "ANANA"

			entonces seria 
					5!=numero de letras 
				   3!x2! 
			esa es la division 
			el 3 porque se repite la A 3 veces
			y el 2 porque se repite la N 2 veces

COMBINACION (NO IMPORTA EL ORDEN)
	
	COMBINACION SIN REPETICION 
		
		Cm,n    = LA FORMULA ES  m!/(m-n)!n!
		
		sirve cuando no importa el orden de ninguna manera

		por ejemplo 

		elegir 3 bolas de billar de 16 que hay
		C16,3 = 560

	COMBINACION CON REPETICION 
		
		C´m,n    = LA FORMULA ES Cm+(n-1),n

		por ejemplo

		¿Cuántas fichas diferentes tiene el juego domino 
		que usa los números 0, 1, 2, 3, 4, 5, 6?
		
			m = 7 n = 2 
			cada valor puede estar repetido en una ficha
			no importa el orden 
			(la ficha puede girarse y no importa 
			la ubicación del número, sino su valor)
			
		solucion = 28 fichas = C8,2 ó C´7,2
			
"""
from Modulo_funciones_matematicas import *


while True:
	
	try :
		num_total = int(input("Escribe el número total de elementos: "))		 	

		num_arreglos = int(input("Escribe el orden: "))

		operacion = input("""Escribe que hay a realizar 
				\n(Si es arreglo sin repetición=asr  
				\n si es un arreglo con repetición= ar 
				\n si es una permutación sin repetición= psr
				\n si es una permutación con repetición= pr
				\n si es una combinación sin repetición= csr
				\n si es una combinación con repetición= cr ): """)
 
		if operacion == "asr":
	
			numerador = factorial(num_total)
	
			denominador = factorial(num_total - num_arreglos)
	 
			print("el arreglo sin repeticion de", num_total 
					,  
					"\n tomados de a ", num_arreglos 
					,"\n es" 
					, int(numerador/denominador))

		if operacion == "ar":

			resultado = exponencial(num_total, num_arreglos)

			print("el arreglo de ", num_total, 
				  "\n tomados de a ", num_arreglos,
			 	  "\n con repetición es ", resultado)

		if operacion == "psr":

			resultado = factorial(num_total)
			
			print(" la permutación de ", num_total, 
			 	  "\n  sin repetición es ", resultado)

		if operacion == "pr":

			repeticiones = int(input("ponga el numero de valores que se repiten "))		
				
			denominador = permutacion_con_repeticion(repeticiones)
			
			resultado = factorial(num_total)/denominador 

			print(resultado)

			
		if operacion == "csr":

			numerador = factorial(num_total)
	
			denominador1 = factorial(num_total - num_arreglos)

			denominador2 = multiplicacion(denominador1, num_arreglos)
	 
			print("el combinación sin repeticion de", num_total 
					,  
					"\n tomados de a ", num_arreglos 
					,"\n es" 
					, int(numerador/denominador2))

		if operacion == "cr":

			numerador1 = num_total + (num_arreglos - 1)

			numerador2 = factorial(numerador1)

			denominador1 = factorial(numerador1 - num_arreglos)

			fact_num_arreglos = factorial(num_arreglos)

			denominador2 = multiplicacion(denominador1, fact_num_arreglos)
	 
			print("\n el combinación con repeticion de", num_total 
					,  
					"\n tomados de a ", num_arreglos 
					,"\n es" 
					, int(numerador2/denominador2))

	except ValueError:

		print("Escribe un valor numerico")












