#Un programa en Python que solicite el ancho y alto de un rectángulo
#Esos valores pueden ser números reales
#Que se utilice la función eval() para calcular y mostrar 
#el área y perímetro del rectángulo.
#La respuesta debe estar redondeada a dos cifras decimales.
ancho=float(input("Digite el ancho del rectángulo: "))
alto=float(input("Digite el alto del rectángulo: "))
print("El perímetro es: ", round(eval("2*ancho+2*alto"),2))
print("El área es: ", round(eval("ancho*alto"),2))