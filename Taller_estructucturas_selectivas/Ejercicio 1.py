#ENTRADAS
dinero_inicial=int(input(" Digite la cantidad que va a invertir "))
inte_banco=float(input(" Digite porcentaje de intereses el cual paga su banco"))
#caja negra
intereses=(dinero_inicial+inte_banco/100)
if(intereses>100000)
#salida
print(f"el valor que tendra al final en su cuenta y que volvera a reinvertir es de {intereses+dinero_inicial}",(f"y el dinero que le fue generado por los intereses es de {intereses}"))
else:
    print(f"el valor que tendra al final en su cuenta sera {intereses+dinero_inicial} y el valor a reinvertir sera de {dinero_inicial}")
