print ('Programa para Calcular las Ganancias de una Trabajador más sus Comisiones: ')

Su = float (input ("Diguite su Sueldo Base: ") )
V1 = float (input ("Ingrese el Costo de su Primera Venta: ") )
V2 = float (input ("Ingrese el Costo de su Segunda Venta: ") )
V3 = float (input ("Ingrese el Costo de su Tercera Venta: ") )

Pv1 = (V1 * 0.1)
Pv2 = (V2 * 0.1)
Pv3 = (V3 * 0.1)
Com = (Pv1 + Pv2 + Pv3)

SuT = (Su + Com)

print ("")
print (" - Su Seuldo Total Sera de: " , SuT)