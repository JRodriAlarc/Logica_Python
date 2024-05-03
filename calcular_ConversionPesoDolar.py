print ('Programa para Calcular la Equivalencia de Pesos a Dólares: ')

C = float (input ("Ingrese la Cantidad que desea Convertir: ") )
Tc = float (input ("Ingrese la Taza de Cambio del Dólar a Peso Mexicano: ") )

E = (C / Tc)

print (" ->" , C , "Pesos son equivalentes a" , round (E,3) , "Dólares")