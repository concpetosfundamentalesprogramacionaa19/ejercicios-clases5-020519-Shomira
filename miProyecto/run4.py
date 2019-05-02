'''Deseamos obtener el costo de una carrera universitaria
el valor promedio de cada ciclo es de 1200$, el valor promedio 
del seguro educativo por ciclo es de 100$ si la edad del estudiante es menor o igual a 20
caso contrario sera de 150$.
Si el estudiante tiene una modalidad adistancia el numero de ciclos a seguir es de 10
caso contrario debera seguir 8 ciclos.
Obtener la proyeccion del costo de la carrera d eun estudiante 
'''
#Valor del ciclo es de 1200
print("CALCULO DEL VALOR DE UNA MATRICULA ")
#Ingreso de datos del estudiante 
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
modalidad = input ("Ingrese la modalidad si es ingrese 1 si es  Adistancia y 2 si es  Presencial: ")

#convertimiento de string a entero para comparar
modalidad = int (modalidad)
edad = int (edad)

#inicializacion del costo inicial 
costoMatricula = 1200

#Comparacion para determinar la modalidad
if modalidad == 1 :
	costoMatricula = costoMatricula * 10
else:
	if modalidad == 2 :
		costoMatricula = costoMatricula * 8

#Determinacion de la edad para el costo del seguro
if (edad <= 20) and (modalidad == 1):
	costoSeguro = 100 * 10
	costoMatricula = costoMatricula + costoSeguro
else:
	costoSeguro = 150 * 10
	costoMatricula = costoMatricula + costoSeguro
	
if (edad <= 20) and (modalidad == 2):
	costoSeguro = 100 * 8
	costoMatricula = costoMatricula + costoSeguro
else:
	costoSeguro = 150 * 8
	costoMatricula = costoMatricula + costoSeguro



print("Estimad@ %s El costo de su matricula es %d" %( nombre, costoMatricula))








