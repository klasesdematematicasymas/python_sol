#Programa que lea el archivo "video20.txt" y en otro archivo llamado "sol_video20.txt" 
# se guarde el número de líneas, vocales minúsculas sin tílde y número de carácteres por línea
# Al final del archivo se debe copiar la última línea del "video20.txt" 
# pero toda la línea debe estár en mayúscula. 
#Salida
#Cantidad de líneas 10
#línea 1- Aes: 7, Es: 9, Ies: 4, Oes: 8, Ues: 3, número de carácteres: 83
#línea 2- Aes: 11, Es: 8, Ies: 4, Oes: 4, Ues: 0, número de carácteres: 78
#línea 3- Aes: 6, Es: 2, Ies: 2, Oes: 6, Ues: 2, número de carácteres: 47
#línea 4- Aes: 11, Es: 11, Ies: 4, Oes: 5, Ues: 2, número de carácteres: 92
#línea 5- Aes: 8, Es: 5, Ies: 2, Oes: 8, Ues: 3, número de carácteres: 85
#línea 6- Aes: 6, Es: 8, Ies: 5, Oes: 10, Ues: 2, número de carácteres: 85
#línea 7- Aes: 6, Es: 6, Ies: 3, Oes: 8, Ues: 3, número de carácteres: 76
#línea 8- Aes: 8, Es: 10, Ies: 2, Oes: 3, Ues: 2, número de carácteres: 79
#línea 9- Aes: 5, Es: 9, Ies: 2, Oes: 3, Ues: 2, número de carácteres: 57
#línea 10- Aes: 6, Es: 4, Ies: 2, Oes: 2, Ues: 3, número de carácteres: 49
#RECUERDA SUSCRIBIRTE Y APOYAR EL CANAL. SALUDOS. 
lectura=open("video20.txt",'r',encoding='utf-8')
escritura=open('sol_video20.txt', 'w',encoding="utf-8")
texto=lectura.read()
lineas=texto.split("\n")
escritura.write('Cantidad de líneas '+ str(len(lineas))+'\n')
i=1
for linea in lineas:
    txt='línea '+ str(i)+ '- Aes: '+ str(linea.count("a"))
    txt+=', Es: '+ str(linea.count("e"))+ ', Ies: '+ str(linea.count("i"))
    txt+=', Oes: '+ str(linea.count("o"))+ ', Ues: '+ str(linea.count("u"))
    txt+=', número de carácteres: '+ str(len(linea))+ '\n' 
    escritura.write(txt)
    i+=1
escritura.write(lineas[len(lineas)-1].upper())
escritura.close()
lectura.close()
