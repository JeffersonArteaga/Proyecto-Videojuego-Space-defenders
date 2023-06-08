import pygame


#Nombre de la subrutina: Proyectil
#Tipo: Clase (se utiliza para crear objetos de tipo Proyectil)
#Objetivo: Representar un proyectil en un juego utilizando el módulo pygame
#Parámetros:
#x (entero): Posición inicial en el eje x del proyectil.
#y (entero): Posición inicial en el eje y del proyectil.
#grados (entero): Ángulo de rotación del proyectil.
#Retorno: Ninguno.
#Ejemplo de uso:
#proyectil = Proyectil(100, 200, 45)
#proyectil.actualizar()
#proyectil.dibujar(superficie)
#Notas:
#Esta clase representa un proyectil en un juego utilizando la biblioteca pygame.
#La imagen del proyectil se carga desde el archivo "imagenes/misil1.png" y se redimensiona a un tamaño de 20x20 píxeles.
#La imagen del proyectil se rota según el ángulo especificado por grados.
#La posición inicial del proyectil se establece en las coordenadas (x, y).
#El proyectil tiene velocidades de movimiento en los ejes x e y.
#La función actualizar() se utiliza para actualizar la posición del proyectil en cada iteración del juego.
#La función dibujar() se utiliza para dibujar el proyectil en una superficie especificada.
class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y,grados):
        pygame.sprite.Sprite.__init__(self)
        self.imagenProyectil = pygame.image.load("imagenes/misil1.png")
        # Redimensionar la imagen del proyectil
        self.imagenProyectil = pygame.transform.scale(self.imagenProyectil, (20, 20))
        self.imagenProyectil = pygame.transform.rotate(self.imagenProyectil,grados)
        self.rect = self.imagenProyectil.get_rect()
        self.velocidad_Y = 1
        self.velocidad_X = 1
        self.rect.centerx = x
        self.rect.centery = y

    def actualizar(self):
        self.rect.y -= self.velocidad_Y
        self.rect.x += self.velocidad_X  # Para mover hacia la derecha

    def dibujar(self, superficie):
        superficie.blit(self.imagenProyectil, self.rect)