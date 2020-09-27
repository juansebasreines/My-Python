

class Vehiculos ():		 

	def __init__ (self, marca, modelo): 	#Esto es un constructor

		self.marca = marca
		self.modelo = modelo
		self.en_marcha = False
		self.acelerar = False
		self.frena = False

	def arrancar(self):
		self.en_marcha = True

	def acelerar(self):
		self.acelerar = True

	def frena(self):
		self.frena = True

	def Estado_de_Vehiculo(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, 
			"\nEn Marcha: ", self.en_marcha, "\nAcelerando: ", self.acelerar,
			"\nFrenar: ", self.frena)



class Camión(Vehiculos):

	def carga(self, cargamento):
		
		self.cargado = cargamento

		if self.cargado:
			print("El camión está cargado")
		else:
			print("El camión va tranqui")



class moto(Vehiculos):
	pasar_entre_autos = ""

	def pasar(self):
		self.pasar_entre_autos ="Esquivando autos" 

	def Estado_de_Vehiculo(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, 
			"\nEn Marcha: ", self.en_marcha, "\nAcelerando: ", self.acelerar,
			"\nFrenar: ", self.frena, "\n", self.pasar_entre_autos)


class VElectricos(self):
	
	def __init__(self):
		km_autonomia = 100

	def bateria(self):
		self.energia = True

class BicicletaElec(Vehiculos,VElectricos):
	pass

