import cv2
import numpy as np
import requests
from io import BytesIO
from PIL import Image

# URL de la imagen original
url = "URL_DE_LA_IMAGEN"
response = requests.get(url)
image_data = np.frombuffer(response.content, dtype=np.uint8)
original_image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

# URL de la imagen del código y la bandera de Perú
codigo_url = "URL_DEL_CODIGO"
codigo_response = requests.get(codigo_url)
codigo_image = Image.open(BytesIO(codigo_response.content))
codigo_image = np.array(codigo_image)

bandera_url = "URL_DE_LA_BANDERA_DE_PERU"
bandera_response = requests.get(bandera_url)
bandera_image = Image.open(BytesIO(bandera_response.content))
bandera_image = np.array(bandera_image)

# Definir la posición del hombro (puedes ajustar estas coordenadas según tu imagen)
hombro_y, hombro_x = 100, 200

# Pegar el código en el hombro
codigo_height, codigo_width, _ = codigo_image.shape
original_image[hombro_y:hombro_y + codigo_height, hombro_x:hombro_x + codigo_width] = codigo_image

# Pegar la bandera de Perú en el hombro
bandera_height, bandera_width, _ = bandera_image.shape
original_image[hombro_y:hombro_y + bandera_height, hombro_x:hombro_x + bandera_width] = bandera_image

# Mostrar la imagen modificada
cv2.imshow("Imagen modificada", original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
