Nombre=input("Ingrese sus nombres: ")
Apellido=input("Ingrese sus apellidos: ")
edad=int(input("Ingrese su edad: "))
Simbolos=["!","#","$","%","&","/","?"]
Numeros=[1,2,3,4,5,6,7,8,9,0]
menu=["1. Generar contraseña",
      "2. Salir",
      "3. Volver a ingresar datos",
      "4. Mostrar datos",
      "5. Contraseña personalizada"]

print("\n----- MENÚ -----")
for opcion in menu:
    print(opcion)

op = input("Seleccione una opción: ")

if op == "1":
    Apellido=(Apellido[0:3])
    Nombre=(Nombre[1:3])
    edad=(str(edad)[0:-1])
    Simbolo=(Simbolos[2:5])
    Numero=(Numeros[-3:-1])

    Contraseña=Apellido+Nombre+edad+Simbolo[0]+Simbolo[1]+Simbolo[2]+str(Numero[0])+str(Numero[1])

    print("Tu contraseña es:", Contraseña)

elif op == "2":
    print("Gracias por usar el programa")

elif op == "3":
    Nombre=input("Ingrese sus nombres: ")
    Apellido=input("Ingrese sus apellidos: ")
    edad=int(input("Ingrese su edad: "))

elif op == "4":
    print("Los datos ingresados son:", Nombre, Apellido, edad)

elif op == "5":
    Simbolo=input("Ingrese un símbolo: ")
    Numero=int(input("Ingrese un número: "))

    Contraseña=(Apellido[0:3])+(Nombre[1:3])+str(edad)+Simbolo+str(Numero)

    print("Tu contraseña personalizada es:", Contraseña)

else:
    print("Opción no válida")
    



















i = 5

while i <= 5 and i > 0:
    print(i)
    i = i - 1

print("fin codigo")