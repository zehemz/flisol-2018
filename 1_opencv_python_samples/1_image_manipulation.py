import cv2 as cv
#Tipos de carga de imagen
print(cv.IMREAD_COLOR) # tipo por defecto, se elimina alpha channel
print(cv.IMREAD_GRAYSCALE) # Loads image in grayscale mode
print(cv.IMREAD_UNCHANGED) # carga la imagen con canal alpha

img = cv.imread('demo.jpg', cv.IMREAD_GRAYSCALE)
print(img)

# mostrar imagen..
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
