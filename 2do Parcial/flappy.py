import pygame, sys, random

pygame.init()
pygame.mixer.init()

# Configuración del reloj para velocidad del juego y dimensiones pantalla
clock = pygame.time.Clock()
ancho_pantalla = 700
alto_pantalla = 750

# Creación de la ventana del juego
pygame.display.set_caption('Flappy bird')
ventana = pygame.display.set_mode((ancho_pantalla,alto_pantalla))

# Variables de desplazamiento y estado del juego
suelo_desplazamiento = 0
velocidad_desplazamiento = 3
espacio_vertical_tubo = 70
frecuencia_tubo = 2000 #milisegundos
score = 0
high_score = 0
volando = False
game_over = False
tubo_pasado = False
ultimo_tubo = pygame.time.get_ticks()

# Carga de imágenes y sonidos
fondo = pygame.image.load("C:/Users/garci/OneDrive/Imágenes/bg.png")
suelo = pygame.image.load("C:/Users/garci/OneDrive/Imágenes/ground.png")
bird = [pygame.image.load(f"C:/Users/garci/OneDrive/Imágenes/bird{num+1}.png") for num in range(3)]
boton_imag = pygame.image.load("C:/Users/garci/OneDrive/Imágenes/restart.png")
bird_jump = pygame.mixer.Sound("C:/Users/garci/Downloads/sfx_wing.mp3")
bird_pipe = pygame.mixer.Sound("C:/Users/garci/Downloads/sfx_point.mp3")
bird_b = pygame.mixer.Sound("C:/Users/garci/Downloads/sfx_die.mp3")


def texto(score):
    fuente = pygame.font.Font(None, 36)
    return fuente.render(f"Score: {score}", True, (255, 255, 255))

def texto1(high_score):
    fuente = pygame.font.Font(None, 36)
    return fuente.render(f"High Score: {high_score}", True, (255, 255, 255))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = alto_pantalla // 2
    score = 0
    return score

# Definición de la clase Bird para el sprite del pájaro
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.indice_imagen = 0
        self.contador_animacion = 0
        self.image = bird[self.indice_imagen]
        self.gravedad_velocidad = 0
        self.rect = self.image.get_rect(center=(x,y))

    def update(self):
        if volando == True:
            self.gravedad_velocidad += 0.5
            if self.gravedad_velocidad > 7:
                self.gravedad_velocidad = 7
            if self.rect.bottom < 600:
                self.rect.y += self.gravedad_velocidad

        if game_over == False:
            if pygame.mouse.get_pressed()[0] == True:
                self.gravedad_velocidad = -5
                bird_jump.play()

            # Manejo de la animación del pájaro
            self.contador_animacion += 1
            flap_cooldown = 5

            if self.contador_animacion > flap_cooldown:
                self.contador_animacion = 0
                self.indice_imagen += 1
                if self.indice_imagen >= len(bird):
                    self.indice_imagen = 0

            self.image = bird[self.indice_imagen]
            self.image = pygame.transform.rotate(bird[self.indice_imagen], self.gravedad_velocidad * -2)

        else:
            self.image = pygame.transform.rotate(bird[self.indice_imagen], -90)


class Tubo(pygame.sprite.Sprite):
    def __init__(self, x, y, posicion):
        super().__init__()
        self.image = pygame.image.load("C:/Users/garci/OneDrive/Imágenes/pipe.png")
        self.rect = self.image.get_rect()
        #posicion 1 es desde arriba, x es desde abajo
        if posicion == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomright = (x, y - espacio_vertical_tubo)
        else:
            self.rect.topright = (x, y + espacio_vertical_tubo)

    def update(self):
        self.rect.x -= velocidad_desplazamiento
        if self.rect.right < 0:
            self.kill()


class Boton():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def dibujo(self):
        accion = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[2] == True:
                accion = True
                bird_b.play()

        ventana.blit(self.image, (self.rect.x, self.rect.y))

        return accion


# Creación del grupo de sprites del pájaro y adición del sprite creado anteriormente
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(100, alto_pantalla // 2)
bird_group.add(flappy)
boton = Boton(298,50,boton_imag)

# Bucle principal del juego
run = True
while run:

    # Configuración de la velocidad del juego
    clock.tick(60)

    # Dibujado del fondo del juego
    ventana.blit(fondo, (0, 0))

    # Dibujado y actualización del sprite del pájaro
    bird_group.draw(ventana)
    bird_group.update()
    pipe_group.draw(ventana)

    # Dibujado y desplazamiento del suelo del juego
    ventana.blit(suelo, (suelo_desplazamiento, 600))
    ventana.blit(texto(score), (80, 60))
    ventana.blit(texto1(high_score),(500,60))

    #checar el score
    if len(pipe_group) > 0 and game_over == False:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right:
            bird_pipe.play()
            tubo_pasado = True
        if tubo_pasado == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                if score >= high_score:
                    high_score = score
                tubo_pasado = False

    #Colisión
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0 or flappy.rect.bottom > 598:
        game_over = True
        if boton.dibujo() == True:
            game_over = False
            volando = False
            score = reset_game()


    if game_over == False and volando == True:
        #generando los tubos
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_tubo > frecuencia_tubo:
            pipe_height = random.randint(-100, 100)
            tubo1 = Tubo(ancho_pantalla, alto_pantalla // 2 + pipe_height, -1)
            tubo2 = Tubo(ancho_pantalla, alto_pantalla // 2 + pipe_height, 1)
            pipe_group.add(tubo1)
            pipe_group.add(tubo2)
            ultimo_tubo = tiempo_actual
                            
        suelo_desplazamiento -= velocidad_desplazamiento 
        if abs(suelo_desplazamiento) > 35:
            suelo_desplazamiento = 0

        pipe_group.update()


    # Monitoreo de eventos del usuario
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and volando == False and game_over == False:
            volando = True

    # Actualización de la pantalla
    pygame.display.update()