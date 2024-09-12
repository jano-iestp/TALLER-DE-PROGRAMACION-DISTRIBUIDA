#1.Desarrollar un programa que permita la carga de 5 valores por teclado y nos muestre la suma de los valores ingresados y su promedio. 

suma =0

for  i in range(0,5):
    x = int(input("Ingre el valor: "))
    suma = suma +1

print("La suma de los valores ingresados es: ",suma)
print("La suma de los valores ingresados es: ",(suma/5))

