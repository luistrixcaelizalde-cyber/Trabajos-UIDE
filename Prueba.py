Nombre=input("Ingrese sus nombres: ")
Apellido=input("Ingrese sus apellidos: ")
edad=int(input("Ingrese su edad: "))
Simbolos=["!","#","$","%","&","/","?"]
Numeros=[1,2,3,4,5,6,7,8,9,0]
print("Deseas generar una contraseña?")
respuesta=input("Ingrese si o no: ")
if respuesta=="si":
    Apellido=(Apellido[0:3])
    Nombre=(Nombre[1:3])
    edad=(str(edad)[0:-1])
    Simbolo=(Simbolos[2:5])
    Numero=(Numeros[-3:-1])
    Contraseña=Apellido+Nombre+edad+Simbolo[0]+Simbolo[1]+Simbolo[2]+str(Numero[0])+str(Numero[1])
    print("Tu contraseña es: ", Contraseña)
    
else:    print("No se generará una contraseña")
print("Gracias por usar el programa")
   
    