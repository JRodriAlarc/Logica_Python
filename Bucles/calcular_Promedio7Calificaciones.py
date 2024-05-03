print("Programa para Calcular el Promedio de 7 calificaciones de un Alumno: ")

Acum = 0

for  cont in range(7):
    C1 = float(input("Ingrese su Calificación: "))
    Acum = Acum + C1

Prom = ( Acum / 7 )
print (" - Su Pormedio es: ", round( Prom , 2 ))