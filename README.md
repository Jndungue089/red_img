# Redimensionalidade de Features em Machine Learning

## 📌 Introdução
Este projeto demonstra um processo fundamental no **pré-processamento de dados** para Machine Learning: a **transformação e binarização de imagens**, o que pode ser visto como um exemplo de **redução de dimensionalidade**. A transformação de imagens coloridas em tons de cinza e posteriormente em binárias reduz a quantidade de informações presentes, simplificando os dados para facilitar sua análise e processamento.

## 📂 Descrição do Programa
Este programa em Python realiza as seguintes etapas:
1. **Carregamento da imagem**: Utiliza a biblioteca OpenCV para abrir uma imagem colorida.
2. **Conversão para escala de cinza**: Reduz as três dimensões do espaço de cores (RGB) para uma única dimensão (tons de cinza).
3. **Binarização**: Transforma a imagem em apenas dois valores (0 e 255), reduzindo ainda mais a complexidade da informação.
4. **Exibição dos resultados**: Mostra a imagem original, a versão em escala de cinza e a binária usando Matplotlib.

## 🛠 Bibliotecas Necessárias
Para executar o código, é necessário instalar as seguintes bibliotecas:

```bash
pip install opencv-python numpy matplotlib
```

## 🚀 Como Executar o Programa
1. Certifique-se de ter Python instalado.
2. Instale as bibliotecas mencionadas acima.
3. Execute o seguinte código em um ambiente Python:

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image_path = "caminho/para/imagem.png"
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
```

## 🎯 Aplicação em Machine Learning
A transformação de imagens coloridas para escala de cinza ou binária é um exemplo de **redução de dimensionalidade**, um conceito chave em Machine Learning. Essa técnica é útil para:
- **Pré-processamento de dados**: Simplificar os dados antes de alimentar um modelo.
- **Redução de ruído**: Eliminar informações desnecessárias para melhorar a performance do algoritmo.
- **Otimização de tempo de treinamento**: Modelos trabalham mais rapidamente com menos dimensões.

📌 **Exemplo prático**: Em visão computacional, redes neurais convolucionais (CNNs) muitas vezes utilizam imagens em tons de cinza para reduzir a complexidade dos cálculos.

## 📚 Conclusão
Este programa demonstra um conceito fundamental para Machine Learning: **a redução da dimensionalidade**. Aplicações dessa técnica podem ser vistas em diversas áreas como reconhecimento de imagens, processamento de sinais e análise de dados.

Sinta-se à vontade para modificar e aprimorar o código! 🚀

