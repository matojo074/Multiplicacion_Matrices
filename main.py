import numpy
import sys
print("BIENVENIO A MULTIPLICACION DE MATRICES")
print("Porfavor ingrese los datos solicitados teninedo en cuenta las reglas para multiplicar matrices.")
f1=int(input("Numero de filas Matriz 1: "))
c1=int(input("Numero de columnas Matriz 1: "))
f2=int(input("Numero de filas Matriz 2: "))
c2=int(input("Numero de columnas Matriz 2: "))

if (c1 != f2):
    print("Operacion no valida.")
    sys.exit()
matriz1=numpy.zeros((f1,c1))
matriz2=numpy.zeros((f2,c2))
matrizR=numpy.zeros((f1,c2))

#Ingresar datos alas matrices
print("Introduce los elementos de la matriz 1")
for f in range (0, f1):
    for c in range (0, c1):
        matriz1[f,c] = input("Elemento A[" + str(f+1) + "," + str(c+1) + "]: ")
print("Introduce los elementos de la matriz 2")
for f in range (0, f2):
    for c in range (0, c2):
        matriz2[f,c] = input("Elemento A[" + str(f+1) + ", " + str(c+1) + "]: ")


#Operacion multiplicacion entre matrices
for f in range (0,f1):
    for c in range (0, c1):
        for k in range (0,f2):
            matrizR[f,c]+=matriz1[f,k]*matriz2[k,c]

#Imprimir matriz resultante
print(matrizR)