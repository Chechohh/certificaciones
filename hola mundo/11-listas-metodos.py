lenguajes = ["Pyton","Ruby","Javascript","PHP","Java"]
lenguajes.insert(3,"Go") # este nos cambia la posicion 3 en la lsita por lo indicado
lenguajes.insert(0,"C")
lenguajes.remove("Ruby") #nos remueve la str de la lista
lenguajes.insert(1,2) #tambien podemos insertas numeros 
print("PHP" in lenguajes) #esto nos da una valor de True o False si el str esta o no en la lista 
print("Go" in lenguajes) #esto nos da una valor de True o False si el str esta o no en la lista 
print("Ruby" in lenguajes) #esto nos da una valor de True o False si el str esta o no en la lista 
print(lenguajes)
print(len(lenguajes)) # con esta funcion nos muestra cuantos elementos tiene nuestra lista

lenguajes.clear() #esto nos elimina todos los elementos de las lista 
print(lenguajes)