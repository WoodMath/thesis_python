import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from PIL import Image

# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\x1b'

sReferences="""
Taken From:
    https://www.opengl.org/documentation/specs/glut/spec3/node49.html (glutKeyboardFunc)
    https://www.opengl.org/documentation/specs/glut/spec3/node50.html (glutMouseFunc)
    https://www.opengl.org/resources/libraries/glut/spec3/node51.html (glutMotionFunc)
    https://www.opengl.org/resources/libraries/glut/spec3/node54.html (glutSpecialFunc)    
"""

def keyPressed(*args):
	# If escape is pressed, kill everything.
    if args[0] == ESCAPE:
	    sys.exit()


def specialPressed(*args):
	# If escape is pressed, kill everything.
    if args[0] == ESCAPE:
	    sys.exit()
