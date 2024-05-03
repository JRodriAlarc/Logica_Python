print("Programa para Calcular la tabla de Multiplicar de Un Número Cualquiera: ")

N = int(input("Ingrese Tabla de Multiplicar que desea Calcular: "))

#for i in [0, 1, 2, 3, 4, 5 ,6 ,7 ,8 , 9, 10]:
    #print(f"{i} * {N} = {i * N}")

for cont in range (10):
    cont = ( cont + 1 )
    R = ( cont * N )
    print( cont , "*" , N , "=", R)
