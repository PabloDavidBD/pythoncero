#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
n = int(input("Ingrese la cantidad de cauchos a comprar: "))
p = float(input("Ingrese el precio unitario: "))
if n > 6:
    s= n*p 
    d= s*0.15
    total=s-d
else: 
    
    s= n*p
    d= s*0.1
    total= s-d 
print("El total a pagar es: ", total)
print ("El total descuento : ",d)
