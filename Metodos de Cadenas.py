#TODO ESTO SE TRATA DE STRINGS

	#UPPER
#VUELVE LAS PALABRAS A MAYUSCULAS 
User = input("Introducir nombre: ")
print("El nombre es :", User.upper())


	#LOWER
#VUELVE TODO A MINUSCULAS 

User = input("Introducir apellido: ")
print("El apellido es :", User.lower())

	#CAPITALIZE
#PONE LA PRIMERA LETRA EN MAYUSCULA

User = input("Introducir alias: ")
print("El alias es :", User.capitalize())

	#COUNT
#CUENTA CUANTAS LETRAS O CADENAS DE TEXTO HAY EN UNA ORACIÓN

User = input("Introducir apodo: ")
print("El apodo es :", User.count("S"))

	#FIND
#ENCUENTRA EL INDICE DE DONDE SE ENCUENTRA UNA LETRA 

User = input("Introducir sobrenombre: ")
print("El sobrenombre es :", User.find("s"))

	#ISDIGIT
#DEVUELVE BOOLEANO


Edad = input("introduce tu edad real no te \nhagas el mayor como en Facebook: ")


while (Edad.isdigit() == False):
	
	print("\npor fa pone números guacho")
	
	Edad = input("\nintroduce tu edad real no te \nhagas el mayor como en Facebook: ")		


if (int(Edad) < 18):
	
	print("no puede pasar")

else:
	
	print("entre nomás perro")



	#ISALUM
#COMPRUEBA SI ES NUMERICO

	#ISALPHA
#COMPRUEBA SI SOLO SON LETRAS 

	#SPLIT
#SEPARA POR PALABRAS UTILIZANDO ESPACIOS

	#STRIP
#BORRA ESPACIOS SOBRANTES AL PRINCIPIO Y AL FINAL

	#REPLACE
#REEMPLAZA POR UNA PALABRA O LETRA 

	#RFIND
#LO MISMO QUE FIND PERO CUENTA DESDE ATRAS R DE REVERSE
