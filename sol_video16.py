#Programa que se ingrese por teclado días de la semana hasta que se digite
#la palabra fin.
#El programa debe indicar cuántos días se digitaron
#Debe mostrar el día de la semana de mayor frecuencia y las veces que aparece
#Solo se deben usar tuplas
#Ejemplo:
#lunes lunes martes jueves viernes lunes martes fin
# El día de mayor frecuencia es: lunes
# El número de veces que aparece es: 3 
dia=''
dias_semana=()
while dia!='fin':
    dia=input("Digite un día de la semana: ")
    if dia!='fin':
        dias_semana=dias_semana+(dia,)

print(dias_semana)

max=0
dia_max=''
for i in range(0,len(dias_semana)):
    cantidad=dias_semana.count(dias_semana[i])
    if cantidad>max:
        max=cantidad
        dia_max=dias_semana[i]

print("El día de mayor frecuencia es: ", dia_max)
print("El número de veces que aparece es: ", max)

