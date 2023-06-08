import pygame
from clases import proyectiles

#Nombre de la subrutina: Nave
#Tipo: Clase (se utiliza para crear objetos de tipo Nave)
#Objetivo: Representar una nave en un juego utilizando el módulo pygame
#Parámetros:
#x (entero): Posición inicial en el eje x de la nave.
#y (entero): Posición inicial en el eje y de la nave.
#image_path (cadena de caracteres): Ruta de la imagen de la nave.
#scale (float): Escala de la imagen de la nave.
#Retorno: Ninguno.
#Ejemplo de uso:
#nave = Nave(100, 200, "imagenes/nave.png", 0.5)
#nave.move(1, 0)
#nave.disparar('arriba')
#nave.actualizar()
#nave.dañar()
#Notas:
#Esta clase representa una nave en un juego utilizando la biblioteca pygame.
#La imagen de la nave se carga desde el archivo especificado y se escala al tamaño especificado por scale.
#La posición inicial de la nave se establece en las coordenadas (x, y).
#La nave tiene una velocidad de movimiento, una lista de proyectiles y una variable de control para disparar misiles.
#La función draw() se utiliza para dibujar la nave en una superficie especificada.
#La función move() se utiliza para mover la nave en las direcciones especificadas por los parámetros dx y dy.
#La función disparar() se utiliza para disparar un proyectil en la dirección especificada.
#La función actualizar() se utiliza para realizar actualizaciones después de un disparo de misil.
#La función dañar() se utiliza para reducir la salud de la nave y actualizar su imagen según el nivel de daño.
class Nave:
    def __init__(self, x, y, image_path, scale):
        self.scale = scale
        self.original_image = pygame.image.load(image_path)
        self.original_rect = self.original_image.get_rect()
        self.damaged = pygame.image.load("imagenes/nave/Damaged.png")
        self.slightDamaged = pygame.image.load("imagenes/nave/SlightDamage.png")
        self.veryDamaged = pygame.image.load("imagenes/nave/VeryDamaged.png")
        self.image = pygame.transform.scale(self.original_image, (int(self.original_rect.width * self.scale),
                                                                  int(self.original_rect.height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 1  # Velocidad de movimiento
        self.listaProyectiles = []
        self.misil_disparado = False  # Variable de control de disparo de misil
        self.sonido_disparo = pygame.mixer.Sound("sonidos/sonidoDisparo.mp3")  # Cargar el sonido de disparo
        self.sonido_daño = pygame.mixer.Sound("sonidos/sonidoDaño.mp3")
        self.sonido_warning = pygame.mixer.Sound("sonidos/sonidoWarning.mp3")
        self.sonidoWarning = False
        self.salud = 4

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, dx, dy):
        next_x = self.rect.x + dx * self.velocity
        next_y = self.rect.y + dy * self.velocity
        
        if dx > 0:
            next_x = min(next_x, 700 - self.rect.width)
        elif dx < 0:
            next_x = max(next_x, 0)
        
        if dy > 0:
            next_y = min(next_y, 700 - self.rect.height)
        elif dy < 0:
            next_y = max(next_y, 15)
        
        self.rect.x = next_x
        self.rect.y = next_y

    def disparar(self,direccion):
        if not self.misil_disparado:  # Verificar si no se ha disparado un misil recientemente
            if direccion == 'arriba':
                proyectil = proyectiles.Proyectil(self.rect.centerx, self.rect.centery,0)
                proyectil.velocidad_X = 0
                self.listaProyectiles.append(proyectil)
            elif direccion == 'abajo':
                proyectil = proyectiles.Proyectil(self.rect.centerx, self.rect.centery,180)
                proyectil.velocidad_Y *= -1  # Invertir la velocidad para mover el misil hacia abajo
                proyectil.velocidad_X = 0
                self.listaProyectiles.append(proyectil)
            elif direccion == 'izquierda':
                proyectil = proyectiles.Proyectil(self.rect.centerx, self.rect.centery,90)
                proyectil.velocidad_X = -1  # Establecer la velocidad en cero para mover el misil solo en el eje X
                proyectil.velocidad_Y = 0
                self.listaProyectiles.append(proyectil)
            elif direccion == 'derecha':
                proyectil = proyectiles.Proyectil(self.rect.centerx, self.rect.centery,270)
                proyectil.velocidad_Y = 0  # Invertir la velocidad para mover el misil hacia abajo
                proyectil.velocidad_X = 1  # Establecer la velocidad en cero para mover el misil solo en el eje X
                self.listaProyectiles.append(proyectil)
            # Reproducir el sonido de disparo
            pygame.mixer.Sound.play(self.sonido_disparo)
            self.misil_disparado = True  # Establecer la variable de control como True

    def actualizar(self):
        # Restablecer la variable de control de disparo de misil después de un tiempo
        if self.misil_disparado:
            self.misil_disparado = False

    def dañar(self):
        self.sonido_daño.play()
        self.salud -= 1
        if self.salud == 3:
            self.image = pygame.transform.scale(self.slightDamaged, (int(self.original_rect.width * self.scale),
                                                                  int(self.original_rect.height * self.scale)))
        elif self.salud == 2:
            self.image = pygame.transform.scale(self.damaged, (int(self.original_rect.width * self.scale),
                                                                  int(self.original_rect.height * self.scale)))
        elif self.salud == 1:
            self.image = pygame.transform.scale(self.veryDamaged, (int(self.original_rect.width * self.scale),
                                                                  int(self.original_rect.height * self.scale)))
            self.sonido_warning.set_volume(1)
            self.sonido_warning.play(-1)
            self.sonidoWarning = True