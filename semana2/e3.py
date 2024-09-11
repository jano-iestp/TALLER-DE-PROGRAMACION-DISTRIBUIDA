#3.	Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.


cantidad = int(input("ingrese la cantidad de las peronsas "))

i =0
suma =0


while i<cantidad:
        altura = int(input("ingrese la altura "))
        suma = suma + altura
        i = i+1

promedio =suma/cantidad
print("La altura promedio del conjunto de personas es ", promedio)





