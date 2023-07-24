#Programa se ingresen las notas de diferentes materias por teclado.
#Las llaves del diccionario son los nombres de las materias
#los valores son las notas.
#Se termina de ingresar información cuando en el nombre de la materia
#se digita fin
#Se debe indicar la materia con mayor nota así como con la menor
#Ejemplo:
#entradas
#mate   60
#fisica 70
#quimica 80
#salida
#La mejor materia es quimica con la nota de  80
#la peor materia es mate con la nota de 60
materia=""
materias=dict()
#ingresamos las materias y sus notas
while materia!="fin":
    materia=input("Digite el nombre de la materia: ")
    if materia!="fin":
        nota=int(input("Digite la nota: "))
        materias[materia]=nota
print(materias)

#Seleccionamos la mayor nota
max=0
max_materia=""
for key in materias:
    if max<materias[key]:
        max=materias[key]
        max_materia=key
print("La mejor materia es", max_materia, "con la nota de ", max)

min=1000
min_materia=""
for key in materias:
    if min>materias[key]:
        min=materias[key]
        min_materia=key
print("La peor materia es", min_materia, "con la nota de ", min)
