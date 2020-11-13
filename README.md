# Rekognition: It's Monday, but keep smiling.

Este programa creado en Python realiza la comparación de texto en dos imágenes subidas por el usuario: una imagen de control (la que determinará que texto identificar) y la imagen de prueba (imagen que se utilizará para ver si contiene el texto de la imagen de control). Entrega como respuesta True si el texto de la imagen de prueba se encuentra en la imagen de control y False en caso contrario.

## Instalación

Para ejecutar este programa es necesario tener una versión de **Python 3.7** o mayor. Además, se debe contar con una cuenta que permita el uso de [Amazon S3](https://aws.amazon.com/es/s3/) y tener actualizadas las credenciales (referirse a [este](https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-chap-install.html) artículo).

Por otra parte se debe instalar `boto3` para poder utilizar los servicios que el programa requiere de Amazon. Para esto se debe utilizar [pip](https://pip.pypa.io/en/stable/).

`pip install boto3`

## Modo de uso

El programa se debe ejecutar por consola sin introducir ningún parámetro en específico.

`python3 rekognition.py`

Tras ejecutar este comando el programa solicitará el nombre del bucket donde se encuentra la Imagen de prueba, el nombre de esta y la confianza en la detección de palabras.

```
Nombre del bucket S3:
Nombre del imagen de control:
Nombre del imagen de prueba:
Porcentaje de confianza:
```

Se debe introducir el nombre de la imagen junto a su formato.

**Nota:** el porcentaje de confianza se introduce de la manera (por ejemplo) 97 y no 0.97.

## Limitaciones

El programa presenta las siguientes limitaciones:

- No puede cargar más de 50 palabras.
- Las mayúsculas y minúsculas se tratan indistintamente (es decir, una N es lo mismo que una n para el programa).
- La imagen no puede estar rotada en un ángulo mayor a los 90° (en ambos sentidos).
- El programa solo puede procesar imágenes en formato .jpg, .jpeg y .png.
- Se eliminan los caracteres especiales, así como las tildes (para efectos de comparación una *a* es lo mismo que una *á*)
