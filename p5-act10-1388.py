import numpy as np
import cv2
#
# lee la imagen en escala de grises
mg = cv2.imread("carro.jpg", cv2.IMREAD_GRAYSCALE)

#
cv2.imshow("carro 1388",mg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#linea
print("La linea 1388")
#crea una imagen negra
img = np.zeros((512,512,3), np.unit8)

#dubyja una diagonal blanca 3xp desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("line 188", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("El circulo 1388")