import cv2
import numpy as np


load_image = (lambda filename: cv2.imread(filename))(input("Digite o nome do arquivo de imagem: "))


brilho = float(input("Digite o fator de ajuste de brilho (por exemplo, 1.5 para aumentar o brilho): "))
ajustar_brilho = (lambda img, factor: cv2.convertScaleAbs(img, alpha=factor, beta=0))(load_image, brilho)


cv2.imshow("Imagem Original", load_image)


cv2.imshow("Imagem com Brilho Ajustado", ajustar_brilho)


cv2.waitKey(0)
cv2.destroyAllWindows()
