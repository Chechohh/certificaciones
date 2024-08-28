""""
TOMA DE DECICIONES 

=: este operador asigan un valore a otro 
==: este operador pregunta si dos variables son iguales
este segundo siempre dara como respuesta verdadero o falso
"""
print(2 == 2) # True
print(2 == 2.) # True
print(2 == 2.0) #True
print(1 == 2) # False
var = 2
print(var == 2) # True el argumento debe estar definido para ser booleano    
print(var != 2) # False el argumento debe estar definido para ser booleano    

var = 3
res1 = var == 2 # False
res2 = var != 2 # True

print(res1,res2)

"""
OPERADORES

==: igual a
!=: desigual o diferente
>: mayor que 
<: menor que
>=: mayor o igual, estos son operadores con enlazado al lado izquierdo
<=: menor o igual
las respuestas de estos operadores se pueden almacenar en una variable para usarlos luego

funciones
min() = encuantra el ninimo de varios numeros 
max() = encuentra el maximo de varios numeros 
round() = redondea un numero 

"""
#escriba un programa que diga si un numero es menos que
#100 diga False de lo contrario res True
#   n =int(input("ingrese un numero: "))
#   print(n >= 100)

"""
CONDICIONES Y EJECUCION CONDICIONAL
-----------------------------------
aprenderemos como hace un programa que tome deciciones si se cumple o no una condicion

condicional
if: condicional si
lo usamos para tomar deciciones de verda o falsedad (True or False)
para poder culminar la toma de decicones
if condicion:
    segunda condicion()
    tercera condicion()
    .
condicion que se cumple siempre
----------------
if-else: condicional si - entonces
if condicion:
    segunda condicion()
else:
    si la primera condicion no se cumple() 
condicion que seimpre se cunplira sin importar que()
----------------
podemos anidar varias condiciones de las sigueinte manera 

if conidicion1:
    if condicion2:
        condicion3()
    else:
        consicion4()
else:
    if condicion5:
        condicion6()
    else:
        condicion7()
en este caso podemos ver las condiciones anidadas en las cuales una depende 
de la otra para poder cumplirce y estas seran consecutivas una con la otra.
----------------
elif: sentecia else if, sirve para verificar mas de una condicion y para que se 
detenga cuando enceuntre una sentencia verdadera.

if condicion1:
    condicion2()
elif condicion3:
    condicion4()
elif conicion5:
    condicion6() #el proceso debe continua tanto como queramos
else:             #el proceso siempre debe finalizar con un else
    condicion7()

EJEMPLOS
"""


# 1
print("\nejemplo 1")
number1 = int(input("ingrese el primer numero: "))
number2 = int(input("ingrese el segundo numero: "))

if number1 > number2:
    large_number = number1
else:
    large_number = number2

print("el numero mas grande es: ",large_number)

# 2, python tiene otra formas de hacerlo 
print("\nejemplo 2")
number1 = int(input("ingrese el primer numero: "))
number2 = int(input("ingrese el segundo numero: "))

if number1 > number2: large_number = number1
else: large_number = number2

print("el numero mas grande es: ",large_number)

# 3. encuentra el mayor de  numeros 
print("\nejemplo 3")
number1 = int(input("ingrese el primer numero: "))
number2 = int(input("ingrese el segundo numero: "))
number3 = int(input("ingrese el tercer numero: "))

large_number = number1

if number2 > large_number:
    large_number = number2

if number3 > large_number:
    large_number = number3

print("el numero mas grande es: ",large_number)

# 4 otra forma
print("\nejemplo 4")
number1 = int(input("ingrese el primer numero: "))
number2 = int(input("ingrese el segundo numero: "))
number3 = int(input("ingrese el tercer numero: "))

if number1 > number2 > number3:
    large_number = number1
elif number2 > number1 > number3:
    large_number = number2
else:
    large_number = number3


print("el numero mas grande es: ",large_number)


# 5 usemos la funcion max y min
print("\nEjemplo 5")
number1 = int(input("ingrese el primer numero: "))
number2 = int(input("ingrese el segundo numero: "))
number3 = int(input("ingrese el tercer numero: "))

large_number = max(number1,number2,number3)
min_number = min(number1,number2,number3)

print("El número más grande es: ",large_number,"\nEl numero mas pequeño es: ",min_number)


#6 ejemplo espatifilo

print("\nEjemplo 6")
planta = input("ingrese el nombre de la planta: ")

if planta == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
elif planta == "Espatifilo":
    print("el",planta," es la mejor planta del mundo")
else:
    print("¡Espatifilo!, ¡no ", planta,"!")

# 7 Calculadore de impustos 
print("\nEjemplo 7 - calculadora de impuestos")

ingresos = float(input("Ingrese el valor de sus ganacias: "))

if ingresos <= 85528:
    IPI = round(ingresos*0.18 - 556.2)
    if IPI <= 0:
        IPI = 0
else:
    ingresos > 85528
    IPI = round(14839.2 + ((ingresos-85528)*0.32)) 

print("el impuesto a cobrar es: ",float(IPI))
