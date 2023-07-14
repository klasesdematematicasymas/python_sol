#Una tienda ofrece una prenda de ropa por USD $10.00 junto con la 
#promoción de que si la compra es de 6 o más prendas cada una
#tiene un descuento del 20% (valor unitario de USD $8.00)
#Desarrolle un programa que lea por teclado la cantidad de
#prendas compradas y que calcule el valor de la compra.
x=int(input("Digite la cantidad de prendas: "))
if x<6:
    valor=10*x
    print("El valor de la compra es: ", valor)
else:
    valor=8*x
    print("El valor de la compra es: ", valor)
print("Recuerda suscribirte")