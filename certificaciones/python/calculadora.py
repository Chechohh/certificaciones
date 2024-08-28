def calculadora():
    # Pedir los dos números
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))

    # Mostrar las opciones disponibles
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Pedir la elección del usuario
    opcion = input("Introduce tu elección (1/2/3/4): ")

    # Realizar la operación correspondiente
    if opcion == '1':
        resultado = numero1 + numero2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == '2':
        resultado = numero1 - numero2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == '3':
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 4.")

# Llamar a la función calculadora
calculadora()
