from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import bresenham
import bresenham2
import bresenhamCircle


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640

SLICES = 15
STACKS = 15

eye = [0, 0, 0]
center = [0, 0, 0]
up = [0, 1, 0] 

tranx = 0
trany = 0
tranz = 0
rota = 1
score1 = 0
score2 = 0

colors ={
    "green": [0.1, 1., 0.1, 0.],
    "white": [0.9, 0.9, 0.9, 0.]
}

UNIT_PIXEL = 0.2
UNIT_DIST = 1
unit_vel = 5

# def init_light():
#     light_ambient = [0.4, 0.4, 0.4, 1]
#     light_diffuse = [0.7, 0.7, 0.7, 1]
#     light_specular = [0.9, 0.9, 0.9, 1]
#     light_pos = [0, 200, -100, 1]
   
#     glEnable(GL_DEPTH_TEST)
#     glEnable(GL_LIGHTING)

#     glShadeModel(GL_SMOOTH)
#     glEnable(GL_COLOR_MATERIAL)
#     glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
#     glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
#     glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.1, 0.1, 0.1, 1])

#     glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
#     glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
#     glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
#     glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

#     glEnable(GL_LIGHT0)


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

# def draw_goal1Dots():
    
#     glPushMatrix()
#     glColor4fv(colors["white"])
#     # glPointSize(5)
#     glBegin(GL_POINTS)
#     glVertex3f(10,0,-1)
#     glVertex3f(10,0,2)
#     glVertex3f(10, 1.5, -1)
#     glVertex3f(10, 1.5, 2)
#     glEnd()

def draw_goal1Lines():
    glPushMatrix()
    glColor4fv(colors["white"])
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex3f(10,0,2)
    glVertex3f(10,1.5,2)
    glVertex3f(10,1.5,-1)
    glVertex3f(10,0,-1)
    glVertex3f(10, 1.5, -1)
    glVertex3f(10, 1.5, 2)
    glEnd()
    glPopMatrix()

def draw_goal1(pos):
    # draw_goal1Dots()
    draw_goal1Lines()


# def draw_goal2Dots():
    
#     glPushMatrix()
#     glColor4fv(colors["white"])
#     glBegin(GL_POINTS)
#     glVertex3f(-10,0,-1)
#     glVertex3f(-10,0,2)
#     glVertex3f(-10, 1.5, -1)
#     glVertex3f(-10, 1.5, 2)
#     glEnd()

def draw_goal2Lines():
    glPushMatrix()
    glColor4fv(colors["white"])
    glBegin(GL_LINES)
    glVertex3f(-10,0,2)
    glVertex3f(-10,1.5,2)
    glVertex3f(-10,1.5,-1)
    glVertex3f(-10,0,-1)
    glVertex3f(-10, 1.5, -1)
    glVertex3f(-10, 1.5, 2)
    glEnd()
    glPopMatrix()


def draw_goal2(pos):
    # draw_goal2Dots()
    draw_goal2Lines()

def draw_ball(pos):
    glPushMatrix()
    glColor4fv(colors["white"])
    glRotatef(rota, rota, 0, rota)
    glTranslatef(tranx, 1, tranz)
    glutSolidSphere(UNIT_PIXEL * 1, SLICES*2, STACKS*2)
    glPopMatrix()
    
def draw_cube():  
    glPushMatrix()
    glColor4fv(colors["green"])
    glScalef(105, 2, 70)
    glutSolidCube(UNIT_PIXEL * 1)
    glPopMatrix()
    
def goal():
    global score1
    global score2
    global tranx
    global tranz
    if(tranx > 10 and (-1 < tranz < 3)):
        score1+=1
        print(f"jogador 1 {score1} x {score2} jogador 2 ")
        tranx = 0
        tranz = 0

    elif(tranx < -10 and (-1 < tranz < 4)):
        score2+=1
        print(f"jogador 1 {score1} x {score2} jogador 2 ")
        tranx = 0
        tranz = 0

def draw_line():
    bresenham.plotline(-10,8,10,8)
    bresenham.plotline(-10,-4.5,10,-4.5)
    bresenham2.plotline2(0,-5,0,8)
    bresenham2.plotline2(10,-5,10,8)
    bresenham2.plotline2(-10,-5,-10,8)
    bresenhamCircle.midPointCircle(2)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear color and depth buffers
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_MODELVIEW)

    draw_cube()
    goal()
    draw_ball([0, 0, 0])
    draw_goal1([70,4,35])
    draw_goal2([-70,4,35])
    draw_line()

    glutSwapBuffers()

def reshape(width, height):
    pass

def keyboard_handler(key, x, y):
    global eye
    global center
    global up
    global tranx
    global trany
    global tranz
    global rota
    
    # move the camera
    if key == b"w":
        eye[2] += UNIT_DIST * UNIT_PIXEL * unit_vel
        center[2] += UNIT_DIST * UNIT_PIXEL * unit_vel

        # print(eye, center, up)
    elif key == b"s":
        eye[2] -= UNIT_DIST * UNIT_PIXEL * unit_vel
        center[2] -= UNIT_DIST * UNIT_PIXEL * unit_vel

    # elif key == b"u":
    #     up[0] = 1   
    elif key == b"z":
        eye[2] -= UNIT_DIST * UNIT_PIXEL * unit_vel
        
    elif key == b"d":
        eye[0] += UNIT_DIST * UNIT_PIXEL * unit_vel
        center[0] += UNIT_DIST * UNIT_PIXEL * unit_vel
            
    elif key == b"a":
        eye[0] -= UNIT_DIST * UNIT_PIXEL * unit_vel
        center[0] -= UNIT_DIST * UNIT_PIXEL * unit_vel

    # move the ball
    elif key == b"l":
        tranx+=0.5
        rota+1
    elif key == b"i":
        tranz-=0.5
        rota-1
    elif key == b"j":
        tranx-=0.5
        rota-1
    elif key == b"k":
        tranz+=0.5
        rota+1
    # elif key == b"y":
    #     rota+1
    # elif key == b"h":
    #     rota-1

        
    # draw_ball(pos)
    move_camera()

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowPosition(0,0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  
glutCreateWindow("Football Field Simulator")

init() 
#init_light()

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard_handler)

glutMainLoop()