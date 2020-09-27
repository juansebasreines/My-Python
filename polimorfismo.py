class moto():

	def moverse(self):
		print("voy en dos ruedas")

class Camión():

	def moverse(self):
		print("voy en casi 6 ruedas")

class Bus():

	def moverse(self):
		print("voy en 4 o 8 ruedas")


def moverseVehiculo(Vehiculo):
	Vehiculo.moverse()

MiVehiculo = Bus()
moverseVehiculo(MiVehiculo)





