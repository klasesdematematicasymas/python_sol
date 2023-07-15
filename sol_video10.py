#El programa debe leer la fecha del sistema
#Y debe mostrar el día de la semana (lunes, martes, etc.)
from datetime import date

hoy=date.today()
w=date.weekday(hoy)
#0 Lunes, 1 Martes, ..., 5 sábado, 6 domingo
if w==0:
    print("Lunes")
elif w==1:
    print("Martes")
elif w==2:
    print("Miércoles")
elif w==3:
    print("Jueves")
elif w==4:
    print("Viernes")
elif w==5:
    print("Sábado")
else:
    print("Domingo")
print("Recuerda Suscríbirte")
