#Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5.


multi5 =0
multi3 =0

for  i in range(0,10):
    x = int(input("Ingre el valor del numero: "))
    if (x%3==0):
        multi5 = multi5 +1
    if (x%5==0) :
        multi3 =multi3 +1


print("La suma de los valores ingresados es: ",multi5)
print("La suma de los valores ingresados es: ",multi3)





