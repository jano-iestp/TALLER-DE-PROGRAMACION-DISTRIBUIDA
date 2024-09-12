# Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
#Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
cuadrante1 =0
cuadrante2 =0 
cuadrante3 =0
cuadrante4 =0 
ejex = 0
ejey=0
origen =0

cantidad = int(input("Ingrese la cantidad de coordenadas que quieras ingresar: "))

for  i in range(0,cantidad):
    abscisa = int(input("Ingre el valor de la abscisa: "))
    ordenada = int(input("Ingre el valor de la ordenada: "))

    if (abscisa >0 and ordenada > 0):
        cuadrante1 = cuadrante1 +1
        print("Pertenece al 1er cuadrante")
    elif (abscisa <0  and ordenada >0):
        cuadrante2 = cuadrante2 +1
        print("Pertenece al 2do cuadrante")
    elif (abscisa <0 and ordenada <0):
        cuadrante3 = cuadrante2 +1
        print("Pertenece al 3er cuadrante")
    elif (abscisa >0 and ordenada <0):
        cuadrante4 = cuadrante4 +1
        print("Pertenece al 4to cuadrante")
    elif (abscisa != 0 and ordenada == 0):
        ejex = ejex +1
        print("Pertenece al eje X")
    elif (abscisa == 0 and ordenada != 0):
        ejey = ejey +1
        print("Pertenece al eje Y")
    else :
        origen = origen +1
        print("Es el origen")

print("La cantidad de coordenadas pertencientes al 1er cuadrante es : ",cuadrante1)
print("La cantidad de coordenadas pertencientes al 2do cuadrante es : ",cuadrante2)
print("La cantidad de coordenadas pertencientes al 3er cuadrante es : ",cuadrante3)
print("La cantidad de coordenadas pertencientes al 4to cuadrante es : ",cuadrante4)
print("La cantidad de coordenadas pertencientes al eje X es : ",ejex)
print("La cantidad de coordenadas pertencientes al eje Y es : ",ejey)
print("La cantidad de coordenadas pertencientes al origen es : ",origen)

