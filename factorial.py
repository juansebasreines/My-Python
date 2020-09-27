num1 = int(input("escribe el numero a realizar el factorial"))

#perm1 = int(input("escribe el n a permutar"))
#perm2 = int(input("escribe el orden"))

g = 1
f = 1
j = 1
#def factorial(num1,num2):
while g < num1:
	for i in range(num1):
		g = g*num1
		num1 = num1-1
		print (g) 

"""	for i in range(num2):
		f=f*num2
		num1 = num2-1
		return f 
print(g)
print(f)

#def combinar(num1,num2):
	
	for i in range(num1):
		g=g*num1
		num1 = num1-1
		return g 
	
	for i in range(num2):
		f=f*num2
		num2 = num2-1
		return f 

	t = g-f
	for i in range(t):
		j=j*t
		t = t-1
		return t 

	resultado = g/((t)*(f))

print(factorial(perm1,perm2))"""
