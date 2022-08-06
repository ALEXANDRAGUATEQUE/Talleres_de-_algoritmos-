#ENTRADA
Parcial_uno=int(input("Digite la nota del parcial uno "))
Parcial_dos=int(input("Digite la nota del parcial dos"))
Parcial_tres=int(input("Digite la nota del parcial tres "))
Examen_final=int(input("Digite la nota del examen final "))
Trabajo_final=int(input("Digite la nota del trabajo final "))
#CAJA NEGRA
calificacionfinal=((Parcial_uno+Parcial_dos+Parcial_tres)/3)*0.55+Examen_final*0.30+Trabajo_final*0.15
#SALIDA
print=("calificacion",calificacionfinal)
