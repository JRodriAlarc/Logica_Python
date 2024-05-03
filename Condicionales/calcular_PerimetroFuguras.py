print('Seleccione La Figura de la Cual desea Calcular el Perimetro:')
print('1.- Un Rectangulo')
print('2.- Un Triangulo')

opc = int(input())

if (opc == 1): 

    print("Programa para Calcular el Perimetro de un Rectangulo")

    A = float(input("Ingrese la Base de la Figura: "))
    B = float(input("Ingrese la Altura de la Figura: "))

    R2 = (2*B)+(2*A)

    print ("El Perimetro del Rectangulo es %s" % R2)
    
if (opc == 2):
    
    L1 = float(input("Ingrese el Primer lado de la Figura: "))
    L2 = float(input("Ingrese el Segundo lado de la Figura: "))
    L3 = float(input("Ingrese el Tercer lado de la Figura: "))

    R1 = (L1+L2+L3)

    print ("El Perimetro del Triangulo es %s" % R1)

if opc < 1 or opc > 2:
  print('Seleccione una Opción Existente')