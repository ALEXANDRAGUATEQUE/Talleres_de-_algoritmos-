#entradas
categoria=int(input("Digite la categoria:"))
sueldo_bruto=int(input("Digite el salario bruto:"))
#caja negra______aumento qu tendra el empleado de acuerdo a su salario 
aumento=""
if(categoria==1 and sueldo_bruto==5000000):
    aumento=(sueldo_bruto*0.10)
if(categoria==2 and sueldo_bruto==4300000):
    aumento=(sueldo_bruto*0.15)
if(categoria==3 and sueldo_bruto==3600000):
    aumento=(sueldo_bruto*0.20)
if(categoria==4 and sueldo_bruto==2000000):
    aumento=(sueldo_bruto*0.40)
if(categoria==5 and sueldo_bruto==900000):
    aumento=(sueldo_bruto*0.60)
else:
    aumento=("No hay aumento")

#_______________nuevo sueldo bruto
if(categoria==1 and sueldo_buto==5000000):
    nuevo_sueldo=((sueldo_bruto*0.10)+sueldo_bruto)
if(categoria==2 and sueldo_buto==4300000):
    nuevo_sueldo=((sueldo_bruto*0.15)+sueldo_bruto)
if(categoria==3 and sueldo_buto==3600000):
    nuevo_sueldo=((sueldo_bruto*0.20)+sueldo_bruto)
if(categoria==4 and sueldo_buto==2000000):
    nuevo_sueldo=((sueldo_bruto*0.40)+sueldo_bruto)
if(categoria==5 and sueldo_buto==900000):
    nuevo_sueldo=((sueldo_bruto*0.60)+sueldo_bruto)
else:
    nuevo_sueldo=("el sueldo se matendra igual:",sueldo_bruto)
print(f"la categoria de trabajdor es: {categoria}, el aumento que tendra sera {aumento} y su nuev sueldo bruto va a ser de {nuevo_sueldo}")



