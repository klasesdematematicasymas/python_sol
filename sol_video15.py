#Listar los números primos menores o iguales a un número entero ingresado por teclado 
#Un número primo es aquel número mayor a 1 que solo se puede dividir 
#entre el mismo y la unidad
#Ejemplo
#15 --> 2,3,5,7,11,13

def primo(num):
    is_primo=False
    if num==1:
        is_primo=False
    elif num==2:
        is_primo=True
    else:
        for j in range(2,num):
            if num % j==0:
                is_primo=False    
                break        
            else:
                is_primo=True
                
    return is_primo

numero = int(input("Digite un número: "))

for i in range(1,numero+1):
    if primo(i)==True:
        print(i)

print("Recuerda suscribirte")