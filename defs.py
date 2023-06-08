import pygame
import os
#Nombre subrutina: cargarFondosEstaticos
#Tipo: Función
#Objetivo: Cargar una imagen de fondo estática desde un archivo y escalarla a un tamaño HD (1280x720).
#Parámetros:
#dir_file: Ruta del archivo que contiene la imagen de fondo estática.
#Retorno:
#Imagen de fondo cargada y escalada.
#Ejemplo de uso:
#archivo_fondo = "ruta/al/archivo/fondo.jpg"
#fondo_estatico = cargarFondosEstaticos(archivo_fondo)
def cargarFondosEstaticos(dir_file,height,width):
    background = pygame.image.load(dir_file).convert()
    background = pygame.transform.scale(background, (height, width))    # Cargar imágenes de fondo y escalarlas a tamaño HD
    return background

#Nombre subrutina: cargarFondosAnimados
#Tipo: Función
#Objetivo: Cargar una secuencia de imágenes de fondo desde una carpeta y escalarlas a un tamaño HD (1280x720).
#Parámetros:
#background_folder: Ruta de la carpeta que contiene las imágenes de fondo.
#Retorno:
#Lista de imágenes de fondo escaladas.
#Ejemplo de uso:
#carpeta_fondos = "ruta/a/la/carpeta/fondos"
#fondos_animados = cargarFondosAnimados(carpeta_fondos)
def cargarFondosAnimados(background_folder):
    background_frames = []
    for file_name in sorted(os.listdir(background_folder)):
        if file_name.endswith(".jpg"):
            file_path = os.path.join(background_folder, file_name)
            image = pygame.image.load(file_path)
            image = pygame.transform.scale(image, (1280, 720))  # Cargar imágenes de fondo y escalarlas a tamaño HD
            background_frames.append(image)
    return background_frames

#Nombre subrutina: cargarFondos
#Tipo: Función
#Objetivo: Cargar diferentes fondos utilizados en el juego, tanto animados como estáticos.
#Parámetros: No se requieren parámetros explícitos.
#Retorno:
#Diccionario que contiene los fondos cargados, con claves correspondientes a cada tipo de fondo.
#Ejemplo de uso:
#fondos_cargados = cargarFondos()
def cargarFondos():
    menu_folder = "fondos/fondoMenu"
    opening_folder = "fondos/fondoOpening"
    creditos_file = "fondos/fondoCreditos.jpg"
    tuto1_file = "fondos/fondoTuto1.jpg"
    tuto2_file = "fondos/fondoTuto2.jpg"
    menu_frames = cargarFondosAnimados(menu_folder)
    opening_frames = cargarFondosAnimados(opening_folder)
    fondoCreditos = cargarFondosEstaticos(creditos_file,1280,720)
    fondoTuto1 = cargarFondosEstaticos(tuto1_file,1280,720)
    fondoTuto2 = cargarFondosEstaticos(tuto2_file,1280,720)
    fondos = {'menu_frames':menu_frames, 'opening_frames': opening_frames, 'fondoCreditos': fondoCreditos, 'fondoTuto1': fondoTuto1, 'fondoTuto2': fondoTuto2}
    return fondos

#nombre subrutina: get_time
#tipo: Función
#Objetivo: Convertir una cantidad de segundos en formato de tiempo en minutos y segundos.
#Parámetros:
#seconds: Entero que representa la cantidad de segundos.
#Retorno:
#Una cadena de caracteres que representa el tiempo en formato "mm:ss", donde "mm" son los minutos y "ss" son los segundos.
#Ejemplo de uso:
#tiempo = get_time(125)
#print(tiempo)  # Salida: "02:05"
#Notas:
#La función asume que el parámetro "seconds" es un entero no negativo.
#Si la cantidad de segundos es mayor a 59, se calculará la cantidad de minutos y el resto de segundos restantes.
#El formato de salida asegura que los minutos y los segundos sean representados con dos dígitos, agregando un cero al principio si es necesario.
def get_time(seconds):
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes:02d}:{seconds:02d}"