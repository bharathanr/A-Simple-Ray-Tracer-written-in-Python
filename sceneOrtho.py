#This is the screne configuration file. It is used to set up the world for rendering.

#Relative to the screen -
#x axis- Left, Right
#y axis- Top, Botttom
#z axis: Outside, Inside

#Colors - R,G,B tuple where each component varies between zero and one.

from numpy import array

from sphere import Sphere
from vector3 import Vector3

#Description of the scene
#Eventually, this should be read from a file

#List of lights in this scene
lights = []

#List of objects in this scene
objects = []

#Background color
BGCOLOR = (0, 0, 0)

#Image size
IMAGE_SIZE = (1024, 768)

#Recursion Level
MAX_RECURSIONS = 3

def initialise_default_scene():
    #Initialise objects
    center = Vector3(1024/2, 768/2, -13)
    radius = 6
    color = (0, 0, 1)
    
    sphere1 = Sphere(center, radius, color)
    
    #center2 = Vector3(1024/2, 768/2, -10)
    #radius2 = 20 
    #color2 = (1, 0, 1)
    
    #sphere2 = Sphere(center2, radius2, color2)
    globs = globals()
    #Add the objects to the object list
    globs['objects'].append(sphere1)

    #globs['objects'].append(sphere2)
