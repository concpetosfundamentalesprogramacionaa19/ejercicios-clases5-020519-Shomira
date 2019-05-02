'''
file: run2.py
autor: shomira
'''
from misvariables import *

#uso de condicional simple

nota2 = input("Ingrese la nota uno: " )
nota= input("Ingrese la nota dos: " )

nota = int(nota) 
nota2 = int(nota2)

if nota >= 18:
	print( "%s, su valor de nota es %d" % (mensaje, nota))
else:
	print( "%s - %d" % (mensaje2, nota))

if nota2 >= 18 :
	print(mensaje)
else:
	print(mensaje2)


