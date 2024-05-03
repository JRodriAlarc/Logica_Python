print ("Programa para Calcular la Suma de 6 Números e identificar los que son Pares e Impares: ")

Acum = int ( 0 )
Cont = int ( 1 )
Pares = int ( 0 ) 
Impares = int ( 0 )

while  Cont <= 6:
    n = int (input ("Digite la Cantidad: ") )
    Acum = Acum + n

    if ( n % 2 == 0 ):
        Pares = Pares + 1
    else:
        Impares = Impares + 1 
    
    Cont = Cont + 1

print ( " - La Suma de los Números es: " , Acum )
print ( " - Los Números Pares Son: " , Pares )
print ( " - Los Números Impares Son: " , Impares )