lenguajes = ["Pyton","Ruby","Javascript","PHP","Java"]

for lenguaje in lenguajes:
    print(lenguaje)


i = 0
while i < len(lenguajes): # condicion
    print("el ",i,"es ",lenguajes[i]) # imprime
    i = i + 1 # limite del bucle, pausa la crecer i y llegar al valor nececitado 
    