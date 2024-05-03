print('Programa para Obtener el Pago de un Producto: ')

Po = str(input("Ingrese el Nombre del Producto a Comprar: "))
Pe = float(input("Digite el Precio del Producto: "))
Ca = int(input("Digite la Cantidad de Artículos que desea Comprar: "))

T = (Pe * Ca)

print ('  __________________________________ ')
print ('')
print ('            Ticket de Compra:        ')
print ('')
print ('     ', Ca , 'x' , Po , '-' , Pe)
print ('')
print ('            Total: ', T ,'        ')
print ('  __________________________________ ')