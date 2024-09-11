#7.	Realizar un programa que permita cargar dos listas de 10 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

i=0
j=0
suma1=0
suma2=0


while i<10:
    lista1=int(input("Ingrese un valor de la primera lista "))
    suma1 =lista1 + 1
    i =i+1

while j<10:
    lista2=int(input("Ingrese un valor de la segunda lista  "))
    suma2 =lista2 + 1
    j =j+1

if (suma1 >suma2):
    print("La lista mayor es la primera: " )
elif (suma1 <suma2):
    print("La lista mayor es la 2da: " )
elif (suma1 == suma2):
    print("Las lista son iguales: " )

