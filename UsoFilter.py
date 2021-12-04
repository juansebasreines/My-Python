#USO DE FILTER COMO FUNCIÓN CLÁSICA

def numero_par(num):
	
	if num % 2 == 0:
		
		return True

numeros=[15,57,6,8,4,987,68,458,858,58]


#Aquí pido que se imprima como tupla
print(tuple(filter(numero_par, numeros)))


#FILTER PARA FUNCIÓN LAMBDA 

numeros=[15,57,6,8,4,987,68,458,858,58]


#Aquí pido se imprima como lista
print(list(filter(lambda numberpar: numberpar % 2 == 0, numeros)))


class Empleado():
	
	def __init__(self, nombre, cargo, salario):
		
		self.nombre = nombre

		self.cargo = cargo
		
		self.salario = salario

	def __str__(self):
		
		#return "{} que trabaja como {} y tiene un salario de {}".format(self.nombre, self.cargo, self.salario)

		return (f"{self.nombre} que trabaja como {self.cargo} y tiene un salario de {self.salario}")

ListaEmpleados=[

Empleado("Juan", "Director", 100000),

Empleado("Ana", "Analista", 45000),

Empleado("Martin", "Programador", 70000),

Empleado("Lucia", "Secretaria", 30000)

]

# USO DE FILTER COMO FUNCIÓN PARA ITERACIÓN

salarios_altos=filter(lambda empleado: empleado.salario > 50000, ListaEmpleados)

for empleado_salario in salarios_altos:
	
	print(empleado_salario)




