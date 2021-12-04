import re

cadena= "Vamos a aprender expresiones regulares. Donde Python es un texto que esta en todas partes quiero hacer un texto donde se repitan muchos textos por eso tanto la palabra texto"

texto_buscar= "texto"

"""
SI SE QUIERE USAR UN CONDICIONAL

if re.search(texto_buscar, cadena) is not None:
	
	print("Ja! Papi se le tiene")

else:
	print("Te he fallado perro")

"""

Texto_encontrado = re.search(texto_buscar, cadena)

print(Texto_encontrado.start()) #ESTE SIRVE PARA VER DONDE EMPIEZA

print(Texto_encontrado.end())	#ESTE SIRVE PARA VER DONDE FINALIZA

print(Texto_encontrado.span())	#ESTE SIRVE PARA VER UNA TUPLA DE DONDE SE ENCUENTRA EL TEXTO

print(str(len(re.findall(texto_buscar, cadena))) + " veces se repite la palabra {}".format(texto_buscar))

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#-------------------			PARTE II	--------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

print("PARTE II \n")

Lista_nombres=[ 
"Ana Perez",
"Juan Martin", 
"Valeria Montenegro",
"Valentina Rodriguez",
"Mateo Ruiz"
]


for elemento in Lista_nombres:
	
	if re.findall("^Valeria", elemento):
		
		print(elemento)


#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#-------------------			PARTE III	--------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

print("PARTE III \n") 

nombre1 = "Sandra Lopez"
nombre2 = "Antonia Gomez"
nombre3 = "Mateo Quevedo"

if re.match("Sandra", nombre3, re.IGNORECASE):
	
	print("Vamoooooooo")

else:

	print("cagaste")

#-------------------------------------------------------------------------------------
#--------------------ESTO ES OTRO EJEMPLO PERO CADA PUNTO ES UNA LETRA----------------
#-------------------------------------------------------------------------------------

print("PARTE III (otro ejemplo) \n")

if re.match(".ra", nombre1, re.IGNORECASE):
	
	print("Vamoooooooo")

else:

	print("cagaste")


#-------------------------------------------------------------------------------------
#--------------------CON SEARCH BUSCA EN TODA LA VARIABLE----------------
#-------------------------------------------------------------------------------------
if re.search("ra", nombre1, re.IGNORECASE):
	
	print("Vamoooooooo")

else:

	print("cagaste")









