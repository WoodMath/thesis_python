import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from PIL import Image

from inputs import *
from imaging import *
from main import *
Angle = 0
Incr = 1

def create_3d_axes():
	glNewList(2,GL_COMPILE)
	glBegin(GL_LINES)
	glColor3f(1,0,0)
	glVertex3f(0,0,0)
	glVertex3f(2,0,0)
	glEnd() 

	glBegin(GL_LINES)
	glColor3f(0,1,0)
	glVertex3f(0,0,0)
	glVertex3f(0,2,0)
	glEnd() 

	glBegin(GL_LINES)
	glColor3f(0,0,1)
	glVertex3f(0,0,0)
	glVertex3f(0,0,2)
	glEnd() 
	glEndList()         

def display():
	global Angle
	global Incr
	global vCamPos
	global ims
      
	w=glutGet(GLUT_WINDOW_WIDTH)
	h=glutGet(GLUT_WINDOW_HEIGHT)
      
#	glScissor (0,0,w,h)
#	glClearColor(0,0,0,0)
#	glClear(GL_COLOR_BUFFER_BIT)
      
#	glEnable(GL_SCISSOR_TEST)
#	glScissor(int(0.05*w),int(0.55*h),int(0.4*w),int(0.4*h))
#	glClearColor(0.4,0.4,0.6,0)
	glClearColor(0.0,0.0,0.0,0.0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glFrustum(-1,1,-1,1,1,30)
	gluLookAt(0,0,3,0,0,0,0,1,0)
	glMatrixMode(GL_MODELVIEW)    
#	glViewport(int(0.05*w),int(0.55*h),int(0.4*w),int(0.4*h))
#	glCallList(1)

	ims.renderImage(0)
 
#	glCallList(2);
   
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glLoadIdentity()

	glCallList(2) 
	glPopMatrix()


          
      
	glFlush()
	glutSwapBuffers()                 
      
	glLoadIdentity()
	glRotated(Angle,0,1,0)
	Angle = Angle + Incr


def keyHandler(Key, MouseX, MouseY):
	global Incr
	if Key == b'f' or Key == b'F':
		print (b"Speeding Up")
		Incr = Incr + 1
	elif Key == b's' or Key == b'S':
		if Incr == 0:
			print ("Stopped")
		else:
			print ("Slowing Down")
			Incr = Incr - 1
	elif Key == b'q' or Key == b'Q' or Key == b'\x1b':
		print ("Bye")
		sys.exit()
	else:
		print ("Invalid Key ",Key)

def timer(dummy):
	display()
	glutTimerFunc(30,timer,0)

def reshape(w, h):
	print ("Width=",w,"Height=",h)
	glViewport(0,0,w,h)
      
