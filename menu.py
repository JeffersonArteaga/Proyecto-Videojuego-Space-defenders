# Proyecto Final Computacion Grafica Jefferson David Arteaga

import pygame
import os
import sys
from defs import cargarFondosEstaticos, cargarFondosAnimados, cargarFondos

# Inicializar Pygame
pygame.init()

def main():
    screen = pygame.display.set_mode((1280, 720))   # Configuración de la pantalla
    fondos = cargarFondos()
    clock = pygame.time.Clock() # Configurar el reloj
    FPS = 25
    pygame.mixer.music.load("sonidos/songMenu.mp3") # Cargar soundtrack del menu
    pygame.mixer.music.stop()
    select = pygame.mixer.Sound("sonidos/select.mp3")   # Cargar sonido de clic
    select_sound = False
    music_playing = False   # El soundtrack iniciara detenido
    current_frame = 0       # Indicara el frame de a mostrar para los fondos animados
    opening = True
    creditos = False
    menu = False
    tuto1 = False
    tuto2 = False
    while True:
        x, y = pygame.mouse.get_pos()
        if opening:
            screen.blit(fondos['opening_frames'][current_frame], (0, 0)) # Mostrar fondo animado de apertura
            current_frame += 1
            if current_frame == (len(fondos['opening_frames']) -1):
                opening = False
                menu = True
                current_frame = 0

        elif menu:
            screen.blit(fondos['menu_frames'][current_frame], (0, 0)) # Mostrar fondo animado del menú
            current_frame = (current_frame + 1) % len(fondos['menu_frames'])
            if 568 <= x <= 705 and 421 <= y <= 447:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (715, 432, 25, 7)) # Dibujar la línea rosada si el mouse está en el área de jugar
                    
            elif 568 <= x <= 705 and 471 <= y <= 497:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (715, 482, 25, 7)) # Dibujar la línea rosada si el mouse está en el área de ayuda

            elif 545 <= x <= 734 and 522 <= y <= 545:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (745, 533, 25, 7)) # Dibujar la línea rosada si el mouse está en el área de creditos

            elif 568 <= x <= 695 and 566 <= y <= 589:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (710, 577, 25, 7)) # Dibujar la línea rosada si el mouse está en el área de salir

            else:
                select_sound = False

        elif creditos:
            screen.blit(fondos['fondoCreditos'], (0, 0)) # Mostrar fondo estático de los créditos
            if 903 <= x <= 1110 and 87 <= y <= 119:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (903, 125, 207, 3))
            else:
                select_sound = False

        elif tuto1:
            screen.blit(fondos['fondoTuto1'], (0, 0)) # Mostrar fondo estático del tutorial 1
            if 868 <= x <= 1130 and 88 <= y <= 116:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (868, 122, 262, 3))

            elif 635 <= x <= 836 and 87 <= y <= 117:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (635, 120, 201, 3))
            else:
                select_sound = False

        elif tuto2:
            screen.blit(fondos['fondoTuto2'], (0, 0)) # Mostrar fondo estático del tutorial 2
            if 903 <= x <= 1110 and 87 <= y <= 119:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (903, 125, 207, 3))
            else:
                select_sound = False

        else:
            pass
        
        if not opening and not music_playing: # Reproducir la música en bucle
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)  # Reproducir la música en bucle
            music_playing = True
        
        pygame.display.flip() # Actualizar pantalla
        clock.tick(FPS) # Limitar FPS
        for event in pygame.event.get(): # Comprobar eventos de salida
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                if menu:
                    if 568 <= x <= 705 and 421 <= y <= 447:
                        pygame.quit()
                        os.system("python3 nivel1.py")
                        sys.exit()
                    if 545 <= x <= 734 and 522 <= y <= 545:
                        menu = False # Transición a la pantalla de créditos
                        creditos = True

                    if 568 <= x <= 705 and 471 <= y <= 497:
                        menu = False # Transición al tutorial 1
                        tuto1 = True

                    if 568 <= x <= 695 and 566 <= y <= 589:
                        pygame.quit() # Salir del juego
                        quit()
                    break

                if tuto1:
                    if 868 <= x <= 1130 and 88 <= y <= 116:                    
                        tuto1 = False # Transición al tutorial 2
                        tuto2 = True
                    elif 635 <= x <= 836 and 87 <= y <= 117:
                        tuto1 = False # Volver al menú desde el tutorial 1
                        menu = True
                    break
                if tuto2:
                    if 903 <= x <= 1110 and 87 <= y <= 119:
                        tuto1 = True # Volver al tutorial 1 desde el tutorial 2
                        tuto2 = False
                    break
                if creditos:
                    if 903 <= x <= 1110 and 87 <= y <= 119:
                        menu = True # Volver al menú desde los créditos
                        creditos = False
                    break

main()

            
            
                
                


