from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640

SLICES = 15
STACKS = 15

eye = [0, 0, 0]
center = [0, 0, 0]
up = [0, 1, 0] 

colors ={
    "green": [0.1, 1., 0.1, 0.],
    "white": [0.9, 0.9, 0.9, 0.]
}

UNIT_PIXEL = 0.2
UNIT_DIST = 1
unit_vel = 5

def init_light():
    light_ambient = [0.4, 0.4, 0.4, 1]
    light_diffuse = [0.7, 0.7, 0.7, 1]
    light_specular = [0.9, 0.9, 0.9, 1]
    light_pos = [0, 200, -100, 1]
   
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.1, 0.1, 0.1, 1])

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    glEnable(GL_LIGHT0)


def init():
    global eye
    eye = [0, 20, 40]

    glClearColor(0.0, 0.1, 0.0, 1.0) 
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(eye[0]   , eye[1]   , eye[2],
              center[0], center[1], center[2],
              up[0]    , up[1]    , up[2])

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, 100.)

def move_camera():
    global eye
    global center
    global up

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eye[0]   , eye[1]   , eye[2],
              center[0], center[1], center[2],
              up[0]    , up[1]    , up[2])

    #glMatrixMode(GL_PROJECTION)
    #gluPerspective(45, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, 100.)

def draw_ball(pos):
    glPushMatrix()
    glColor4fv(colors["white"])
    glTranslatef(pos[0] * UNIT_PIXEL, pos[1] * UNIT_PIXEL, pos[2] * UNIT_PIXEL)
    glutSolidSphere(UNIT_PIXEL * 1, SLICES*2, STACKS*2)
    glPopMatrix()

def draw_cube():
    glPushMatrix()
    glColor4fv(colors["green"])
    glScalef(105, 2, 65)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear color and depth buffers
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_MODELVIEW)

    draw_cube()
    draw_ball([0, 4, 0])

    glutSwapBuffers()

def reshape(width, height):
    pass

def keyboard_handler(key, x, y):
    global eye
    global center
    global up

    if key == b"w":
        eye[2] += UNIT_DIST * UNIT_PIXEL * unit_vel
        center[2] += UNIT_DIST * UNIT_PIXEL * unit_vel

        print(eye, center, up)
    elif key == b"s":
        eye[2] -= UNIT_DIST * UNIT_PIXEL * unit_vel
        center[2] -= UNIT_DIST * UNIT_PIXEL * unit_vel

    elif key == b"u":
        up[0] = 1   


    elif key == b"z":
        eye[2] -= UNIT_DIST * UNIT_PIXEL * unit_vel

    move_camera()

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowPosition(0,0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  
glutCreateWindow("Football Field Simulator")

init() 
init_light()

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard_handler)

glutMainLoop()