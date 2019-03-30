from random import *
inicial = int(input("ingresa la cantidad inicial: "))
max= int(input("ingresa la cantidad maxima: "))
dia= 0 
while inicial <= max:
    inicial= inicial * 2 
    dia = dia + 1 
print("la cantidad de bacterias excede al maximo permitido en el dia: ",dia)