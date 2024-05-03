print('Programa para Obtener el salario neto de un Trabajador: ')

HT = float(input("Ingrese el Numero de Horas Trabajadas: "))
ST = float(input("Ingrese el Salario Pecibido por Hora: "))
TI = float(input("Ingrese la tasa de Impuestod que debe Pagar: %"))

S = (HT*ST)
IP = (S/100)*(TI)
SN = (S-IP)

print("Su salario Neto es: ",SN)