from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def plotline2(x1, z1, x2, z2):
    global dx
    global dz
    global E
    global NE
    global d
    global x
    global z

    dx = x2 - x1
    dz  = z2 - z1
    d = 2 * dx - dz
    E = 2 * dx
    NE = 2*(dx - dz)
    x = x1
    z = z1
    draw_pixel2(z, x)
    while(z < z2):
        if(d <= 0):
            d += E
            z +=0.1
        else:
            d +=NE
            z +=0.1
            x +=0.1
        draw_pixel2(z, x)

def draw_pixel2(z ,x):
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex3f(x, 0.2, z)
    glEnd()
    glFlush()