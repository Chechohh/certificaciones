texto = "hola mundo"
print(texto)

#metodos 

print(texto.upper()) # .upper nos pasa todo a mayusculas  
print(texto.lower()) # .lower nos pasa tooo a minusculas 
print(texto.find("mun")) #.fin nos encuentras el str que buscamos 
print(texto.find("Mun")) 
nuevoTexto = texto.replace("mun", "chanchito feliz") #.seprace remplaza el str en la ps 1 por el str de la pos 2 
print(texto , nuevoTexto)
print("mundo" in texto) #pregunta si el texto esta incluido en la variable
