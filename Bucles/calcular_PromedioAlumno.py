print("Programa para Calcular el Promedio de un Alumno: ")

TC = int(input("Ingrese el Número de Calificaciones que desea Calcular: "))
Acum = 0

for  cont in range( TC ):
    C1 = float(input("Ingrese su Calificación: "))
    Acum = Acum + C1

Prom = ( Acum / TC )
print (" - Su Pormedio es: ", round( Prom , 2 ))
