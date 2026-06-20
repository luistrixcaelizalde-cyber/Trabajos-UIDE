import random
ejecutar = True

while ejecutar:

    print("\nMENU PRINCIPAL")
    print("1. Generar contraseña")
    print("2. Personalizada")
    print("3. Guardar contraseña")
    print("4. Historial")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:

        letras = "abcdefghijklmnopqrstuvwxyz"
        numeros = "0123456789"

        contraseña = ""

        for i in range(8):
            contraseña += random.choice(letras + numeros)

        print("Contraseña generada:", contraseña)

    elif opcion == 2:

        contraseña = input("Ingrese una contraseña: ")

        longitud = len(contraseña)

        tiene_numero = False
        tiene_mayuscula = False

        for caracter in contraseña:

            if caracter.isdigit():
                tiene_numero = True

            if caracter.isupper():
                tiene_mayuscula = True

        if longitud < 6:
            print("Seguridad: DÉBIL")
            print("Es fácil de adivinar.")

        elif longitud >= 6 and (tiene_numero or tiene_mayuscula):
            print("Seguridad: INTERMEDIA")
            print("Podría mejorarse.")

        elif longitud >= 8 and tiene_numero and tiene_mayuscula:
            print("Seguridad: SEGURA")
            print("Buena contraseña.")

        else:
            print("Seguridad: INTERMEDIA")

    # OPCION 3
    elif opcion == 3:
        print("Guardar contraseña")
        # Pendiente

    # OPCION 4
    elif opcion == 4:
        print("Mostrar historial")
        # Pendiente

    # OPCION 5
    elif opcion == 5:
        print("Gracias por usar el programa.")
        ejecutar = False

    else:
        print("Opción inválida.")