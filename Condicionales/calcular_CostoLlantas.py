print("Programa para Calcular el costo a Pagar por unas llantas: ")

n = int(input("Ingrese el Número de llantas que desea comprar: "))

if ( n <= 5 ):
    ts = (n * 800)
    print ("El Total a pagar es: ",ts)
else:
    tn = (n * 700)
    print ("El Total a pagar es: " ,tn)