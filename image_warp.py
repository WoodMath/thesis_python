import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from PIL import Image
import csv
import functions
import numpy as np

sReferences="""
Taken From:
	http://scikit-image.org/
	http://effbot.org/imagingbook/image.htm#tag-Image.Image.transform
	http://stackoverflow.com/questions/5071063/is-there-a-library-for-image-warping-image-morphing-for-python-with-controlled
	http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html
    
"""


im = Image.open('./images/Sport0.png')
im1 = im.transform(im.size, Image.AFFINE, (1,0,0,0,-im.size[1],0))
k=im.transform((im.size[0],im.size[1]), Image.AFFINE, (1,0,-50,0,1,-50))
#im.show()
k.show()
