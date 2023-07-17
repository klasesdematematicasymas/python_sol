#Un programa que pida una lista de nombres.
#El usuario debe detener el ingreso de nombres cuando digite la palabra "fin"
#Posteriormente debe mostrar la cantidad de nombres ingresados
#Debe mostrar todos los nombres ingresados ordenados alfabéticamente
nombre=""
listado=[]
while nombre!="fin":
    nombre=input("Digite un nombre: ")
    listado.append(nombre)

del listado[len(listado)-1]
print("La cantidad de nombres digitados es: ", len(listado))
listado.sort()
print(list(listado))
print("Recuerda suscribirte")