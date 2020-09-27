from io import open 

# ABRE EL ARCHIVO Y SI NO EXISTE LO CREA

archivo_text = open("archivo.txt","r+")

#ESCRIBE ELO EN EL ARCHIVO

archivo_text.write("\n igual no tengo tiempo para verlo")

lista = archivo_text.readlines()

lista[1] = "Esta es una nueva línea\n"

archivo_text.seek(0)

archivo_text.writelines(lista)

#LO CERRAMOS 

archivo_text.close()

