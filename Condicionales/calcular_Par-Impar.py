print("Programa para leer un Número e Identificar si es Par o Impar: ")

numero = float(input("Ingrese un Número: "))
modulo = numero % 2

if ( modulo == 0):
    print("El Número:" , numero , "es Par ")
else:
    print("El Número:" , numero , "es Impar ")
