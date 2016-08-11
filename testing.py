import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *

from inputs import *
from imaging import *
from callbacks import *
from functions import *


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGBA|GLUT_DEPTH)
glutInitWindowSize(800, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"PyOpenGL Demo")

k=Im()
#k.loadCSV('./data/pml.csv')
k.loadImage('./images/Sport0.png','./data/pml.csv')

#k.addImage('./images/Sport0.png','./data/pml.csv')
#k.loadImages()
#(a,r,t)=k.decompose()
