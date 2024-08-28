"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""
x = 1 #float(input("ingresa el valor de x: "))
y = 1 #float(input("ingresa el valor de y: "))
z = 1 #float(input("ingresa el valor de z: "))

print("la suma entre ",x, "y", y, " es: ", x + y)
print(f"la suma de x + y = { x + y }") #esto se llama proceso de interpolacion en python
print(f"la resta de x - y =  {x - y}")
print("el producto entre",x, " y ",y," es: " , x * y)
print("la division entre ",x," y ",y, " es: ", x / y )
print("la parte entera entre",x," y ",y, " es: ", x % y)
print("la division parte entera entre ", x ," y ",y, " es: " , x // y)
print("al redondear la division de ",x," con ", y, "nos da: ", round(x/y))
print("la pontencia de", x,"a la ",y," es: ", x ** y)
print("el maxiumo de los tres numeros es: ", max(x,y,z))
print("el minimo de los tres numeros es: ", min(x,y,z))
print(x, "es mayor que", y, ":", x > y)
print(x, "es mayor o igual que", y, ":", x >= y)
print(x, "es menor que", y, ":", x < y)
print(x, "es menor o igual que", y, ":", x <= y)
print(x, "es igual que", y, ":", x == y)
print(x, "es distinto que", y, ":", x != y, "\n")

# operadores logicos, or, and, not

print("verdader o verdadero da: ", True or True)
print("verdadero o falso da: ", True or False)
print("falso o falso da : ", False or False)
print("falso o verdadero da: ", False or True)
print("verdadero y verdadero da: ", True and True)
print("verdadero y falso da: ", True and False)
print("falso y faldo da: ", False and False)
print("faldo y verdadero da: ", False and True)
print("la negacion de la verdad da: ", not True)
print("la negacion de lo falso da: ", not False)
print("la negacion de la negacion de la verdad da: ", not not True)
print("la negacion de la negacion de lo falso da: ", not not False, "\n")

# operadores de asignacion: asignan al valor de la derecha el valor de la izquierda mas el operador y es progresivo 
x = y
print("ahora x vale: ", x, "y vale: ",y)
x -= y
print("ahora x vale: ", x, "y vale: ",y)
x += y 
print("ahora x vale: ", x, "y vale: ",y)
x *= y
print("ahora x vale: ", x, "y vale: ",y)
x /= y
print("ahora x vale: ", x, "y vale: ",y)
x //= y
print("ahora x vale: ", x, "y vale: ",y)
x %= y
print("ahora x vale: ", x, "y vale: ",y)
x **= y
print("ahora x vale: ", x, "y vale: ",y, "\n")

# operadores de identidad is, is not

a = 1 
b = 1
c = 2

print(a is b)
print(a is not b)

print(a is c)
print(a is not c,"\n")

# operadores de pertenencia in, not in y listas 

lista = [1,2,3,4,5,6,7,8,9]

print(lista)

print("el numero 2 esta en la lista? ",2 in lista)
print("el numero 12 no esta en la lista? ",12 not in lista)
print("el numero 2 no esta en la lista? , ",2 not in lista)
print("els numero 12 esta en la lista? ",12 in lista, "\n")

print(lista[0])
print(lista[8])
print(lista[-9])
print(lista[1:5])
print(lista[-8])

lista[2] = lista[2]**2
print(lista)

lista[2] = lista[3]**2
print(lista)

tupla = ("\nColombia", "Perú", "México", "Argentina", "Chile")
for i in tupla:
    print(i)

#* DIFICULTAD EXTRA (opcional):
#* Crea un programa que imprima por consola todos los números comprendidos
#* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

inicio = 10 
fin = 56

lista_p = list(range(inicio,fin))

print(lista_p)

num_elementos = len(lista_p)

print("la lista tiene ", num_elementos, "elementos")


n = 0
ne = num_elementos
print(n,ne)

# print(lista_p[n])

if (lista_p[n]%2 == 0) and (lista_p[n]!=16) and (lista_p[n]%3!=0) and lista_p[n]<=55:
    print(lista_p[n])

if (lista_p[n+4]%2 == 0) and (lista_p[n+4]!=16) and (lista_p[n+4]%3!=0) and lista_p[n+4]<=55:
    print(lista_p[n+4])

if (lista_p[n+10]%2 == 0) and (lista_p[n+10]!=16) and (lista_p[n+10]%3!=0) and lista_p[n+10]<=55:
    print(lista_p[n+10])

if (lista_p[n+45]%2 == 0) and (lista_p[n+45]!=16) and (lista_p[n+45]%3!=0) and lista_p[n+45]<=55:
    print(lista_p[n+45])

# esto si se hace recursivo se optienen los valores deseados pero es un prceso mas largo 


for i in range (10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print("\n",i)
