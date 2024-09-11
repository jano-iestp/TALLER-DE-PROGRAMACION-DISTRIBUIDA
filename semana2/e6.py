#6.	En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.


cantidad = int(input("ingrese la cantidad de empleados "))
i=0
mas =0
entre =0
suma=0


while i<cantidad:
    sueldo=int(input("Ingrese el sueldo entre 100 y 500 "))
    suma =suma + sueldo
    if (sueldo >=100 and sueldo <=500):
        if (sueldo <=300 and sueldo >=100):
            entre=entre+1
        else:
            mas = mas+1

        i =i+1
    else :
        print("ERROR: ingrese una cantidad entre 100 y 500 " )


print("La cantidad de empleados con sueldos entre 100 y 300 es: " , entre)
print("La cantidad de empleados con sueldos mayores a 300 es : " , mas)
print("El importe total que gasta la empresa en sueldos es : " , suma)

