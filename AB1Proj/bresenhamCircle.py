from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#x,z,d,px,pz

def midPointCircle(r):
    global x, z, d
    x = 0
    z = r
    d = 5/4 - r
    plot(x,z)
    while(z > x):
        if(d < 0):
            x+=1
            d = 2*x+1
        else:
            z-=1
            x+=1
            d+=2*(x - z) + 1
        plot(x,z)
        plot(x,-z)
        plot(-x,z)
        plot(-x,-z)
        plot(z, x)
        plot(-z, x)
        plot(z, -x)
        plot(-z, -x)

def plot(x, z):
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex3f(x+0, 1, z+2)
    glEnd()
    glFlush()