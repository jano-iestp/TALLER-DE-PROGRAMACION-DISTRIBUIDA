#5.	Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos alumnos aprobaron y desaprobaron considerando que la nota mínima para aprobar es 13


aprobado =0
desaprobado =0
i =0
suma =0


while i<10:
    n=int(input("Ingrese la nota "))
    
    if (n>=13):
        aprobado=aprobado+1
    else:
        desaprobado = desaprobado+1
    i =i+1

print("La cantidad de alumnos aprobados es: " , aprobado)
print("La cantidad de alumnos desaprobados es: " , desaprobado)



