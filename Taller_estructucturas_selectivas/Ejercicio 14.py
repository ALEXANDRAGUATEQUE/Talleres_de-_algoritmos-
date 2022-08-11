# Entradas
lv=int(input("digite la lectura anterior de kivolatios usados "))
la=int(input("digite la lectura actual de kivolatios usados "))
consumo=abs(la-lv) 
# Caja Negra
monto_pagar=""
if(consumo>=0)or(consumo<=100):
    monto_pagar=(consumo*4600) 
elif(consumo>=101)or(consumo<=300):
    monto_pagar=(consumo*80.00)
elif(consumo>=301)or(consumo<=500):
    monto_pagar=(consumo*100_000)
elif(consumo>=501):
    monto_pagar=(consumo*120_000)
# Salidas
print(" Monto final que debera pagar por el consumo de luz electrica y aseo urbano es de :", monto_pagar)