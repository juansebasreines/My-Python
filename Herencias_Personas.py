class Persona():

	def __init__(self, nombre, edad, país):

		self.nombre = nombre
		self.edad = edad
		self.país = país

	def descripción(self):
		
		print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nPaís: ",
		 self.país)

class Empleado(Persona):

	def __init__(self, Experiencia, Salario, Name_employed, age_employed, 
		country_employed):

		super().__init__(Name_employed, age_employed, country_employed)
		
		self.experiencia = Experiencia
		self.salario = Salario

	def descripción(self):

		super().descripción()

		print("Experiencia: ", self.experiencia,"año", "\nSalario: ", self.salario) 

Juan = Empleado(1, 5000, "Juan", 20, "Colombia")
Juan.descripción()