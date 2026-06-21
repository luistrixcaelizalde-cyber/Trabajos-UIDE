import random

# Variable para mantener el programa ejecutándose
ejecutar = True

while ejecutar:

    print("\n===== GESTOR DE CONTRASEÑAS =====")
    print("1. Generar contraseña")
    print("2. Analizar contraseña")
    print("3. Guardar contraseña")
    print("4. Historial")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # OPCION 1
    if opcion == "1":

        letras = "abcdefghijklmnopqrstuvwxyz"
        numeros = "0123456789"

        contraseña = ""

        # Genera 6 letras
        for i in range(6):
            contraseña += random.choice(letras)

        # Agrega 2 números
        for i in range(2):
            contraseña += random.choice(numeros)

        print("\nContraseña generada:", contraseña)

    # OPCION 2
    elif opcion == "2":

        contraseña = input("Ingrese una contraseña: ")

        longitud = len(contraseña)

        tiene_numero = False
        tiene_mayuscula = False

        for caracter in contraseña:

            if caracter.isdigit():
                tiene_numero = True

            if caracter.isupper():
                tiene_mayuscula = True

        # Evaluación de seguridad
        if longitud < 6:
            print("\nSeguridad: DÉBIL")
            print("La contraseña es fácil de adivinar.")

        elif longitud >= 8 and tiene_numero and tiene_mayuscula:
            print("\nSeguridad: SEGURA")
            print("La contraseña cumple los requisitos básicos.")

        else:
            print("\nSeguridad: INTERMEDIA")
            print("Podría mejorarse agregando más caracteres.")

    # OPCION 3
    elif opcion == "3":
        print("\nFunción en desarrollo.")

    # OPCION 4
    elif opcion == "4":
        print("\nFunción en desarrollo.")

    # OPCION 5
    elif opcion == "5":
        print("\nGracias por utilizar el programa.")
        ejecutar = False

    else:
        print("\nOpción inválida. Intente nuevamente.")