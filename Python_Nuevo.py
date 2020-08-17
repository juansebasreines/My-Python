###################
# CURSO PYTHON	  #
###################

###############
# 1) VARIABLES#
###############

	# ENTERAS (INT)

a = 5 
print(a)

	# DECIMALES (FLOAT)

b = 6.7
print(b)

	# TEXTO (STRINGS)
c = "hola"
print(c)

	# COMPLEJAS (COMPLEX)
d = 12j+3
print(d)

###################
# 2) CONDICIONALES#
###################
	
	# SI (IF, ELIF, ELSE)

if a>b:
	print(a+d)
elif a<b:
	print(a-b)
else:
	print(a-d)

#############
# 3) LISTAS # 
#############

mi_lista = [5,3,4,7,6,2,4,"lista"]
print(type(mi_lista))

#############
# 4) TUPLAS #
#############

mi_tupla = (5,7,6,8,9,3,0,4,"tupla")
print(type(mi_tupla))

###################
# 5) DICCIONARIOS #
###################

mi_diccionario = {5,4.4,7,9,c}
print(type(mi_diccionario))

##############################
# 6) FUNCIONES Y EXCEPCIONES #
##############################

def suma(a,b):
	return a+b

def resta(a,b):
	return a-b

def multiplicar(a,b):
	return a*b

def division(a,b):
	try:
		return a/b
	except ZeroDivisionError:
		print("No se puede dividir por cero")
		return "Operación errónea"
	
while True:
	
	try:
		
		opcion_1 = int(input("Escribe un número: "))
		
		opcion_2 = int(input("Escribe otro número: "))
		
		break
	
	except ValueError:
		
		print("Por favor introduce un valor numerico. Intentalo de nuevo")
		
aclaratorio_op = "Por favor escribe de manera exacta como está en los parentesis"

print(aclaratorio_op)

operacion = input("Escribe una operación (suma, resta, multiplicar, division): ")

if operacion == "suma":
	
	print(suma(opcion_1,opcion_2))

elif operacion == "resta":
	
	print(resta(opcion_1,opcion_2))

elif operacion == "multiplicar":
	
	print(multiplicar(opcion_1,opcion_2))

elif operacion == "division":
	
	print(division(opcion_1,opcion_2))

else: 
	
	print("No es una operacion valida")

print("Fin de operacion")



