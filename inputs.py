import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from PIL import Image

vCamPos = [0,0,-1];

# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

sReferences="""
Taken From:
	https://www.opengl.org/documentation/specs/glut/spec3/node49.html (glutKeyboardFunc)
	https://www.opengl.org/documentation/specs/glut/spec3/node50.html (glutMouseFunc)
	https://www.opengl.org/resources/libraries/glut/spec3/node51.html (glutMotionFunc)
	https://www.opengl.org/resources/libraries/glut/spec3/node54.html (glutSpecialFunc)
	https://www.opengl.org/documentation/specs/glut/spec3/node73.html (glutGetModifiers)
"""

def keyPressed(*args):
	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		sys.exit()
	if args[0] == b'q' or args[0] == b'Q' or args[0] == b'\x1b':
		sys.exit()

def specialPressed(*args):
	global vCamPos
	# If escape is pressed, kill everything.
	iMod = glutGetModifiers()
	if args[0] == ESCAPE:
		sys.exit()
	if(args[0] == GLUT_KEY_LEFT):
		print('GLUT_KEY_LEFT')
		vCamPos[0] += -15
	if(args[0] == GLUT_KEY_RIGHT):
		print('GLUT_KEY_RIGHT')
		vCamPos[0] += 15
	if(args[0] == GLUT_KEY_DOWN):
		print('GLUT_KEY_DOWN')
		vCamPos[1] += -15
	if(args[0] == GLUT_KEY_UP):
		print('GLUT_KEY_UP')
		vCamPos[1] += 15
        
def keyPressedUp(*args):
	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		sys.exit()

def specialPressedUp(*args):
	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		sys.exit()
	if(args[0] == GLUT_KEY_LEFT):
		print('GLUT_KEY_LEFT')
