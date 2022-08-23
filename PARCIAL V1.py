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
    pp1 = [0, 0]
    pp2 = [0, 70]
    pp3 = [-105, 35]
    pp4 = [-105, 105]
    pp5 = [70, 105]
    pp6 = [-35, 140]
    pp7 = [70, 175]
    pp8 = [-35, 210]
    pp9 = [105, 192.5]
    pp10 = [0, 227.5]
    pp11 = [105, 122.5]
    pp12 = [0, 157.5]
    pp13 = [175, 157.5]
    pp14 = [70, 192.5]
    pp15 = [175, 87.5]
    pp16 = [70, 122.5]






    # Ubicamos los puntos correspondientes en el plano carteciano, con su respectiva rotacion y escalamiento

    p1 = CartesianoPos(origen, pp1)
    p2 = CartesianoPos(origen, pp2)
    p3 = CartesianoPos(origen, pp3)
    p4 = CartesianoPos(origen, pp4)
    p5 = CartesianoPos(origen, pp5)
    p6 = CartesianoPos(origen, pp6)
    p7 = CartesianoPos(origen, pp7)
    p8 = CartesianoPos(origen, pp8)
    p9 = CartesianoPos(origen, pp9)
    p10 = CartesianoPos(origen, pp10)
    p11 = CartesianoPos(origen, pp11)
    p12 = CartesianoPos(origen, pp12)
    p13 = CartesianoPos(origen, pp13)
    p14 = CartesianoPos(origen, pp14)
    p15 = CartesianoPos(origen, pp15)
    p16 = CartesianoPos(origen, pp16)

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
