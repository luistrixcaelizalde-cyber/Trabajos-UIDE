def guardar_contraseña():

    nombre = input("Nombre de la cuenta: ")
    contraseña = input("Contraseña a guardar: ")

    with open("datos/historial.txt", "a") as archivo:

        archivo.write(nombre + " -> " + contraseña + "\n")

    print("\nContraseña guardada correctamente.")