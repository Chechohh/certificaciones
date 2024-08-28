resultado = input("ingresa tu edad:")
print(resultado)
print(type(resultado)) #nos muestra que tipo de variable es
numero = int(resultado) # toma el dato de resultado y lo convierte en un entero 
print(numero + 2, type(numero + 2)) 

x = str(22) #toma el dato ingressado y lo convierte en un str
print(x,type(x))
y = float("22.13")#tomael dato ingresado y lo convierte en un numero float
print(y,type(y))
z = bool("")#lo convierte en True o False, solo hay hay 4 valores que evalia en False 
        # estos 4 serina 1- False, 2- 0, 3- " ", 4- None 
print(z,type(z))
w = bool(False)
print(w,type(w))
v = bool(0)
print(v,type(v))
a = bool(None)
print(a,type(a))
