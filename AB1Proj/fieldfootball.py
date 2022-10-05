from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 480


def init():
  glClearColor(0.0, 0.0, 0.0, 0.0)
  
def ball():
  glPushMatrix()
  glColor4f(1.0, 1.0, 0.0, 1.0)
  glutSolidSphere(0.05, 30, 30)
  glPopMatrix()

def field():
  
  # glBegin(GL_POLYGON)
  glColor3f(0.0, 1.0, 0.0)
  glRectf(-1.0, 1.0, 1.0, -1.0)
  # glEnd()
  
  
def show():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glEnable(GL_DEPTH_TEST)
  field()
  ball()
  glutSwapBuffers()
  
def reshape(w,h):
  pass

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
  glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
  glutCreateWindow("football field")
  init()
  glutDisplayFunc(show)
  glutReshapeFunc(reshape)
  glutMainLoop()
  
if __name__ == "__main__":
  main()