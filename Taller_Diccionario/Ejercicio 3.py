usuarios = {
 "iperurena": {
 "nombre": "Iñaki",
 "apellido": "Perurena",
 "password": "123123"
 },
 "fmuguruza": {
 "nombre": "Fermín",
 "apellido": "Muguruza",
 "password": "654321"
 },
 "aolaizola": {
 "nombre": "Aimar",
 "apellido": "Olaizola",
 "password": "123456"
 }
}
contador=1
u=str(input("Inserte el usuario"))
c=int(input("Inserte el numero de su contraseña "))

while True:
    if u=="iperuna" in usuarios and c==123123:
        a=(usuarios["iperurena"])
        if (usuarios["iperurena"]["pasword"]==123123):
            print(a["nombre"])
            print(a["apellido"])
        break



elif u=="fmuguruza" in usuarios and c==654321:
     b=(usuarios["fmuguruza"])
        if (usuarios["fmuguruza"]["pasword"]==654321):
            print(b["nombre"])
            print(b["apellido"])
        break

else u=="aolaizola" in usuarios and c==123456:
     c=(usuarios["aolaizola"])
        if (usuarios["aolaizola"]["pasword"]==123456):
            print(c["nombre"])
            print(c["apellido"])
        break
else:
u=int(input("Inserte el usuario"))
c=int(input("Inserte el numero de su contraseña "))
contador=contador+1
print("Contraseña o Usuario incorrectos")
 
if contador==3:
    break








    