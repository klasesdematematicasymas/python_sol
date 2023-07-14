#Digitar tres números enteros por teclado y mostrar en pantalla el menor
A=int(input("Digite el primer número: "))
B=int(input("Digite el segundo número: "))
C=int(input("Digite el tercer número: "))
if A<B<C:
    print("El menor es: ", A)
if B<A<C:
    print("El menor es: ", B)
if C<A<B:
    print("El menor es: ", C)