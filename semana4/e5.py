#Confeccionar un programa que lea n datos, cada dato corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12


mayor=0

cantidad = int(input("Ingrese la cantidad de triangulos que quieras analizar: "))

for  i in range(0,cantidad):
    base = int(input("Ingre el valor de la base: "))
    altura = int(input("Ingre el valor de la altura: "))
    superficie = base*altura

    print("El valor de la base es  : ",base)
    print("El valor de su altura es  : ",altura)
    print("El valor de su superficie es  : ",superficie)
    
    if (superficie>12):
        mayor = mayor +1
 

print("La cantidad de triangulos  cuya superficie es mayor a 12 es : ",mayor)



