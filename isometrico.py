import pygame
import math
from lib import *

pygame.init()
Pantalla = pygame.display.set_mode([800, 650])
origen = [400, 450]  # --> punto de origen
n = 1  # valor de escalamiento, inicia en 1 para no alterar la figura
g = 0  # grados de rotacion,inicia en 0 para que no se altere la figura
v = 1  # variable de confirmacion, conocer el metodo de rotacion
j = 0  # auxiliar para la rotacion antihoraria
k = 0  # auxiliar para la rotacion horaria

# Colores de las vistas
linea = negro
frontal = rojo
lateral = azul
superior = morado
piso = blanco
atras = amarillo


def figura(s, g, v):
    # Coordenadas de cada punto del isometrico
    p1 = [0, 0]
    p2 = [0, 70]
    p3 = [-105, 35]
    p4 = [-105, 105]
    p5 = [70, 105]
    p6 = [-35, 140]
    p7 = [70, 175]
    p8 = [-35, 210]
    p9 = [105, 192.5]
    p10 = [0, 227.5]
    p11 = [105, 122.5]
    p12 = [0, 157.5]
    p13 = [175, 157.5]
    p14 = [70, 192.5]
    p15 = [175, 87.5]
    p16 = [70, 122.5]

    # ubicamos cada uno de los puntos en pantalla, con su escalamiento correspondiente
    pp1 = escalamiento(p1, s)
    pp2 = escalamiento(p2, s)
    pp3 = escalamiento(p3, s)
    pp4 = escalamiento(p4, s)
    pp5 = escalamiento(p5, s)
    pp6 = escalamiento(p6, s)
    pp7 = escalamiento(p7, s)
    pp8 = escalamiento(p8, s)
    pp9 = escalamiento(p9, s)
    pp10 = escalamiento(p10, s)
    pp11 = escalamiento(p11, s)
    pp12 = escalamiento(p12, s)
    pp13 = escalamiento(p13, s)
    pp14 = escalamiento(p14, s)
    pp15 = escalamiento(p15, s)
    pp16 = escalamiento(p16, s)

    # correspondiente a la varibale de confirmacion, se procede a realizar un tipo de rotacion

    if v == 1:  # en el plano va a cambiar
        pg1 = Rotacion_ant(pp1, g)
        pg2 = Rotacion_ant(pp2, g)
        pg3 = Rotacion_ant(pp3, g)
        pg4 = Rotacion_ant(pp4, g)
        pg5 = Rotacion_ant(pp5, g)
        pg6 = Rotacion_ant(pp6, g)
        pg7 = Rotacion_ant(pp7, g)
        pg8 = Rotacion_ant(pp8, g)
        pg9 = Rotacion_ant(pp9, g)
        pg10 = Rotacion_ant(pp10, g)
        pg11 = Rotacion_ant(pp11, g)
        pg12 = Rotacion_ant(pp12, g)
        pg13 = Rotacion_ant(pp13, g)
        pg14 = Rotacion_ant(pp14, g)
        pg15 = Rotacion_ant(pp15, g)
        pg16 = Rotacion_ant(pp16, g)

    if v == 2:
        pg1 = Rotacion_hor(pp1, g)
        pg2 = Rotacion_hor(pp2, g)
        pg3 = Rotacion_hor(pp3, g)
        pg4 = Rotacion_hor(pp4, g)
        pg5 = Rotacion_hor(pp5, g)
        pg6 = Rotacion_hor(pp6, g)
        pg7 = Rotacion_hor(pp7, g)
        pg8 = Rotacion_hor(pp8, g)
        pg9 = Rotacion_hor(pp9, g)
        pg10 = Rotacion_hor(pp10, g)
        pg11 = Rotacion_hor(pp11, g)
        pg12 = Rotacion_hor(pp12, g)
        pg13 = Rotacion_hor(pp13, g)
        pg14 = Rotacion_hor(pp14, g)
        pg15 = Rotacion_hor(pp15, g)
        pg16 = Rotacion_hor(pp16, g)

    # Ubicamos los puntos correspondientes en el plano carteciano, con su respectiva rotacion y escalamiento

    p1 = CartesianoPos(origen, pg1)
    p2 = CartesianoPos(origen, pg2)
    p3 = CartesianoPos(origen, pg3)
    p4 = CartesianoPos(origen, pg4)
    p5 = CartesianoPos(origen, pg5)
    p6 = CartesianoPos(origen, pg6)
    p7 = CartesianoPos(origen, pg7)
    p8 = CartesianoPos(origen, pg8)
    p9 = CartesianoPos(origen, pg9)
    p10 = CartesianoPos(origen, pg10)
    p11 = CartesianoPos(origen, pg11)
    p12 = CartesianoPos(origen, pg12)
    p13 = CartesianoPos(origen, pg13)
    p14 = CartesianoPos(origen, pg14)
    p15 = CartesianoPos(origen, pg15)
    p16 = CartesianoPos(origen, pg16)

    # Dibujamos cada una de las caras del isometrico

    pygame.draw.polygon(Pantalla, atras, [p6, p12, p10, p8])  # primer cara atras
    pygame.draw.polygon(Pantalla, atras, [p3, p16, p14, p4])  # segunda cara atras
    pygame.draw.polygon(Pantalla, piso, [p1, p15, p16, p3])  # priemr del piso
    pygame.draw.polygon(Pantalla, lateral, [p1, p2, p4, p3])  # primer cara lateral
    pygame.draw.polygon(Pantalla, superior, [p2, p5, p6, p4])  # priemr cara superior
    pygame.draw.polygon(Pantalla, lateral, [p15, p13, p14, p16])  # cuarta cara lateral
    pygame.draw.polygon(Pantalla, frontal, [p1, p15, p13, p2])  # segunda cara adelante
    pygame.draw.polygon(Pantalla, superior, [p11, p13, p14, p12])  # tercera cara superior
    pygame.draw.polygon(Pantalla, lateral, [p5, p6, p8, p7])  # segunda cara lateral
    pygame.draw.polygon(Pantalla, lateral, [p11, p12, p10, p9])  # tercera cara lateral
    pygame.draw.polygon(Pantalla, frontal, [p5, p11, p9, p7])  # primer cara adelante
    pygame.draw.polygon(Pantalla, superior, [p7, p9, p10, p8])  # segunda cara superior

    pygame.display.flip()


fin = False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        if event.type == pygame.MOUSEBUTTONDOWN:  # al detectar actividad dibuja el isometrico original
            s = [n, n]  # escalamiento
            figura(s, g, v)
        if event.type == pygame.KEYDOWN:  # escalar el isometrico con valores pequeños(hacer mas pequeño el isometrico)
            if event.key == pygame.K_DOWN:
                # el isometrico esta limitado a un tamaño minimo de 0,3 y maximo de 2
                if n >= 0.3:
                    n -= 0.1
                Pantalla.fill(negro)
                s = [n, n]
                figura(s, g, v)
            if event.key == pygame.K_UP:
                if n <= 2:
                    n += 0.1
                Pantalla.fill(negro)
                s = [n, n]
                figura(s, g, v)

            # La rotacion esta limitada a valores entre 0 y 30
            # para las rotaciones, como verificacion se usa (1)para Rotacion Horaria
            #                                              (2)para Rotacion Antihoraria
            if event.key == pygame.K_LEFT:  # rotacion antihoraria

                if j <= 30 and j > 0 and g > 0:  # control de la rotacion cuando este en el tope de horaria
                    v = 1
                    g -= 1
                    j = g

                if g >= 0 and g < 30 and j == 0:  # rotar el isometrico en sentido antihorario siempre y cuando la rotacion en horari0=0
                    v = 2  # ademas los grados de rotacion se encuentre entre los valores correspondientes.
                    g += 1
                    k = g
                Pantalla.fill(negro)
                figura(s, g, v)
            if event.key == pygame.K_RIGHT:  # rotacion horaria

                if k <= 30 and k > 0 and g > 0:  # control de la rotacion cuando este en el tope de antihoraria
                    v = 2
                    g -= 1
                    k = g

                if g >= 0 and g < 30 and k == 0:  # rotar el isometrico en sentido horario siempre y cuando la rotacion antihoraria=0
                    v = 1  # ademas los grados de rotacion se encuentre entre los valores correspondientes.
                    g += 1
                    j = g

                Pantalla.fill(negro)
                figura(s, g, v)

