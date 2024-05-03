print ('Programa para Calcular la Calificación Final de la Materia de Algoritmos: ')

C1 = float (input ("Ingrese su Primera Calificación Parcial: ") )
C2 = float (input ("Ingrese su Segunda Calificación Parcial: ") )
C3 = float (input ("Ingrese su Tercera Calificación Parcial: ") )
Ef = float (input ("Ingrese su Calificación del Examen Final: ") )
Tf = float (input ("Ingrese su Calificación del Trabajo Final: ") )

PC = (C1 + C2 + C3) / 3

PPC = (PC * 0.55)
PEf = (Ef * 0.3)
PTf = (Tf * 0.15)

PF = (PPC + PEf + PTf)

print (" - Su Promedio Final es: " , round(PF, 2))