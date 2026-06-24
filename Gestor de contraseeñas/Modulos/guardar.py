def guardar_contraseña(usuario):

    nombre = input("Nombre de la cuenta: ")
    contraseña = input("Contraseña a guardar: ")

    with open("datos/" + usuario + ".txt", "a") as archivo:

        archivo.write(nombre + " -> " + contraseña + "\n")

    print("\nContraseña guardada correctamente.")