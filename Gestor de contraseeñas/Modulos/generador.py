from random import choice

def generar_contraseña():

    letras = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"

    contraseña = ""

    for i in range(6):

        contraseña += choice(letras)

    for i in range(2):

        contraseña += choice(numeros)

    print("\nContraseña generada:", contraseña)

    return contraseña