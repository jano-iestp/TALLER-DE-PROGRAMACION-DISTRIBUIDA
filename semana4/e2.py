#Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 13 y cuántos menores.

mayor =0
menor =0

for  i in range(10):
    x = int(input("Ingre la nota del alumno: "))
    if (x>=13):
        mayor = mayor +1
    else :
        menor =menor +1


print("La suma de los valores ingresados es: ",mayor)
print("La suma de los valores ingresados es: ",menor)