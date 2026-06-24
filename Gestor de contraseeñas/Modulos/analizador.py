def analizar_contraseña():

    contraseña = input("Ingrese una contraseña: ")

    longitud = len(contraseña)

    tiene_numero = False
    tiene_mayuscula = False

    for caracter in contraseña:

        if caracter.isdigit():

            tiene_numero = True

        if caracter.isupper():

            tiene_mayuscula = True

    estados = (
        "DÉBIL",
        "INTERMEDIA",
        "SEGURA"
    )

    if longitud < 6:

        print("\nSeguridad:", estados[0])

    elif longitud >= 8 and tiene_numero and tiene_mayuscula:

        print("\nSeguridad:", estados[2])

    else:

        print("\nSeguridad:", estados[1])