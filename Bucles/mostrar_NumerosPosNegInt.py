print("Programa para analizar 20 Números e imprimir cuantos son Positivos, cuantos Negativos y cuantos neutros: ")

ContNeg = 0
ContPos = 0
ContNeu = 0

for  cont in range(20):
    C1 = float(input("Ingrese un Número: "))

    if ( C1 == 0 ):
        ContNeu = ContNeu + 1
    elif ( C1 > 0 ):
        ContPos = ContPos + 1
    elif ( C1 < 0 ):
        ContNeg = ContNeg + 1

print ("  - La Cantidad de Números Positivos es: ", ContPos)
print ("  - La Cantidad de Números Neutros es: ", ContNeu)
print ("  - La Cantidad de Números Negativos es: ", ContNeg)