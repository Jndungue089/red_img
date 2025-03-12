import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image_path = "try.png"
image = cv2.imread(image_path)

# Converter para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar limiarização (binarização)
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Exibir as imagens
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Imagem em Cinza")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap="gray")
plt.title("Imagem Binária")
plt.axis("off")

plt.show()
