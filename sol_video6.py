#El programa en Python debe pedir tres números por teclado (enteros)
#Debe encontrar y mostrar el mínimo común múltiplo (mcm) de esos numeros
#Debe encontrar y mostrar el máximo común divisor
#Debe mostrar el resultado de cada división entre los números ingresados y el mcm
#ejemplo
#se digitan los números 4,6,8
#El mínimo común múltiplo es: 24
#El máximo común divisor es: 1
#24/4 = 6
#24/6 = 4
#24/8 = 3
import math
x=int(input("Digite el primer número: "))
y=int(input("Digite el segundo número: "))
z=int(input("Digite el tercer número: "))
mcm=math.lcm(x,y,z)
mcd=math.gcd(x,y,z)
print("El mínimo común múltiplo es:", mcm)
print("El máximo común divisor es: ", mcd)
print("", mcm, "/" , x, "= ", mcm/x)
print("", mcm, "/" , y, "= ", mcm/y)
print("", mcm, "/" , z, "= ", mcm/z)