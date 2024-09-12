#4.	Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.

cantidad = int(input("ingrese la cantidad de numeros enteros "))
i=0
par =0
impar =0


while i<cantidad:
    n=int(input("Ingrese el valor del numero entero "))
    
    if (n%2==0):
        par=par+1
    else:
        impar = impar+1

    i =i+1

print("La cantidad de numeros pares es: " , par)
print("La cantidad de numeros imares es: " , impar)



