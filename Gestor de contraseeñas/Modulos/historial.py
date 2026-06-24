def mostrar_historial(usuario):

    try:

        with open("datos/" + usuario + ".txt", "r") as archivo:

            print("\n===== HISTORIAL =====")

            contenido = archivo.read()

            if contenido == "":

                print("No existen registros.")

            else:

                print(contenido)

    except FileNotFoundError:

        print("No tiene contraseñas guardadas.")