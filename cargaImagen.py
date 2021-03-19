import cv2
import numpy as np

#Cargar la imagen a color
IRGB = cv2.imread('004.jpg')
print(IRGB)
print(IRGB.shape)

#Imprimiendo el tamaño de la imagen como matriz
print('Modificación en la rama main')
print(len(IRGB))
