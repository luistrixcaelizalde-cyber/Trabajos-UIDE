def mostrar_historial():

    try:

        with open("datos/historial.txt", "r") as archivo:

            print("\n===== HISTORIAL =====")

            contenido = archivo.read()

            if contenido == "":

                print("No existen registros.")

            else:

                print(contenido)

    except FileNotFoundError:

        print("No existe historial.")