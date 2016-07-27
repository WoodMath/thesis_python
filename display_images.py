import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from PIL import Image
from input_states import *

Angle = 0
Incr = 1

iTextureCount=0
iTextureIDs=[]
iTextureIDs_list=[]
sTextureFilenames=[]
mProjections=[]
class Im:
      def __init__(self):
            return
      
def load_image(sImage, mProjection):
      # Loads an image and its projection matrix,
      # adds to collection, and return identifier
      global iTextureCount
      global iTextureIDs
      global sTextureFilenames
      global mProjections
      sTextureFilenames.append(sImage)
      iTextureCount += 1
      print('sTextureFilenames=',sTextureFilenames)
      print('iTextureCount=',str(iTextureCount))      
      print('iTextureIDs=',str(iTextureIDs))
      
      return

def load_images():
      # Loads the image collection into OpenGL format

      global iTextureCount
      global iTextureIDs
      global iTextureIDs_list
      global sTextureFilenames

      print('iTextureCount=',str(iTextureCount))
      
      iTextureIDs=glGenTextures( iTextureCount )
      print('iTextureIDs=',str(iTextureIDs))

      if(iTextureIDs.size==1):
            iTextureIDs_list = [iTextureIDs]
      else:
            iTextureIDs_list = iTextureIDs
#      iTextureIDs_list = iTextureIDs

      for iID in iTextureIDs_list:
            
            glBindTexture(GL_TEXTURE_2D, iID)
            iIndex = iTextureIDs_list.index(iID)
            sFilename = sTextureFilenames[iIndex]
            image = Image.open(sFilename)
	
            ix = image.size[0]
            iy = image.size[1]

            print(' ix = ',str(ix))
            print(' iy = ',str(iy))

            image = image.tobytes("raw", "RGBX", 0, -1)
	
            # Create Texture
            glBindTexture(GL_TEXTURE_2D, iID)   # 2d texture (x and y size)

            glPixelStorei(GL_UNPACK_ALIGNMENT,1)
            glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
            glEnable(GL_TEXTURE_2D)



      glEnable(GL_TEXTURE_2D)
      return
      glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
      glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
      glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
      glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
      glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	
      glMatrixMode(GL_PROJECTION)
#      glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
#      gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

      glMatrixMode(GL_MODELVIEW)
    
      return

def render_image(iID):
      # Renders the images from the collection

      global iTextureIDs
      global iTextureIDs_list

      print('iTextureIDs = ',str(iTextureIDs))
      print('iTextureIDs = ',str(type(iTextureIDs)))
      print('iTextureIDs_list = ',str(type(iTextureIDs_list)))


#      iIndex = iTextureIDs_list.index(iID)
      iIndex = iID
      print(' iIndex = ',str(iIndex))
#      return
      if(not iTextureIDs.size):
            return
      elif(iTextureIDs.size==1):
            glActiveTexture(GL_TEXTURE0 + iTextureIDs - 1)
      else:
            glActiveTexture(GL_TEXTURE0 + iTextureIDs[iID] - 1)

      glBindTexture(GL_TEXTURE_2D, iTextureIDs)

#      glLoadIdentity()					# Reset The View
#      glTranslatef(0.0,0.0,-5.0)

#      glColor3f(1.0,1.0,1.0)
#      glClearColor(0.0,0.0,0.0,0.0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


#      glLoadIdentity()
#      glMatrixMode(GL_TEXTURE)

      glEnable(GL_TEXTURE_2D)
      glBegin(GL_QUADS)			    # Start Drawing The Cube

      # Front Face (note that the texture's corners have to match the quad's corners)
      glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  0.0)	# Bottom Left Of The Texture and Quad
      glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  0.0)	# Bottom Right Of The Texture and Quad
      glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  0.0)	# Top Right Of The Texture and Quad
      glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  0.0)	# Top Left Of The Texture and Quad

      glEnd()
      glDisable(GL_TEXTURE_2D)

      glutSwapBuffers()

      return
        
def create_pyramid():
      glNewList(1,GL_COMPILE)
      glBegin(GL_TRIANGLES)

      glVertex3f(0,0,0)
      glVertex3f(1,1,0)
      glVertex3f(0,1,0)
      glVertex3f(0,0,0)
      glVertex3f(1,0,0)
      glVertex3f(1,1,0)
      
      glColor3f(0,1,0)
      glVertex3f(0,0,0)
      glVertex3f(0,1,0)
      glVertex3f(0.5,0.5,1)
      
      glColor3f(0,0,1)
      glVertex3f(0,1,0)
      glVertex3f(1,1,0)
      glVertex3f(0.5,0.5,1)
      
      glColor3f(1,1,0)
      glVertex3f(1,1,0)
      glVertex3f(1,0,0)
      glVertex3f(0.5,0.5,1)
      
      glColor3f(1,0,1)
      glVertex3f(1,0,0)
      glVertex3f(0,0,0)
      glVertex3f(0.5,0.5,1)
      
      
      glEnd() 
      glEndList()

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
      w=glutGet(GLUT_WINDOW_WIDTH)
      h=glutGet(GLUT_WINDOW_HEIGHT)
      
#      glScissor (0,0,w,h)
#      glClearColor(0,0,0,0)
#      glClear(GL_COLOR_BUFFER_BIT)
      
#      glEnable(GL_SCISSOR_TEST)
#      glScissor(int(0.05*w),int(0.55*h),int(0.4*w),int(0.4*h))
#      glClearColor(0.4,0.4,0.6,0)
      glClearColor(0.0,0.0,0.0,0.0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glFrustum(-1,1,-1,1,1,30)
      gluLookAt(0,0,3,0,0,0,0,1,0)
      glMatrixMode(GL_MODELVIEW)    
#      glViewport(int(0.05*w),int(0.55*h),int(0.4*w),int(0.4*h))
#      glCallList(1)

      render_image(0)
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




          
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGBA|GLUT_DEPTH)
glutInitWindowSize(800, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"PyOpenGL Demo")

load_image('NeHe.bmp','./data/ml.csv')
#load_image('./images/Sport0.png','./data/ml.csv')
#load_image('./images/Sport1.png','./data/mr.csv')
load_images()

glClearColor(1,1,0,0)
glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)
glShadeModel(GL_SMOOTH)

glutDisplayFunc(display)
glutKeyboardFunc(keyHandler)
glutTimerFunc(300,timer,0)
glutReshapeFunc(reshape)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glMatrixMode(GL_MODELVIEW)
#create_pyramid()
create_3d_axes()
#display()

glutMainLoop()

