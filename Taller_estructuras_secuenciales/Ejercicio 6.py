#ENTRADA
Total_m=int(input("Digite tatal de mujeres"))
Total_h=int(input("Digite total de hombres"))
#CAJA NEGRA
resultadom=(Total_m / (Total_m+Total_h))*100
resultadoh=(Total_h / (Total_h+Total_m))*100
print=("El porcentaje de mujeres es :", resultadom)
print=("El porcentaje de hombreses :", resultadoh)