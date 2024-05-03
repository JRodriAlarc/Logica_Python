print("Programa para leer dos números: ")

A = float(input("Ingrese un Primer Núemro: "))
B = float(input("Ingrese un Segundo Núemro: "))

if ( A == B ):
    R = (A * B)
    print ("El Resultado de la Multiplicación es: ",R)
elif ( A > B ):
    R = (A - B)
    print ("El Resultado de la Resta es: ",R)
else:
    R = (A + B)
    print ("El Resultado de la Suma es: ",R)