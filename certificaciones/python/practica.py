print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print(0o123) # para pasr los numero a octal
print(0x123) # para pasr los numero a hexadecimal   
print(3e10) # para pasr los numero a exponencial
print(4) # para pasr los numero a entero
print(4.0) # para pasr los numero a flotante
print(4*4.0 ) # al multiplicar un entrero por un float se convierte en float
print("me gusta \"monthy python\"") # para imprimir las comillas
print("me gusta 'monthy python'") # para imprimir las comillas
print('me gusta "monthy python"') # para imprimir las comillas
print("i'am monthy python") # para imprimir las comillas
print(True>False) # para comparar los booleanos
print(True<False) # para comparar los booleanos
print(1>0) # para comparar los numeros
print(1<0) # para comparar los numeros
print('"estoy"') # para imprimir las comillas
print('""aprendiendo""') # para imprimir las comillas
print('"""python"""') # para imprimir las comillas
print('"estoy"\n""aprendiendo""\n"""python"""') # nos imprime las comillas y nos los separa filas 
print('"estoy"','""aprendiendo""','"""python"""',sep="\n") # nos imprime las comillas y nos los separa filas 
binario="1011" # para asignar el valor de la variable binario
entero= int(binario,2) # para convertir el binario a entero
print(entero) # para imprimir el valor de la variable entero
print(2**2) # para elevar el numero 2 al cuadrado
print(2**4) # para elevar el numero 2 al cuadrado
print(2+2)
print((2+2+2-(4*2))/3) # para calcular la expresion
print(19//8) # nos redondea la divicion hacia abajo
print(15%25) # esta expresion nos genera un modulo en divisro por el dividendo
print(2**3) # para elevar el numero 2 al cubo
print(2**3.) # para elevar el numero 2 al cubo  
print(2.**3) # cuand alguno de lo numero tien enteros entonces el resultado se convierte en flotante
print(2.**3.) # para elevar el numero 2 al cubo
print(++2) # para un operador binario que esta solo, la uma varias veeces a la izqueirda no genera nda 
print(9%6) # modulo 
print(3%2) # modulo
print(9%6%2) # modulo
print(15%25) # modulo
print(4%5) # modulo
print(1%2) # modulo
print(2 ** 2 ** 3) # para exponenciales siemrpe se inica de derecha a izquierda
print((2 ** 2) ** 3) # si tien parentecis hace una diferencia
print((-3 )** 2) # para elevar el numero -3 al cuadrado
print((-2) ** 3) # para elevar el numero -2 al cubo
print(-(-3 ** 2)) # cambia con el manejod de los parentecis     
print(2*3%5) # si los operadores son de el mismo nivel entonvces la oepracion se resuleve desde izquierda 
print(4/2*3) # para que la operacion se resuleve desde izquierda 
print(25%13) # modulo
print(5*(12+100)) # primer se resulevne los parentesis 
print(560/26)
print((560/26)//2)
print((5*((25%13)+100)/(2*13))//2)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
print(2**9)
"""
Variables
"""
var = 2
valance_decuenta = 100
media = 50
print(var , valance_decuenta , media)
print(var*media)
var = "3.12.4"
print(var)
print("python version " + var)
var = 100
var = 100 + 200 # las variables son replazdas cuando se usan de nuevo 
print(var)
a = 3.0
b = 4.0
c = (a**2 + b**2)/2
print("c = ",c )
c = (a**2 + b**2)**0.5
print(c)
c = (a**2 + b**2)**(1/2)
print("c = ", c)

j = 3
m = 5
a = 6
ma = "manzanas"
print( "jhon tiene " , j , ma,',' ,"mary tiene ", m , ma,',' ,"adam tiene ", a , ma )
t = j + m + a
print(t)
print(j%t)
print(m%t)
print(a%t)
print(j//t)
print(m//t)
print(a//t)
print(t//j)
print(t//m) # esto tambien
print(t//a)
# esto es un comentario

mll = 1.61
kms = 1/mll
print("un kilomtro son ", round(kms,5), "millas")

print( "una milla son", mll , "kilometros y un kilometro son ", kms, "millas")
print(round(kms,6))
print("12.5 kilometros son", round(12.5*kms,3) ,"millas", "y ", "7.38 millas son ", round(7.38*mll,3), "kms" )

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 3), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 3), "millas")

x = 2
x = float(x)
y = (3*x**3) - (2*x**2) + (3*x)-1
print(y)

x = 0
x = float(x)
y = (3*x**3) - (2*x**2) + (3*x)-1
print(y)

x = 1
x = float(x)
y = (3*x**3) - (2*x**2) + (3*x)-1
print(y)

x = -1
x = float(x)
y = (3*x**3) - (2*x**2) + (3*x)-1
print(y)

x = -1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print(y)

var = 1
var += 1
print(var)
var-=3
print(var)
var*=5
print(var)
var /= 5
print(var)
var **=2
print(var)
var //= 2
print (var)
var = float(var)
print(var)
var = " hola pues"
print("hola " + var)

var = 2
var = 3
print (var)

a = '1'
b = "1"
print(a + b)

a = 6
b = 3
a /=2*b
print(a)
import sys

print(f"Estás trabajando con Python versión: {sys.version}")
# Esto es un comentario de una sola línea en Python

'''
Esto es un comentario
de múltiples líneas
en Python
'''

"""
También puedes usar
comillas dobles para
comentarios de múltiples líneas
"""

# Ejemplo de uso de comentarios en código:
x = 5  # Asignamos el valor 5 a la variable x
y = 10  # Asignamos el valor 10 a la variable y

# Sumamos x e y
resultado = x + y  # El resultado será 15

print(resultado)  # Imprimimos el resultadop
print("dime lo que quieras...")
algo = input()
print("hmm... " , algo , "es buen comentario")


"""
funcion input()

"""

print("dime lo que sea ") #nos pide mostrar en patalla un texto 
anything = input() # nos solicita en este texto copiar algo 
print("hmm...", anything, "...¿en serio?") # nos imprimer en paralla un textos seleccionado y a este se le adiciona en la mitad lo que nostros copiamos, generando asi aun variable de ingresi de tipo caracter

# vamos a cambiar la funcion anterior de manera que no usemos la entrada print()

anything = input("dime lo que quieras...") #la funcion input() se puede invocar con un argimento que la anteceda
print("hmm....", anything, ".... ¿en serio") #y la respuesta puede seguir siendo la misma 
print(anything * 2) #podemos usar el multiplicador de caracteres eneteros pero no podemos usar ningun otro operador

"""
CONVERSION DE TIPOS
"""
#en este caso tenemos que pasa asar un caracte a int o float, debemos de usar una funcion que lo haga por nosotos.
anything = float(input("ingresa un numero: ")) #aqui estamos convirtiendo un argumento en un numero float
something = anything ** 2.0 # le damos valor a una nueva variable 
print(anything, " a la potecia de 2 es ",something) #imprimos en pantalla una respues que sea logica para el que lo ve

anything = int(input("ingresa un numero: ")) # si lo usamos con int o con float, debemos tenemos en cuenta que numero se ingresa, dado que int solo acepta valores enteros
something = anything ** 2.0
print(anything, " a la potecia de 2 es ",something)

"""
Teotema de pitagoras
"""
leg_a = float(input("ingrese la longitud del primer cateto: ")) # en este caso tenemos un erro con los signos negativos, pues solo considera una operacion de potencias y sumas pero tiene en cuetnas si son positicos o negativos y esto genera un error.
leg_b = float(input("ingresel la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2)**0.5
print("la hipotenusa del triangulo es: ", hypo)

leg_a = float(input("ingrese la longotud del primer cateto: "))
leg_b = float(input("ingresel la longitud del segundo cateto: "))
print("la hipotenusa del triangulo es: ", (leg_a**2 + leg_b**2)**0.5)#claramente con la variable hypo solo almacena una formula, esta misama la podmeos inprimir en la salida sin nigun problema pues las variabls usadas ya estan definidas

"""
OPERADORES CADENAS
para este caso tenemos los oepradores "+" y "*" los cuales aparte de poder operar entre numeros 
tambien puden operar entre caracteres de la sigueitne manera 
para que el simbolo "+" no sume si no que concatene ambos argumentos deben ser cadenas y no numeros.

"""
fnam = input("¿me puedes dar tu nombre por favor?: ")
lnam = input("¿me puedes dar tu apellido por favor?: ")
print("gracias. ")
print("\nTu nombre es "+ fnam + " " + lnam + ".") #aqui tenemos un ejeplo calro de lo que s una concatenacion entre caracteres

a = ("2" * 2) #esto se comparta como una cadena y no puede ser llevado a un numero, asi eque si se opera con el se comprtara como tal 
print (a)
b = input("ingrese el valor de b: ")
print(b)
print( "el valor de a es ",  a , " el valor de b es: ", b , "las suma de los dos es ",  a + b)

# otro modo de usarlo seria 

print("+" + 10 * "-" + "+")
print(("!" + " " * 10 + "!\n")*5,end="")
print("+" + 10 * "-" + "+")

"""
CONVERSIONES DE TIPOS DE NUEVO
para este caso usaremos las funcion str(), la cual nos lleva un numero a una
cadena y con esto lo que podemos es usar los simbolos para concatenar una respuesta. 
"""
leg_a = float(input("ingrese la longotud del primer cateto: "))
leg_b = float(input("ingresel la longitud del segundo cateto: "))
print("la hipotenusa del triangulo es: "+ str((leg_a**2 + leg_b**2)**0.5))#en este caso usamos la funcion str() para cambiar el valor de la hyp y llevarlo a una cadena, asi podemos usar el conector "+" para concatenar la respuesta

"""
# LAB

"""

# vamos a solicitar dos calores a y b y generar las operaciones aritmeticas basicas 
a = float(input("ingresa un valro para a: "))
b = float(input("ingresa un valro para b: "))

print("la suma entre a y b es: ", a + b)
print("la resta entre a y b es: ", a - b)
print("la division entere a y b es: ", a/b)
print("el producto entre a y b es: ", a * b)

print("\nEso es todo, amigos")

# hagamos el mismo ejercicio paro concatenando 

a = float(input("ingresa un valro para a: "))
b = float(input("ingresa un valro para b: "))

print("la suma entre a y b es: " + str( a + b))
print("la resta entre a y b es: " + str( a - b))
print("la division entere a y b es: " + str( a/b))
print("el producto entre a y b es: " + str( a * b))

print("\nEso es todo, amigos")

# evaluar una funcion periodica  de 1/x 4 veces 

x = float(input("ingresa un valor para x diferente de cero: "))
y = (1/(x + (1/(x + (1/(x+(1/x))))))) #en este caso la evaluamos dandole un valo establecido a y
print("y = " , y) 

# vamos a hacero directamente cobre la fincuon print

x = float(input("ingresa un valor para x diferente de cero: "))
print("y = ", (1/(x + (1/(x + (1/(x+(1/x))))))) )

# ahora vamos a hacelo con la funciuon str() 

x = float(input("ingresa un valor para x diferente de cero: "))
print("y = " +  str(1/(x + (1/(x + (1/(x+(1/x))))))) )


"""
calcular segun la hora de ingreso a una reunion y el timep ode reunmion a que hora se sale de esta 

"""
# primera practica da resultados pero no es eficiente cuando pasa de cierto valor 
h = int(input("ingrese la hora de inicio a: "))
m = int(input("ingrese el minuto de inicio b: "))
h_m = h * 60 # hora en minutos 
h_i = h_m + m # hora de inicio 
print("la hora de inicio en minutos es: ", h_i) 
t = int(input("ingrese el tiempo de la reunion en mintos: "))
t_f = int(h_i + t) # timepo de finalizacion en minutos 
print("el timepo en minutos es: ", t_f) # el timpo en minutos es 
h_f = t_f//24
h_s = t_f%60  # hora de salida  
print("la hora de finalizacion es: ",h_f,"horas :", h_s , "minutos")

# aqui tenemos una respuesta que da los mismos resultados 

h = int(input("ingrese la hora de inicio a: "))
m = int(input("ingrese el minuto de inicio b: "))
t_r = int(input("ingrese el timepo de la reunion: "))
m = m + t_r # total de minutos 
h = h * 60 # las horas a minutos 
print(h, m , h + m)
h = h + m # tiempo total en minutos 
m = h
h = h // 60
m = (m / 60) - h 
print(h, m)
h = h % 24
m = round(m * 60)
print("hora" , h,":", m , " minutos") # hora del dia para finalizar 


# aqui tenemos la respuesta de la pagina 

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')

# nota, la funcion type(), tipifica lo que ingresamos

x = input( "ingrese un numero: ") # ingresamos un careacter
print(x) 
x = 5 * x # se crea un caracter de 5 
print(x) 
print(x * 2) 
x = x * 2 # sigue siendo un caracter que se multilia por un entrero, generando uan cadenas mas larga  
print(type(x)) 
x = int(x) # se convierte el caracter en un int
print(type(x)) 
x = float(x) # se convierte el caracter en un float
print(type(x)) 
x = x - 222222 
print(x)
print(type(x)) 
True


""" -------------------
    COMO TOMAR DECICIONES EN PYTHON
---------------------"""


