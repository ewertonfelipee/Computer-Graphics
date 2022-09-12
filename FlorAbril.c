#include <stdio.h>
#include <stdlib.h>

// #include <GL/glew.h>
// #include <GLFW/glfw3.h>
#include <GL/glut.h>

void init (void){
  /* selecionar cor de fundo (preto) */
  glClearColor (0.0, 0.0, 0.0, 0.0);

  glMatrixMode (GL_PROJECTION); //Projecao 2D

  glOrtho(0.0, 500.0, 0.0, 400.0, -1.0, 1.0); //Definindo os limites da Porta de Visao (ViewPort)

}

void displayFcn(void){
  glClear(GL_COLOR_BUFFER_BIT);

  glColor3f(1.0,1.0,.0);
  glBegin(GL_POLYGON);

    glVertex3f(249.f, 250.0f, -1.0f);
		glVertex3f(251.f, 250.0f, -1.0f);
		glVertex3f(249.f, 100.0f, -1.0f);
		glVertex3f(251.f, 100.0f, -1.0f);

	glEnd();
}


int main(int argc, char** argv) {

	glutInit(&argc, argv);

	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize (500, 400);
	glutInitWindowPosition (200, 200);
	glutCreateWindow ("Flor de Abril");

	init();

	glutDisplayFunc(displayFcn);

	glutMainLoop();

	
	return 0;

}
