# vamos a hacer un codigo que nos permita convertir de farenhei a celcius y al contrario
temperatura = float(input("ingrese la temperatura: "))
escala = input("es Farenheit(F): o Celsius(C)?").lower()

if escala == "f":
    celsius = (temperatura - 32)* 5/9
    print(celsius)
elif escala == "c":
    fahrenheit = ( temperatura * 9)/5 + 32
    print (fahrenheit)
else:
    print("escala invcorrecta")