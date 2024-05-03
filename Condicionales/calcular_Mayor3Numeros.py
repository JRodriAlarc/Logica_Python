print("Programa para leer tres Números Diferentes: ")

A = float(input("Ingrese un Primer Número: "))
B = float(input("Ingrese un Segundo Número: "))
C = float(input("Ingrese un Tercer Número: "))

if ( A == B and B == C ):
    print ("Los Tres Números: " , A , B , C , " Son Iguales ")

elif ( A > B and A > C ):
    print ("El Primer Número: " , A , " es el Mayor ")

elif ( B > A and B > C ):
    print ("El Segundo Número: " , B , " es el Mayor ")

else :
    print ("El Tercer Número: " , C , " es el Mayor ")
    
#Comentario: