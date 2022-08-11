
#Es necesario importar las dependencias necesarias
from datetime import date 
#__________________ fecha del sistema
#Dia actual
today = date.today()
#Fecha de hoy
dia_a=today.day
mes_a=today.month
año_a=today.year
#entradas
fecha_nacimiento=input("Digite en este formato:año/mes/dia:")
(año,mes,dia)=fecha_nacimiento.split("/")
año_n=int(año)
mes_n=int(mes)
dia_n=int(dia)
#caja negra
#_______________edad
edad=0
if(mes_a==mes_n)
  if(dia_n>=dia_a):
        edad=(año-a-año_n)
  else:
        edad=(año_a-año_n)
elif(mes_a>mes_n):
     edad=(año_a-año_n)
else:
    (edad=(año_a-año))-1
#________________signo
signo=""
if((dia_n<=22 and mes_n<=11) or (dia_n<=21 and mes_n<=12)):
    signo="Sagitario"
if((dia_n<22 and mes_n<=12) or (dia_n<=20 and mes_n<=1)):
    signo="Capricornio"
if((dia_n<21 and mes_n<=1) or (dia_n<=19 and mes_n<=2)):
    signo="Acuario"
if((dia_n<20 and mes_n<=2) or (dia_n<=19 and mes_n<=3)):
    signo="piscis"
if((dia_n<21 and mes_n<=3) or (dia_n<=20 and mes_n<=4)):
    signo="aries"
if((dia_n<21 and mes_n<=4) or (dia_n<=21 and mes_n<=5)):
    signo="tauro"
if((dia_n<22 and mes_n<=5) or (dia_n<=21 and mes_n<=6)):
    signo="geminis"
if((dia_n<22 and mes_n<=6) or (dia_n<=22 and mes_n<=7)):
    signo="cancer"
if((dia_n<23 and mes_n<=7) or (dia_n<=23 and mes_n<=8)):
    signo="leo"
if((dia_n<24 and mes_n<=8) or (dia_n<=22 and mes_n<=9)):
    signo="virgo"
if((dia_n<23 and mes_n<=9) or (dia_n<=22 and mes_n<=10)):
    signo="libra"
if((dia_n<23 and mes_n<=10) or (dia_n<=21 and mes_n<=11)):
    signo="Escorpio"


#salidas
print(edad)
print(signo)

