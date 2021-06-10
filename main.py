import numpy
import sys
print("¡Bienvenido al multiplicador de matrices!")
fila1=int(input('Numero de filas de la matriz 1: '))
colum1=int(input('Numero de columnas de la matriz 1: '))
fila2=int(input('Numero de filas de la matriz 2: '))
colum2=int(input('Numero de columnas de la matriz 2: '))
#Verificación de las matrices 
if (colum1 != fila2):
  print("No es posible hacer la multiplicacion")
  sys.exit()
matriz1=numpy.zeros((fila1, colum1))
matriz2=numpy.zeros((fila2, colum2))
matrizResultado=numpy.zeros((fila1, colum2))
print("\nIntroduce los numeros de la matriz 1:\n")
for fila in range (0, fila1):
  for columna in range (0, colum1):
    matriz1[fila, columna] = input("Elemento a ["+str(fila+1)+" , "+str(columna+1)+"]: ")
print("\nIntroduce los numeros de la matriz 2:\n")
for fila in range (0, fila2):
  for columna in range (0, colum2):
    matriz2[fila, columna] = input("Elemento a ["+str(fila+1)+" , "+str(columna+1)+"]: ")
#Empieza la multiplicación
for fila in range (0, fila1):
  for columna in range (0, colum2):
    for x in range (0, fila2):
      matrizResultado[fila][columna] += matriz1[fila][x] * matriz2[x][columna]
#Imprime el resultado
print("\nLa matriz resultante es:\n")
print(matrizResultado)
print("\nElaborado por: Guachamin Daniel\n")