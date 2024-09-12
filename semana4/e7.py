#7.	Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
#Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

x = int(input("Ingrese un valor entre el 1 y el 10 "))
if (x >=1 and x <=10):
    for  i in range(0,12):
        print("",i, " x ",x, " = ", (i*x))
    
else :
    print("ERROR: Ingrese un valor entre 1 y el 10 ")




