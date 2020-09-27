#############
# si se necesita el orden 
# se usa combinacion simple
# y se puede repetir
def combinacion (m,n,grado):
#n= numero de elementos que quiero
#m= numero total de elementos
#	total = 0
	for i in (m,1):
		i=i+1
		if i<m:
			total=(m)*(m-i)
			pass
		pass

#print(total)
#combinacion(1,2,3)

##################################################
g=1
f=1
num1= int(input("poner un numero"))
num2= int(input("poner un numero"))
for i in range(num1):
	g=g*num1
	num1 = num1-1

for i in range(num2):
	f=f*num2
	num2 = num2-1

print(g)
print(f)

##################################################