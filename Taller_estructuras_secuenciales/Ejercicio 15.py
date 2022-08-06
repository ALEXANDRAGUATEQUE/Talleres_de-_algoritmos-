#entradas
pf=int(input("digite el precio final pagadopor un producto"))
pvp=int(input("inserte el precio de venta  al publico"))
#caja negra
a=(pvp-pf)
b=(a/pvp*100)
#salidas
print("porcentaje de descuentoque le ha sido aplicado es:", b,"%")
