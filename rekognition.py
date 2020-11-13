# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 10:59:38 2020

@author: baca2
"""
#Librerías para este programa
import boto3
import re
from datetime import datetime

#Función para detectar palabras coincidentes entre imagen de control e imagen de prueba
def detect_text(photo, bucket, confidence, photo_control):
    
    f = open("logs.txt", "a")
    f.write('Fecha de prueba:' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')
    f.write('Intervalo de confianza establecido: ' + str(confidence) + '\n')
    f.write("Palabras en imagen de control: \n")
    f.write("[")
    #Cargar palabras en imagen de control
    client_control = boto3.client('rekognition')

    response_control=client_control.detect_text(Image={'S3Object':{
                                            'Bucket': bucket,
                                            'Name':photo_control}
                                        },
                                Filters={'WordFilter':{
                                            'MinConfidence': confidence}})
    
    textDetections_control=response_control['TextDetections']
    
    #Cargar una lista con las palabras en imagen de control
    lista_control = []
    
    #Se guardan las palabras en la lista, pero se normalizan a minúsculas, se eliminan espacios y textos especiales
    for text in textDetections_control:
        #La idea es identificar palabras, pero rekognition a veces deja palabras juntas, creando una frase
        #y separadas por un espacio. Aquí se separan estas palabras (si corresponde) y se testean de manera
        #independiente
            x = text['DetectedText'].split()
            for i in x:
                standarized = re.sub(r'[^(á-ú)*\w*@*]','',i).lower()
                if standarized not in lista_control:
                    lista_control.append(standarized)
                    f.write(standarized + ", ")
            
    f.write("] \n")
    f.write("Palabras en " + photo + ": \n")
    f.write("[")
    #Cargar palabras en imagen de prueba
    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{
                                            'Bucket':bucket,
                                            'Name':photo}
                                        },
                                Filters={'WordFilter':{
                                            'MinConfidence': confidence}})
                        
    textDetections=response['TextDetections']
    
    #Se verifica si las palabras en imagen de control están en imagen de prueba
    lista_prueba = []
    
    #Se chequea si la palabra ha sido testeada, si no es así se guarda en la lista
    #de palabras testeadas y se transforma a minúscula para ver si se encuentra en
    #la lista de palabras de la imagen de control.
    flag = 0
    for text in textDetections:
            x = text['DetectedText'].split()
            for i in x:
                texto = re.sub(r'[^(á-ú)*\w*@*]','',i).lower()
                if texto not in lista_prueba:
                    lista_prueba.append(texto)
                    f.write(texto + ', ')
                
    f.write("] \n")
    for word in lista_control:
        if word not in lista_prueba:
            flag = 1
            break
        
    if flag == 0:
        print("Resultado: true")
        f.write("Resultado: true \n")
    else:
        print("Resultado: false")
        f.write("Resultado: false \n")
    f.write('\n')
    f.close()
def main():
    
    bucket = input('Nombre del bucket S3: ')
    photo_control = input('Nombre de imagen de control: ')
    photo = input('Nombre de imagen de prueba: ')
    confidence = float(input('Porcentaje de confianza: '))
    
    print()
    detect_text(photo,bucket, confidence, photo_control)
    #print("Algo ocurrió. Por favor, revise los datos ingresados y verifique que sean válidos. Considere que el archivo debe estar en formato .jpg, .jpeg o .png.")

if __name__ == "__main__":
    main()