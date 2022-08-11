#entradas
nombre_cilente=str(input("Digite ell nombre del cliente:"))
monto_compra=int(input("Digite el valor de la compra del cliente:"))
#caja negra

monto_pagar=""
if(monto_compra<50000):
    monto_pagar=(monto_compra)
elif(monto_compra>50000 and monto_compra<=100000):
    monto_pagar=(monto_compra-(monto_compra+0.05))
elif(monto_compra>100000 and monto_compra<=700000):
    monto_pagar=(monto_compra-(monto_compra*0.11))
elif(monto_compra>700000 and monto_compra<=1500000):
    monto_pagar=(monto_compra-(monto_compra*0.18))
elif(monto_compra>1500000):
    monto_pagar=(monto_compra-(monto_compra*0.25))

descuento=""
if(monto_compra<50000):
    descuento=("No hoy descuento")
elif(monto_compra>50000 and monto_compra<=100000):
    descuento=(monto_compra*0.05)
elif(monto_compra>100000 and monto_compra<=700000):
    descuento=(monto_compra*0.11)
elif(monto_compra>700000 and monto_compra<=1500000):
    descuento=(monto_compra*0.18)
elif(monto_compra>1500000)
    descuento=(monto_compra*0.25)

#salidas
print(f"{nombre_cliente}")
print(f" el monto de la compra es :{monto_compra}")
print(f" el monto final a pagar es :{monto_pagar}")
print(f" el descuento fue de :{descuento}")