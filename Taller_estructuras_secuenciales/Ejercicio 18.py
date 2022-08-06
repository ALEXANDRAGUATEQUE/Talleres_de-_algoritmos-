#entradas
x=int(input("cantidad de bolivares prestados"))
y=int(input("cantidad de intereses pagados"))
#caja negra
r=((y*100)/(x*4))
p=r/4
#salida
print("el porcentaje anual de intereses que pago durante el plazo de cuatro años es de :", p , "%")
