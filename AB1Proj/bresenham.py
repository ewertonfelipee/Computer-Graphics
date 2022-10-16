from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def plotline(x1, z1, x2, z2):
    global dx
    global dz
    global E
    global NE
    global d
    global x
    global z

    dx = x2 - x1
    dz  = z2 - z1
    d = 2 * dz - dx
    E = 2 * dz
    NE = 2*(dz - dx)
    x = x1
    z = z1
    draw_pixel(x, z)
    while(x < x2):
        if(d <= 0):
            d += E
            x +=1
        else:
            d +=NE
            x +=1
            z +=1
        draw_pixel(x, z)

def draw_pixel(x ,z):
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex3f(x, 1, z)
    glEnd()
    glFlush()