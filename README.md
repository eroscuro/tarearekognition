# Rekognition: It's Monday, but keep smiling.

Este programa detecta las palabras de una imagen cargada por el usuario (esta imagen será llamada la Imagen de prueba) y detecta las palabras que se encuentran en esta. Tras la detección lleva a cabo una comparación con las palabras en [esta imagen](https://docs.aws.amazon.com/es_es/rekognition/latest/dg/images/text.png) (la llamaremos Imagen de control) y da aviso de si las palabras en la Imagen de prueba se encuentran en la Imagen de control.

## Instalación

Para ejecutar este programa es necesario tener una versión de **Python 3.7** o mayor. Además, se debe contar con una cuenta que permita el uso de [Amazon S3](https://aws.amazon.com/es/s3/) y tener actualizadas las credenciales.

Por otra parte se debe instalar `boto3` para poder utilizar los servicios que el programa requiere de Amazon. Para esto se debe utilizar [pip](https://pip.pypa.io/en/stable/).

`pip install boto3`

## Modo de uso

El programa se debe ejecutar por consola sin introducir ningún parámetro en específico.

`python3 prueba2.py`

Tras ejecutar este comando el programa solicitará el nombre del bucket donde se encuentra la Imagen de prueba, el nombre de esta y la confianza en la detección de palabras.

```
Nombre del bucket S3:
Nombre del archivo a cargar:
Porcentaje de confianza:
```

Se debe introducir el nombre de la imagen junto a su formato.

## Limitaciones

El programa presenta las siguientes limitaciones:

- No puede cargar más de 50 palabras.
- Las mayúsculas y minúsculas se tratan indistintamente (es decir, una N es lo mismo que una n para el programa).
- La imagen no puede estar rotada en un ángulo mayor a los 90° (en ambos sentidos).
- El programa solo puede procesar imágenes en formato .jpg, .jpeg y .png.
- Se eliminan los caracteres especiales, así como las tildes (para efectos de comparación una *a* es lo mismo que una *á*)
