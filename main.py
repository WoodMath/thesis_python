import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *

from inputs import *
from imaging import *

ims = Ims()
from callbacks import *

def main(argv):

	global ims

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGBA|GLUT_DEPTH)
	glutInitWindowSize(800, 500)
	glutInitWindowPosition(100, 100)
	glutCreateWindow(b"PyOpenGL Demo")

	#load_image('NeHe.bmp','./data/ml.csv')
	ims.addImage('./images/Sport0.png','./data/pml.csv')
	#load_image('./images/Sport1.png','./data/pmr.csv')
	ims.loadImages()



	glClearColor(1,1,0,0)
	glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LESS)
	glShadeModel(GL_SMOOTH)

	glutDisplayFunc(display)
	glutKeyboardFunc(keyPressed)
	glutSpecialFunc(specialPressed)
	#glutKeyboardUpFunc(keyPressedUp)
	#glutSpecialUpFunc(specialPressedUp)

	glutTimerFunc(30,timer,0)
	glutReshapeFunc(reshape)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glMatrixMode(GL_MODELVIEW)
	#create_pyramid()
	create_3d_axes()
	#display()

	glutMainLoop()


if __name__ == "__main__":
	main(sys.argv[1:])
