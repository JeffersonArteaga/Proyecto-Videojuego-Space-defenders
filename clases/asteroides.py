import pygame
import random

#Nombre de la subrutina: Asteroide
#Tipo: Clase (se utiliza para crear objetos de tipo Asteroide)
#Objetivo: Representar un asteroide en un juego utilizando el módulo pygame
#Parámetros:
#width (entero): Ancho del asteroide en píxeles.
#height (entero): Altura del asteroide en píxeles.
#velocidad (entero): Velocidad de movimiento del asteroide.
#tipo (entero): Tipo de asteroide (1, 2, 3 o 4) que afecta su posición inicial y rotación.
#Retorno: Ninguno.
#Ejemplo de uso:
#asteroide = Asteroide(50, 50, 2, 1)
#asteroide.actualizar()
#asteroide.dibujar(screen)
#Notas:
#Esta clase representa un asteroide en un juego utilizando la biblioteca pygame.
#El asteroide se carga desde una imagen y se escala al tamaño especificado.
#El asteroide puede tener cuatro tipos diferentes, cada uno con una posición y rotación inicial específica.
#La función actualizar() se utiliza para actualizar la posición del asteroide en función de su velocidad.
#La función dibujar() se utiliza para dibujar el asteroide en una superficie de destino utilizando la imagen cargada.
class Asteroide(pygame.sprite.Sprite):
    def __init__(self, width, height, velocidad, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.tipo = tipo
        self.imagenAsteroide = pygame.image.load("imagenes/asteroide.png")
        self.imagenAsteroide = pygame.transform.scale(self.imagenAsteroide, (width, height))
        self.rect = self.imagenAsteroide.get_rect()
        if self.tipo == 1:
            self.imagenAsteroide = pygame.transform.rotate(self.imagenAsteroide,180)
            self.rect.x = random.randint(0, 700 - width)  # Generar posición aleatoria en el eje x
            self.rect.y = 0  # Posición inicial en el eje y
            self.velocidad_Y = velocidad
            self.velocidad_X = 0
        if self.tipo == 2:
            self.imagenAsteroide = pygame.transform.rotate(self.imagenAsteroide,0)
            self.rect.x = random.randint(0, 700 - width)  # Generar posición aleatoria en el eje x
            self.rect.y = 650  # Posición inicial en el eje y
            self.velocidad_Y = velocidad * -1
            self.velocidad_X = 0
        if self.tipo == 3:
            self.imagenAsteroide = pygame.transform.rotate(self.imagenAsteroide,270)
            self.rect.y = random.randint(0, 700 - width)  # Generar posición aleatoria en el eje x
            self.rect.x = 0  # Posición inicial en el eje y
            self.velocidad_Y = 0
            self.velocidad_X = velocidad
        if self.tipo == 4:
            self.imagenAsteroide = pygame.transform.rotate(self.imagenAsteroide,90)
            self.rect.y = random.randint(0, 700 - width)  # Generar posición aleatoria en el eje x
            self.rect.x = 650  # Posición inicial en el eje y
            self.velocidad_Y = 0
            self.velocidad_X = velocidad * -1
        
    
    def actualizar(self):
        self.rect.y += self.velocidad_Y  # Mover el asteroide en dirección hacia abajo
        self.rect.x += self.velocidad_X

    
    def dibujar(self, superficie):
        superficie.blit(self.imagenAsteroide, self.rect)