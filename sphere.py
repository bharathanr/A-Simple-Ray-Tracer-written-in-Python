from math import sqrt

from primitive import Primitive
from vector3 import dot_product

DEBUG = 0 

class Sphere(Primitive):
    def __init__(self, center, radius, color):
        super(Sphere, self).__init__(color)
        self.center = center
        self.radius = radius

    def find_intersection(self, ray):
        #From : http://www.cs.unc.edu/~rademach/xroads-RT/RTarticle.html
        result = [0, False]
        #Ray to sphere direction
        oc = self.center - ray.origin
        #Ray to sphere length squared
        oc2 = dot_product(oc, oc)
        #Distance to the sphere along the ray
        #In other words, the point on the ray closest to the center
        v = dot_product(oc, ray.direction)
        
        #DEBUG
        #print oc2, v
        
        #Is the ray origin outside the sphere?
        outside = oc2 > (self.radius ** 2)
        if v < 0 and outside:
            if DEBUG == 1:
                print "ping"
            return result
        discriminant = (self.radius * self.radius) - (oc2 - v*v)
        if discriminant < 0:
            if DEBUG == 1:
                print "pong"
            return result
        else:
            if outside:
                temp = v - sqrt(discriminant)
            else:
                temp = v + sqrt(discriminant)

            if temp < 0:
                return result
            
            result[1] = True
            result[0] = sqrt(discriminant)
            return result

if __name__ == "__main__":
    from vector3 import *
    center = Vector3(0, 0, -10)
    radius = 4 
    color = (0, 0, 1)
    sph1 = Sphere(center, radius, color)
    #print sph1.radius, sph1.center, sph1.color
    from ray import Ray
    ray_origin = origin = Vector3(0, 0, 0)
    #print origin
    ray_direction = (Vector3(0, 3, -10) - origin)
    #print ray_direction
    r1 = Ray(ray_origin, ray_direction)
    print sph1.find_intersection(r1)
