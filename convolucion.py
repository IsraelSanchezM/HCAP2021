#Bibliotecas importadas
import cv2
import numpy as np

#Función de convolución
def convolucion(IOriginal, Kernel):
    #Variables:
    fr = len(IOriginal) - (len(Kernel) - 1)           #Número de filas de la matriz resultante
    cr = len(IOriginal[0]) - (len(Kernel[0]) - 1)     #Número de columnas de la matriz resultante 
    Res = np.zeros((fr, cr), np.uint8)                          #Matriz resultante

    #For para recorrer las filas
    for i in range(len(Res)):
        #For para recorrer las columnas
        for j in range(len(Res[0])):
            suma = 0  #Resultado de la multiplicación de la imagen con el Kernel
            #For para recorrer las filas del Kernel
            for m in range(len(Kernel)):
                #For para recorrer las columnas del Kernel
                for n in range(len(Kernel[0])):
                    suma += Kernel[m][n] * IOriginal[m + i][n + j] #Multiplicación de matrices
            if suma <= 255:
                Res[i][j] = round(suma) #Sustituyendo el valor de la multiplicación en su celda correspondiente
            else:
                Res[i][j] = 255
    return Res #Se regresa la matriz resultante

#Probando la función
#Variables
K = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]                                                   #Kernel
I = [[2, 0, 1, 1, 1], [3, 0, 0, 0, 2], [1, 1, 1, 1, 1], [3, 1, 1, 1, 2], [1, 1, 1, 1, 1]]   #Imágen
In = np.array(I)  #Array de la imagen en numpy
Kn = np.array(K)  #Array del Kernel en numpy

#Pipeline
IRGB = cv2.imread('004.jpg')                     #Imágen real
IGS = cv2.cvtColor(IRGB, cv2.COLOR_BGR2GRAY)     #Convirtiendo la imagen a escala de grises
print(IGS.shape) #Imprimiendo las dimensiones de la imagen antes de la convolución   

#Realizndo la convolución
R = convolucion(IGS, Kn) #Se hace la matriz resultante mandando a llamar la función de convolución
print(R)   #Se imprime la matriz resultante de la convolución
print(R.shape) #Imprimiendo dimensiones de la imagen después de la convolución

#Guardando la impagen
cv2.imwrite('004C.jpg', R)
