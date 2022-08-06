#entradas
#matematicas
examen_m=float(input("Examen matematicas1:"))
tarea_1_m=float(input("Digite tarea matematicas1"))
tarea_2_m=float(input("Digite tarea matematicas2"))
tarea_3_m=float(input("Digite tarea matematicas3"))
#fisica
examen_f=float(input("Examen fisica1:"))
tarea_1_f=float(input("Digite tarea fisica1"))
tarea_2_f=float(input("Digite tarea fisica2"))
#quimica
examen_q=float(input("Examen quimica1:"))
tarea_1_q=float(input("Digite tarea quimica1"))
tarea_2_q=float(input("Digite tarea quimica2"))
tarea_3_q=float(input("Digite tarea quimica3"))
#caja negra
ma=examen_m*0.90+((tarea_1_m+tarea_2_m+tarea_3_m)/3)*0.10
fi=examen_f*0.80+((tarea_1_f+tarea_2_f)/2*0.20)
qu=examen_q*0.85+((tarea_1_q+tarea_2_q+tarea_3_q)/3*0.15)
promedio=(ma+fi+qu)/3
#salida
print(f"Matematicas {ma} , Fisica {fi} , Quimica {qu}, el promedio del semestre es:{promedio}")