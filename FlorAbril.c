#include <stdio.h>
#include <stdlib.h>

#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <GL/glut.h>

static GLfloat spin = 0.0;

void init (void){
  /* selecionar cor de fundo (preto) */
  glClearColor (1.0, 1.0, 1.0, 1.0);

	glShadeModel(GL_FLAT);

}

void displayFcn(void){
  glClear(GL_COLOR_BUFFER_BIT);
	glPushMatrix();

  glColor3f(0.0,0.0,.0);
  glBegin(GL_POLYGON);
    glVertex3f(249.f, 250.0f, -1.0f);
		glVertex3f(251.f, 250.0f, -1.0f);
		glVertex3f(249.f, 100.0f, -1.0f);
		glVertex3f(251.f, 100.0f, -1.0f);
	glEnd();

	glRotatef(spin,.0f,0.0f,1.0f);
	glColor3f(1.0,0.0,0.0);
	glBegin(GL_TRIANGLES);
		glVertex2f(250.0f,250.0f);
		glVertex2f(230.0f,200.0f);
		glVertex2f(270.0f,200.0f);
	glEnd();

	glColor3f(0.0,1.0,0.0);
	glBegin(GL_TRIANGLES);
		glVertex2f(250.0f,250.0f);
		glVertex2f(300.0f,230.0f);
		glVertex2f(300.0f,270.0f);
	glEnd();

	glColor3f(0.0,0.0,0.0);
	glBegin(GL_TRIANGLES);
		glVertex2f(250.0f,250.0f);
		glVertex2f(230.0f,300.0f);
		glVertex2f(270.0f,300.0f);
	glEnd();

	glColor3f(1.0,0.0,1.0);
	glBegin(GL_TRIANGLES);
		glVertex2f(250.0f,250.0f);
		glVertex2f(200.0f,270.0f);
		glVertex2f(200.0f,230.0f);
	glEnd();

	//glRectf(-25.0, -25.0, 25.0, 25.0);
	glPopMatrix();
	glutSwapBuffers();

	glFlush();
}

void spinDisplay(){
	spin = spin + 2.0;
	if(spin > 360){
		spin = spin - 360;
	}
	glutPostRedisplay();
}

void reshape(int w, int h){
	glViewport(0,0,(GLsizei)w,(GLsizei)h);
	glMatrixMode (GL_PROJECTION); //Projecao 2D
	glLoadIdentity();
  glOrtho(0.0, 500.0, 0.0, 400.0, -1.0, 1.0); //Definindo os limites da Porta de Visao (ViewPort)
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

void mouse(int button, int state, int x, int y){
	switch (button) {
		case GLUT_LEFT_BUTTON:
			if (state == GLUT_DOWN)
				glutIdleFunc(spinDisplay);
			break;

		case GLUT_MIDDLE_BUTTON:
			if (state == GLUT_DOWN)
				glutIdleFunc(NULL);
			break;
		default:
			break;
	}
}

int main(int argc, char** argv) {

	glutInit(&argc, argv);

	glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize (500, 400);
	glutInitWindowPosition (800, 100);
	glutCreateWindow ("Flor de Abril");

	init();

	// callback routines
	glutDisplayFunc(displayFcn);
	glutReshapeFunc(reshape);
	glutMouseFunc(mouse);

	glutMainLoop();

	
	return 0;

}
