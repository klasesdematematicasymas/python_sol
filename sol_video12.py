#Indicar si un número entero ingresado por teclado es primo o no
#si no resulta ser primo debe mostrar dos factores que multiplicados den el número
#Un número primo es aquel número mayor a 1 que solo se puede dividir 
#entre el mismo y la unidad
#Ejemplo
#11 es primo
#12 no es primo 2 * 6 = 12
num = int(input("Digite un número: "))
j=2
if num > 1:
    while j<num:
        if num % j==0:
            print(num, " no es un número primo")
            print(j, " * " , num//j , " = ", num)    
            break        
        else:
            print(num, " es un número primo")
            break
        j+=1
else:
    print(num," no es un número primo")