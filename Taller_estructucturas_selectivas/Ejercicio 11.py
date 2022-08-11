#entradas
temperatura=float(input(" Digite temperatura "))
# Caja Negra 
deporte=''
if(temperatura>85 and temperatura < 120):
    deporte= "Natacion "
elif(temperatura>70 and temperatura<= 85 ):
    deporte= "Tenis "
elif(temperatura>32 and temperatura<= 70 ):
    deporte = "Golf "
elif(temperatura>10 and temperatura<= 32 ):
    deporte = "Esqui "
elif(temperatura =0 and temperatura <= 10 ):
    deporte = "Marcha "
else:
    deporte= "No hay ningun deporte a practicar"
# Datos de Salida
print(f"El deporte apropiado para practicar es : {deporte} ")