#METODO 

class computador():
	def __init__(self) : #este hace que tenga un estado inicial
						 #si se quiere 	que no se modifique se deja como esta
						 # la pantalla
		self.ram = str(8)+"GB"
		self.disk_hard = str(2)+"TB"
		self.__pantalla = str(15)+" pulgadas"		#esto es una variable encapsulada 
		self.teclado = "doble"						#(no se puede modificar)
		self.gabinete = "mini box"
		self.cargador = 1  # los números de hardware son el metros
		self.estado = False
	
	def arrancar(self, comienzo):
		self.estado = comienzo

		if (self.encendido):
			chequeo = self.__chequeo_maquina()
		
		if (self.estado and chequeo):
			return "iniciando proceso"

		elif(self.estado and chequeo == False):
			return "algún componente falta a conectar (mouse ó impresora)"
		
		else: 
			return "pantalla apagada"

	
	def encendido(self):
		
		print("los componentes principales del computador son: ", "una ram de ",
			self.ram,", un disco duro de " , self.disk_hard,", una pantalla de ",
			self.__pantalla,", un teclado ", self.teclado, 
			", un gabinete tipo" , self.gabinete, "y un cargador de ", self.cargador, "metro")

	
	def __chequeo_maquina(self):
		print("realizando chequeo interno")

		self.mouse = "ok"
		self.impresora = "ok"

		if (self.mouse == "ok" and self.impresora == "ok"):
			return True
		else: 
			print("Falta el mouse o la impresora o el ups, por favor conectelo lo más antes posible ")


dell = computador()

dell.arrancar(True)

dell.encendido()

print("--------------------------------------cargando----------------------------------------------")
print("--------------------------------------cargando----------------------------------------------")
print("--------------------------------------cargando----------------------------------------------")
print("--------------------------------------cargando----------------------------------------------")
print("--------------------------------------cargando----------------------------------------------")
print("--------------------------------------cargando----------------------------------------------")
print("-------------------------------Entrando a computador LG-------------------------------------")

print("-------------------------------------INICIO LG----------------------------------------------")

lg = computador()
 
lg.encendido()


