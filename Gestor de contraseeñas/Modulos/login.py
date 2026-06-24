def registrar():

    usuario = input("Ingrese un usuario: ")
    contraseña = input("Ingrese una contraseña: ")

    with open("datos/usuarios.txt", "a") as archivo:

        archivo.write(usuario + "," + contraseña + "\n")

    print("\nUsuario registrado correctamente.")


def iniciar_sesion():

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    try:

        with open("datos/usuarios.txt", "r") as archivo:

            for linea in archivo:

                datos = linea.strip().split(",")

                if usuario == datos[0] and contraseña == datos[1]:

                    print("\nBienvenido", usuario)

                    return usuario

    except FileNotFoundError:

        print("No existe la base de usuarios.")

    print("\nUsuario o contraseña incorrectos.")

    return None