print ("Programa para Calcular el Perimetro de un Triangulo Rectangulo: ")

B = float(input("Ingrese la base del Triangulo: "))
A = float(input("Ingrese la altura del Triangulo: "))

R1 = (B**2)+(A**2)
C = pow(R1,0.5)
S = (A + B + C)

print ("El Perimetro del Triangulo Rectangulo es: %s" % round(S,4))