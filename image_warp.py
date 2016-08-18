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
	http://scikit-image.org/docs/dev/auto_examples/applications/plot_geometric.html
	http://effbot.org/imagingbook/image.htm#tag-Image.Image.transform
	http://stackoverflow.com/questions/5071063/is-there-a-library-for-image-warping-image-morphing-for-python-with-controlled
	http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html
	http://www.perrygeo.com/python-affine-transforms.html
	    
"""


im = Image.open('./images/Sport0.png')
im1 = im.transform(im.size, Image.AFFINE, (1,0,0,0,1,-im.size[1]))
k=im.transform((im.size[0],im.size[1]), Image.PERSPECTIVE, (1,0,-50,0,1,-50,0,0))
#im.show()
k.show()
