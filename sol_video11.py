#Programa en donde la persona digite por teclado un mes (todo en minúscula)
#Y el programa le muestre por consola a qué trimestre pertenece
#Ejemplo
#Se digita: mayo
#Se muestra por consola: Segundo Trimestre
A=input("Digite un mes (todo en minúscula): ")

match A:
    case "enero":
        print("Primer trimestre")
    case "febrero":
        print("Primer trimestre")
    case "marzo":
        print("Primer trimestre")
    case "abril":
        print("Segundo trimestre")
    case "mayo":
        print("Segundo trimestre")
    case "junio":
        print("Segundo trimestre")
    case "julio":
        print("Tercer trimestre")
    case "agosto":
        print("Tercer trimestre")
    case "septiembre":
        print("Tercer trimestre")
    case "octubre":
        print("Cuarto trimestre")
    case "noviembre":
        print("Cuarto trimestre")
    case "diciembre":
        print("Cuarto trimestre")
print("Recuerda suscribirte")