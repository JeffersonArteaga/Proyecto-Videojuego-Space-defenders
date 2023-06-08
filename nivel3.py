import pygame
import time
import sys
import random
import os
from clases import asteroides, naves
from defs import get_time, cargarFondosEstaticos

# Inicializar Pygame
pygame.init()

def main():
    screen = pygame.display.set_mode((700, 700))  # Crear la ventana
    dir_fondo = "fondos/fondoNiveles/fondoNivel3.png"
    fondo = cargarFondosEstaticos(dir_fondo,700,700)
    nave = naves.Nave(350, 350, "imagenes/nave/FullHealth.png", 2)

    # Definir la fuente y el tamaño del texto
    font = pygame.font.SysFont('Bahnschrift', 40)
    font_time = pygame.font.SysFont('Bahnschrift', 35)

    pygame.mixer.music.load("sonidos/songNivel3.mp3")  # Cargar soundtrack del menú
    pygame.mixer.music.stop()
    pygame.mixer.music.play(-1)  # Reproducir la música en bucle

    # Definir el tiempo límite en segundos
    time_limit = 40
    start_time = time.time()

    paused = False
    time_paused = 0

    #Control de velocidad para la nave
    control_izquierda = 0
    control_derecha = 0
    control_arriba = 0
    control_abajo = 0

    #Control de generacion de asteroide
    control_asteroide = 0

    dirFondoPausa = "fondos/fondoPausa.jpg"
    dirFondoWin = "fondos/fondoVictoria.jpg"
    dirFondoLose = "fondos/fondoLose.jpg"
    fondoMenuPausa = cargarFondosEstaticos(dirFondoPausa,506,305)
    fondoWin = cargarFondosEstaticos(dirFondoWin,506,305)
    fondoLose = cargarFondosEstaticos(dirFondoLose,506,305)
    menuPausa = pygame.Rect(95,200,506,305)
    menuWin = pygame.Rect(95,200,506,305)
    menuLose = pygame.Rect(95,200,506,305)

    select = pygame.mixer.Sound("sonidos/select.mp3")   # Cargar sonido de clic
    select_sound = False

    sonidoWin = pygame.mixer.Sound("sonidos/sonidoVictoria.mp3")
    sonidoWinPlay = False

    sondioExplosion = pygame.mixer.Sound("sonidos/sonidoExplosion.mp3")
    sonidoLose = pygame.mixer.Sound("sonidos/sonidoLose.mp3")
    select_lose = False

    # Grupo de sprites para los asteroides
    grupo_asteroides = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if paused:
                        time_paused += time.time() - unpause_time
                        pygame.mixer.music.unpause()  # Reanudar la música
                    else:
                        unpause_time = time.time()
                        pygame.mixer.music.pause()  # Pausar la música
                    paused = not paused
                elif event.key == pygame.K_w:
                    nave.disparar('arriba')
                elif event.key == pygame.K_s:
                    nave.disparar('abajo')
                elif event.key == pygame.K_a:
                    nave.disparar('izquierda')
                elif event.key == pygame.K_d:
                    nave.disparar('derecha')

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if paused and time_left > 0:
                    x, y = pygame.mouse.get_pos()
                    if 263 <= x <= 436 and 394 <= y <= 413:
                        if paused:
                            time_paused += time.time() - unpause_time
                            pygame.mixer.music.unpause()  # Reanudar la música
                        else:
                            unpause_time = time.time()
                            pygame.mixer.music.pause()  # Pausar la música
                        paused = not paused
                    elif 199 <= x <= 502 and 445 <= y <= 464:
                        pygame.quit()
                        os.system("py -m menu.py")
                        sys.exit()

                if time_left < 0 and nave.salud > 0:
                    x, y = pygame.mouse.get_pos()
                    if 301 <= x <= 396 and 392 <= y <= 411:
                        pygame.quit()
                        sys.exit()
                    elif 199 <= x <= 502 and 445 <= y <= 464:
                        pygame.quit()
                        os.system("py -m menu.py")
                        sys.exit()
                
                if time_left > 0 and nave.salud <= 0:
                    x, y = pygame.mouse.get_pos()
                    if 301 <= x <= 396 and 392 <= y <= 411:
                        pygame.quit()
                        sys.exit()
                    elif 199 <= x <= 502 and 445 <= y <= 464:
                        pygame.quit()
                        os.system("py -m menu.py")
                        sys.exit()

        if not paused:  #Si el nivel no esta pausado
            elapsed_time = int(time.time() - start_time - time_paused)
            time_left = time_limit - elapsed_time
            if time_left >= 0:  #Si el tiempo del nivel no se ha acabado
                if nave.salud > 0:  #Si el jugador todavia tiene vida
                    if nave.salud == 1 and not nave.sonidoWarning:
                        nave.sonido_warning.play(-1)
                        nave.sonidoWarning = True

                    if control_asteroide == 100:
                        tipo_asteroide = random.choice([1,2,3,4])
                        asteroide = asteroides.Asteroide(50, 100, 1,tipo_asteroide)  # Crear un asteroide con dimensiones 50x50 y velocidad 1
                        grupo_asteroides.append(asteroide)
                        control_asteroide = 0
                    control_asteroide += 1 

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            control_izquierda += 1
                            if control_izquierda == 5:
                                nave.move(-1,0)
                                control_izquierda = 0
                        elif event.key == pygame.K_RIGHT:
                            control_derecha += 1
                            if control_derecha == 5:
                                nave.move(1,0)
                                control_derecha = 0
                        elif event.key == pygame.K_UP:
                            control_arriba += 1
                            if control_arriba == 5:
                                nave.move(0,-1)
                                control_arriba = 0
                        elif event.key == pygame.K_DOWN:
                            control_abajo += 1
                            if control_abajo == 5:
                                nave.move(0,1)
                                control_abajo = 0
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or \
                                event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            nave.move(0, 0)
                    
                    screen.blit(fondo, (0, 0))
                    nave.draw(screen)
                    nave.actualizar()
                    
                    for proyectil in nave.listaProyectiles:
                        proyectil.actualizar()
                        proyectil.dibujar(screen)

                        # Verificar si el proyectil está fuera de la ventana
                        if proyectil.rect.bottom < 0 or proyectil.rect.top > 700 or \
                        proyectil.rect.right < 0 or proyectil.rect.left > 700:
                            nave.listaProyectiles.remove(proyectil)

                    for asteroide in grupo_asteroides:
                        asteroide.actualizar()
                        asteroide.dibujar(screen)
                        # Verificar si el asteroide está fuera de la ventana
                        if asteroide.rect.bottom < 0 or asteroide.rect.top > 700 or \
                        asteroide.rect.right < 0 or asteroide.rect.left > 700:
                            grupo_asteroides.remove(asteroide)
                        if asteroide.rect.colliderect(nave):
                            nave.dañar()
                            grupo_asteroides.remove(asteroide)

                    for proyectil in nave.listaProyectiles:
                        for asteroide in grupo_asteroides:
                            if proyectil.rect.colliderect(asteroide.rect):
                                sondioExplosion.play()
                                nave.listaProyectiles.remove(proyectil)
                                grupo_asteroides.remove(asteroide)
                    
                    time_text = get_time(time_left)
                    text_surface = font_time.render(time_text, True, (255, 255, 255))
                    screen.blit(text_surface, (620, 10))
                
                else:
                    time_left = 1
                    pygame.draw.rect(screen,(255,255,255),menuLose)
                    screen.blit(fondoLose,menuLose)
                    nave.sonido_warning.stop()
                    pygame.mixer.music.stop()
                    if not select_lose:
                        sonidoLose.play()
                        select_lose = True
                    x,y = pygame.mouse.get_pos()
                    if 301 <= x <= 396 and 392 <= y <= 411:
                        if not select_sound:
                            select.play()
                            select_sound = True
                        pygame.draw.rect(screen, (238, 37, 201), (406, 398, 25, 7)) 
                    elif 199 <= x <= 502 and 445 <= y <= 464:
                        if not select_sound:
                            select.play()
                            select_sound = True
                        pygame.draw.rect(screen, (238, 37, 201), (512, 448, 25, 7)) 
                    else:
                        select_sound = False
                    
            else:
                if nave.salud > 0:  #Si el tiempo del nivel se acabo y el jugador todavia tiene vida
                    nave.sonido_warning.stop()
                    pygame.mixer.music.set_volume(0.1)
                    x, y = pygame.mouse.get_pos()
                    pygame.draw.rect(screen,(255,255,255),menuWin)
                    screen.blit(fondoWin,menuWin)
                    if 301 <= x <= 396 and 392 <= y <= 411:
                        if not select_sound:
                            select.play()
                            select_sound = True
                        pygame.draw.rect(screen, (238, 37, 201), (406, 398, 25, 7)) 
                    elif 199 <= x <= 502 and 445 <= y <= 464:
                        if not select_sound:
                            select.play()
                            select_sound = True
                        pygame.draw.rect(screen, (238, 37, 201), (512, 448, 25, 7)) 
                    else:
                        select_sound = False
                    if not sonidoWinPlay:
                        sonidoWin.play()
                        sonidoWinPlay = True

        if paused and time_left > 0:    #Si se presiona el boton de pausa y el jugador todavia tiene vida
            pygame.draw.rect(screen,(255,255,255),menuPausa)
            screen.blit(fondoMenuPausa,menuPausa)
            if nave.sonidoWarning:
                nave.sonido_warning.stop()
                nave.sonidoWarning = False

            x, y = pygame.mouse.get_pos()
            if 263 <= x <= 436 and 394 <= y <= 413:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (446, 403, 25, 7)) 
            elif 199 <= x <= 502 and 445 <= y <= 464:
                if not select_sound:
                    select.play()
                    select_sound = True
                pygame.draw.rect(screen, (238, 37, 201), (512, 454, 25, 7)) 
            else:
                select_sound = False

        print(time_left)
        pygame.display.flip()

main()