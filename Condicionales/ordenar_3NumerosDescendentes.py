print("Programa para leer tres Números Diferentes y que los Muestre de Manera Descendente: ")

n1 = float(input("Ingrese un Primer Núemro: "))
n2 = float(input("Ingrese un Segundo Núemro:  "))
n3 = float(input("Ingrese un Tercer Núemro:  "))

if ( n1 == n2 == n3 ):
    print ("Los Números: " , n1 , ',' , n2 , ',' , n3 , " Son Iguales ")

        # >=
elif ( n1 > n2 and n1 > n3): # N1 es el Mayor
    
    if( n2 > n3):
        print (n3)
        print (n2)
        print (n1)
    else:
        print (n2)
        print (n3)
        print (n1)

elif ( n2 > n1 and n2 > n3): # N2 es el Mayor

    if( n1 > n3):
        print (n3)
        print (n1)
        print (n2)

    else:
        print (n1)
        print (n3)
        print (n2)

elif ( n3 > n2 and n3 > n1): # N3 es el Mayor

    if( n1 > n2):
        print (n2)
        print (n1)
        print (n3)

    else:
        print (n2)
        print (n1)
        print (n3)