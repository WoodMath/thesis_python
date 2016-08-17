import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from PIL import Image

import numpy as np

import csv
import copy
import functions

from numpy.linalg import inv
from numpy.linalg import qr
from numpy.linalg import det
#from numpy.linalg import transpose
from numpy.linalg import norm
from numpy.linalg import matrix_rank

from numpy import linalg as LA


from inputs import *
from functions import *

def vect_int(arr):
	rtrn = []
	for k in arr:
		rtrn.append(int(k))
	return rtrn

def vect_float(arr):
	rtrn = []
	for k in arr:
		rtrn.append(float(k))
	return rtrn


Angle = 0
Incr = 1

sReferences="""
Taken From:
    https://docs.python.org/3.6/library/csv.html
"""


class Im:
      
	def __init__(self):
		self.matrixProjection=[]
		self.matrixA=[]
		self.matrixR=[]
		self.matrixT=[]
		self.sMatrixFilename=[]
		self.sTextureFilename=[]
		self.imageData=[]
		self.imageBytes=[]
		self.imageSize=[]
		self.ID=None
		print(' self.__func__.__name__ = ', str(self.__class__.__name__))
		return

	def loadCSV(self,sFilename):
		arr=[]
		with open(sFilename, newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in spamreader:
				col = vect_float(row[0].split(','))
				arr.append(col)
        
		return arr
#		print(' row = ',str(row))
#                  
#		print(' self.matrixProjection = ', str(self.matrixProjection))
#		for ent in col:
#			print('end = ',str(ent),end='\n')
#			print(', '.join(row))

	def loadProjectionMatrix(self, sFilename):

		try:
			arr=self.loadCSV(sFilename)
		except:
			print(' Problem loading \'', str(sFilename), '\'')
		self.matrixProjection = arr

		(a,r,t) = art(arr)
		self.matrixA=a
		self.matrixR=r
		self.matrixT=t

		return arr
    

      
	def loadImage(self, sImage, sProjection):
	#     Loads an image and its projection matrix,
	# adds to collection, and return identifier
#		global iTextureCount
#		global iTextureIDs
#		global sTextureFilenames
#		global sMatrixFilenames
#		global mProjections
#		sTextureFilenames.append(sImage)
#		sMatrixFilenames.append(sProjection)
#		iTextureCount += 1
#		print('sTextureFilenames=',sTextureFilenames)
#		print('iTextureCount=',str(iTextureCount))      
#		print('iTextureIDs=',str(iTextureIDs))
		self.loadProjectionMatrix(sProjection)
		self.sMatrixFilename=sProjection
		self.sTextureFilename=sImage


		image = Image.open(sImage)
		self.imageData = image
		self.imageSize = image.size
		self.imageBytes = image.tobytes("raw", "RGBX", 0, -1)

		self.ID = glGenTextures(1)
		print(' self.ID = ', str(self.ID))
		print(' type(self.ID) = ', str(type(self.ID)))

#		image.show()


		return


class Ims:
	def __init__(self):
		self.count=0
		self.images=[]
		self.IDs=[]

		print(' self.__func__.__name__ = ', str(self.__class__.__name__))
		return

	def addImage(self, sImage, sProjection):

		im=Im()
		im.loadImage(sImage, sProjection)

		self.images.append(im)
		self.count += 1
        
		return im


	def loadImages(self):
	# Loads the image collection into OpenGL format
      
		print(' self.count = ',str(self.count))
		if(not self.count):
			return

		self.IDs = [i.ID for i in self.images]
        

		glEnable(GL_TEXTURE_2D)

		for i in self.images:

			iID = i.ID
			print(' iID = ', str(iID))
#			glActiveTexture(GL_TEXTURE0 + iID - 1)
			glBindTexture(GL_TEXTURE_2D, iID)
			iIndex = self.IDs.index(iID)

			ix = i.imageSize[0]
			iy = i.imageSize[1]

			glPixelStorei(GL_UNPACK_ALIGNMENT,1)
			glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, i.imageBytes)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
			glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
#			glEnable(GL_TEXTURE_2D)


		glDisable(GL_TEXTURE_2D)
		return
		glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
		glClearDepth(1.0)			# Enables Clearing Of The Depth Buffer
		glDepthFunc(GL_LESS)			# The Type Of Depth Test To Do
		glEnable(GL_DEPTH_TEST)			# Enables Depth Testing
		glShadeModel(GL_SMOOTH)			# Enables Smooth Color Shading
            
		glMatrixMode(GL_PROJECTION)
#		glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
#		gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

		glMatrixMode(GL_MODELVIEW)
    
		return

	def renderImage(self,iIndex):
	# Renders the images from the collection


		if(not len(self.IDs)):
			return

		iID = self.images[iIndex].ID
		print(' iID = ', str(iID))
		print(' iIndex = ', str(iIndex))
        
		glActiveTexture(GL_TEXTURE0 + iIndex)
		glBindTexture(GL_TEXTURE_2D, iID)

#		glLoadIdentity()					# Reset The View
#		glTranslatef(0.0,0.0,-5.0)

#		glColor3f(1.0,1.0,1.0)
#		glClearColor(0.0,0.0,0.0,0.0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


#		glLoadIdentity()
#		glMatrixMode(GL_TEXTURE)

		glEnable(GL_TEXTURE_2D)
		glBegin(GL_QUADS)			    # Start Drawing The Cube

		# Front Face (note that the texture's corners have to match the quad's corners)
		glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  0.0)	# Bottom Left Of The Texture and Quad
		glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  0.0)	# Bottom Right Of The Texture and Quad
		glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  0.0)	# Top Right Of The Texture and Quad
		glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  0.0)	# Top Left Of The Texture and Quad

		glEnd()
		glDisable(GL_TEXTURE_2D)

#		glutSwapBuffers()

		return

