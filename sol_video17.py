# Definir los siguientes conjuntos:
# U numeros mayores a 20 y menores o iguales a 50
# A subconjunto de U con números impares
# B subconjunto de U con números múltiplos de 3
#Encontrar: A union B, B diferencia A, U diferencia (A union B)
#A diferencia simétrica B
U=set()
A=set()
B=set()
for i in range(20,51):
    U.add(i)
    if i%2==1:
        A.add(i)
    if i%3==0:
        B.add(i)

print("El conjunto U es \n", U)
print("El conjunto A es \n",A)
print("El conjunto B es \n",B)

print("A unión B: ", A | B)
print("B diferencia A: ", A - B)
print("U diferencia (A union B): ", U - (A | B))
print("A La diferencia simétrica B: ", A ^ B)
