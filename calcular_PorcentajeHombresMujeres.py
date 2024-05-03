print ('Programa para Calcular el Porcentaje de Hombres y Mujeres que hay en un Grupo de Estudiantes: ')

H = int (input ("Ingrese la Cantidad de Hombres que hay en el Grupo: ") )
M = int (input ("Ingrese la Cantidad de Mujeres que hay en el Grupo: ") )

T = (H + M)
PH = (H * 100) / T
PM = (M * 100) / T

print()
print (' - El Porcentaje de Hombres es: ', round (PH, 1))
print (' - El Porcentaje de Mujeres es: ', round (PM, 1))