#entradas
n=str(input("digite su numero"))
hn=int(input("digite numero de horas normales trabajadas"))
p=float(input("digite pagp por hora normal trabajada"))
he=int(input("digite cantidad de horas extras trabajadas"))
x=int(input("digite la cantidad de hijos"))
#caja negra 
sb=p*(hn)
a=(250000+173000*(x)+18000)
de=sb*(0.14)
d=sb-de
ce=(p*he)
cx=(ce*0.25)+ce
sn=(a+d+cx)
#salida
print("Las asignacicones son de ",a)
print("las deducciones son de ",de)
print(f"el sueldo neto que  recibira {n} en el mes de diciembre es: {sn}")