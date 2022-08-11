#entradas
monto_total=int((input("Inserte el monto total de la compra : ")))
#caja negra 
#cuando excede 5_000_000
em=(monto_total*0.55)
b=(monto_total*0.30)

#no exede 5_000_000
pe=(monto_total*0.70)
b_2=(monto_total*0.30)
intereses=(monto_total*0.20)
#salidas
if(monto_total<5_000_000):
 print("La cantidad a invertir en los fondos es: ",em)
 print("la cantidad prestada por el banco es :",b)
else: 
 print("La cantidad a invertir en los fondos es: ",pe)
 print("la cantidad prestada a credito de fabricante es :",b_2)
 print("la cantidas por interes es de :",intereses)
