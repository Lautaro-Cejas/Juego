import pygame
import random
import sys

pygame.init()

# Constantes
ancho = 800
alto = 600

# Tipografia
fuente = pygame.font.SysFont('coolveticargregular', 45, True)

# Audio
st = pygame.mixer.Sound('audio/ambientemenu.mp3')
st.set_volume(0.15)
musica = pygame.mixer.Sound('audio/slime.mp3')
musica.set_volume(0.2)

# Jugador
size_jugador = 50
posicion_jugador = [ancho / 2, alto - size_jugador * 2]

# Enemigo(s)
size_enemigo = 50
posicion_enemigo = [random.randint(0, ancho - size_enemigo), 0]

# Ventanas
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("CO-VIDEOGAME 21")
menubg = pygame.image.load("img/hospital.png").convert_alpha()
bg = pygame.image.load("img/escenario.png").convert_alpha()

# Tiempo

clock = pygame.time.Clock()       


# Funciones

def menu():
    # Estados de juego

    inicio = True
    corriendo = False

    while inicio:
        ventana.blit(menubg, [0, 0])
        st.play(-1)
        instruccion = fuente.render("Presione Enter para jugar",1 ,(0,0,0))
        ventana.blit(instruccion,(100, 520))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_RETURN]:
            inicio = False
            corriendo = True

        pygame.display.update()

    def detectar_colision(posicion_jugador, posicion_enemigo):
        jx = posicion_jugador[0]
        jy = posicion_jugador[1]
        ex = posicion_enemigo[0]
        ey = posicion_enemigo[1]

        if(ex >= jx and ex < (jx + size_jugador)) or (jx >= ex and jx < (ex + size_enemigo)):
            if(ey >= jy and ey < (jy + size_jugador)) or (jy >= ey and jy < (ey + size_enemigo)):
                return True
            return False

    while corriendo:
        st.stop()
        musica.play(-1)
        ventana.blit(bg, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                x = posicion_jugador[0]
                if event.key == pygame.K_LEFT:
                    x -= size_jugador
                if event.key == pygame.K_RIGHT:
                    x += size_jugador

                posicion_jugador[0] = x

        if posicion_enemigo[1] >= 0 and posicion_enemigo[1] < alto:
            posicion_enemigo[1] += 20
        else:
            posicion_enemigo[0] = random.randint(0, ancho - size_enemigo)
            posicion_enemigo[1] = 0

        # Colisiones
        if detectar_colision(posicion_jugador, posicion_enemigo):
            corriendo = False

        # Dibujar jugador
        jugador = pygame.image.load("img/doctor.png").convert_alpha()
        ventana.blit(jugador, (posicion_jugador))

        # Dibujar enemigo
        enemigo = pygame.image.load("img/virus.png").convert_alpha()
        ventana.blit(enemigo, (posicion_enemigo))

        clock.tick(60)
        pygame.display.update()

menu()