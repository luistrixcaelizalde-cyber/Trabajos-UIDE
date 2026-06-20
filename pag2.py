print("Bienvenido a mi programa")
alumnos=int(input("Ingrese el número de alumnos: "))
for i in range(alumnos):
    Nombre=input("Ingrese el nombre del alumno: ")
    Apellido=input("Ingrese el apellido del alumno: ")
    edad=int(input("Ingrese la edad del alumno: "))
    calificacion=float(input("Ingrese la calificación del alumno: "))
    
if calificacion>=7.0:
    print("El alumno ", Nombre, Apellido, "aprobó con una calificación de: ", calificacion)    
    
if calificacion<7.0:
    print("El alumno ", Nombre, Apellido, "reprobó con una calificación de: ", calificacion)

if calificacion==10.0:
    print("El alumno ", Nombre, Apellido, "obtuvo la calificación máxima")

if calificacion==0.0:
    print("El alumno ", Nombre, Apellido, "obtuvo la calificación mínima")  
print("los datos del alumno son: ", Nombre, Apellido, edad, calificacion)
