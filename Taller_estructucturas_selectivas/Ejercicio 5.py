#Entradas
apto_uno=int(input( "Inserte las Ventas que obtuvo el departamento No 1 en el mes : "))
apto_dos=int(input( "Inserte las Ventas que obtuvo el departamento No 2 en el mes : "))
apto_tresr=int(input( "Inserte las Ventas que obtuvo el departamento No 3 en el mes: "))
sueldo_empleados=int(input(" Inserte el salario que tienen los empleados "))
# Caja Negra 

s = ((apto_uno + apto_dos + apto_tresr)*0.33) 
e=(sueldo_empleados*0.2)
sf=(e+sueldo_empleados) 

# Salidas 

if (apto_uno > s):
    
    print(f" Comision que recibiran cada uno de los empleados del departamento No 1 en el mes es de :{e} , por lo tanto su sueldo final es de {sf} ")
else:

    print(f" Los empleados del departamento 1 no recibiran comision , recibiran su salario normal : {sueldo_empleados} ")

if(apto_dos> s):

    print(f" La Comision que recibiran cada uno de los empleados del departamento No 2 en el mes es de :{e}, por lo tanto su sueldo final es de {sf} ")
else:

    print(f"Los empleados del departamento 2 no recibiran comision , recibiran su salario normal : {sueldo_empleados} ")

if(apto_tresr> s ):

    print(f" La Comision que recibiran cada uno de los empleados del departamento No 3 en el mes es de {e} , por lo tanto su sueldo final es de : {sf} ")

else:
    print(f"Los empleados del departamento 3 no recibiran comision , recibiran su salario normal : {sueldo_empleados} ")