# libreria.py
import math
import pygame
# --------------------------------COLORES--------------------------------------------------
rojo=[255,0,0]
blanco=[255,255,255]
azul=[0,255,255]
morado=[116,11,228]
negro=[0,0,0]
amarillo=[228,218,11]


def Punto (ventana,color,pos):
    pygame.draw.circle(ventana,color,pos,3)
    pygame.display.flip()

def Linea (ventana,color,pos_inicio,pos_final):
    pygame.draw.line(ventana,color,pos_inicio,pos_final,5)
    pygame.display.flip()

def Cartesiano (ventana,pos):
    pygame.draw.line(ventana,azul,[pos[0],(pos[1]-600)],[pos[0],(pos[1]+600)],5)
    pygame.draw.line(ventana,azul,[(pos[0]-600),pos[1]],[(pos[0]+600),pos[1]],5)
    pygame.display.flip()

def Triangulo (ventana,color,a,b,c):
    pygame.draw.polygon(ventana,color,[a,b,c])
    pygame.display.flip()


def CartesianoPos (origen,pos):
    p1=pos[0]+origen[0]
    p2=origen[1]-pos[1]
    return [int(p1),int(p2)]

def PosCartesiano (origen,pos):
    x=pos[0]-origen[0]
    y=origen[1]-pos[1]
    return [int(x),int(y)]

def Polar(r,a):
    ar=math.radians(a)
    x=r*math.cos(ar)
    y=r*math.sin(ar)
    return [int(x),int(y)]

def traslacion(punto,traslacion):
    xt = punto[0]+traslacion[0]
    yt = punto[1]+traslacion[1]
    return [xt,yt]

def escalamiento(p,s): #s es el escalamiento
    xp=p[0]*s[0]
    yp=p[1]*s[1]
    return [xp,yp]


def Rotacion_hor(punto,grado):
    xp=int(punto[0]*math.cos(math.radians(grado)) - punto[1]*math.sin(math.radians(grado)))
    yp=int(punto[0]*math.sin(math.radians(grado)) + punto[1]*math.cos(math.radians(grado)))
    return([xp,yp])

def Rotacion_ant(punto,grado):
    xp=int(punto[0]*math.cos(math.radians(grado)) + punto[1]*math.sin(math.radians(grado)))
    yp=int(-punto[0]*math.sin(math.radians(grado)) + punto[1]*math.cos(math.radians(grado)))
    return([xp,yp])

#def traslacion(punto,tx,ty):
   # x_d = punto[0] + tx
    #y_d = punto[1] + ty
   # return ([x_d,y_d])
