import pygame, sys
pygame.init()

#definir colores:

black = (0  ,  0,  0)
white = (255,255,255)
green = (0  ,255,  0)
red   = (255,  0,  0)
blue  = (  0,  0,255)
palo_rosa = (255,227,232)


size = (800, 500) #tupla

#crear ventana
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get(): #esto es para poder cerrar el juego
        if event.type == pygame.QUIT:
            sys.exit()

    #color de fondo
    screen.fill(palo_rosa)
    #-----zona de dibujo 
    pygame.draw.line(screen, red, [0,100], [200,300], 5)





    #-----zona de dibujo 
    #actualizar pantalla
    pygame.display.flip()
