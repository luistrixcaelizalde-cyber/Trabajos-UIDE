from modulos.login import registrar
from modulos.login import iniciar_sesion

from modulos.generador import generar_contraseña
from modulos.analizador import analizar_contraseña
from modulos.guardar import guardar_contraseña
from modulos.historial import mostrar_historial
from modulos.bienvenida import mostrar_bienvenida

mostrar_bienvenida()

ejecutar = True

while ejecutar:

    print("\n===== ACCESO AL SISTEMA =====")

    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        registrar()

    elif opcion == "2":

        usuario = iniciar_sesion()

        if usuario:

            print("\nBienvenido", usuario)

            sesion = True

            while sesion:

                print("\n===== MENÚ PRINCIPAL =====")

                menu = [
                    "1. Generar contraseña",
                    "2. Analizar contraseña",
                    "3. Guardar contraseña",
                    "4. Historial",
                    "5. Cerrar sesión"
                ]

                for opcion_menu in menu:
                    print(opcion_menu)

                opcion_menu = input("Seleccione una opción: ")

                if opcion_menu == "1":

                    generar_contraseña()

                elif opcion_menu == "2":

                    analizar_contraseña()

                elif opcion_menu == "3":

                    guardar_contraseña()

                elif opcion_menu == "4":

                    mostrar_historial()

                elif opcion_menu == "5":

                    print("\nSesión cerrada correctamente.")

                    sesion = False

                else:

                    print("\nOpción inválida.")

    elif opcion == "3":

        print("\nGracias por utilizar el programa.")

        ejecutar = False

    else:

        print("\nOpción inválida.")