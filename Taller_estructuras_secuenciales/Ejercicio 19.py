#entrada 
x=int(input("inserte la cantidad de naranjas compradas"))
y=int(input("inserte el precio por la docena de naranjas"))
k=int(input("inserte el precio en el que vendio las naranjasa los detallistas"))
#caja negra
inv=((x*y)/12)
g=(((k-inv)*100)/inv)
#salida
print("el porcentaje de ganancia obtenido enla inversion es del", g, " % ")