#entrada
lv=int(input("Digite la lectura anterior de kilovatios usados"))
la=int(input("Digite la lectura actual de kilovatios usados"))
c=float(input("Digite el costo por kilovatio"))
#caja negra
f=abs(la-lv)*c
print("Total que debera pagar para el recibo de la luz",f)


