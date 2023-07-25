#Programa que reciba una palabra por teclado, deje todas las vocales sin 
# acentos (tildes) y todas las letras en minúscula. Posteriormente que 
# verifique si la palabra es palíndroma 
# (Leida de izquierda a derecha es igual que de derecha a izquierda)
#Ejemplo - Entrada:
#Digite una palabra: Elévele
#Salida:
#La palabra  elevele  es un palíndromo

def tildes(texto:str):
    texto=texto.lower()
    texto=texto.replace("á","a")
    texto=texto.replace("é","e")
    texto=texto.replace("í","i")
    texto=texto.replace("ó","o")
    texto=texto.replace("ú","u")
    return texto

def palindromo(texto:str):
    pal=True
    for i in range(0,len(texto)):
        if texto[i] != texto[len(texto)-1-i]:
            pal=False
            break
    return pal        
        
txt=input("Digite una palabra: ")
txt=tildes(txt)
if palindromo(txt): 
    print("La palabra ", txt, " es un palíndromo")
else:
    print("La palabra ", txt, " no es un palíndromo")
