# Realizar un programa que lea los lados de n triángulos, e informar:
#a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b) Cantidad de triángulos de cada tipo

suma=0
equilatero =0
isoceles =0 
escaleno =0

cantidad = int(input("Ingrese la cantidad de triangulos que quieras analizar: "))

for  i in range(0,cantidad):
    lado1 = int(input("Ingre el valor del lado 1: "))
    lado2 = int(input("Ingre el valor del lado 2: "))
    lado3 = int(input("Ingre el valor del lado 3: "))
    suma = suma +1

    if (lado1 ==lado2 and lado2 == lado3):
        equilatero = equilatero +1
        print("Es un triangulo equilatero")
    elif (lado1 != lado2 and lado2 != lado3):
        escaleno = escaleno +1
        print("Es un triangulo escaleno")
    else :
        isoceles = isoceles +1
        print("Es un triangulo isoceles")

print("La cantidad de triangulos equilatero es  : ",equilatero)
print("La cantidad de triangulos isoceles es  : ",isoceles)
print("La cantidad de triangulos escaleno es  : ",escaleno)
    
    