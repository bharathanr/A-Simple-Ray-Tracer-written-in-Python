from math import fabs

from primitive import Primitive
from vector3 import dot_product

class Plane(Primitive):
    def __init__(self, normal, distance, material):
        #normal is the normal to the plane
        #distance is the perpendicular distance 
        #of the plane from the world origin
        super(Plane, self).__init__(material)

        self.normal = normal
        self.distance = float(distance)
    
    def find_intersection(self, ray):
        result = [0.0, False]
        rayD = dot_product(self.normal, ray.direction)
        #Check if the ray is parallel to the plane
        if fabs(rayD) < 0.0001:
            return result
        originD = -(dot_product(self.normal, ray.origin) + self.distance)
        intersectDist = originD / rayD

        #Check if the intersection is in front of the camera
        if intersectDist < 0.0001:
            return result

        result[1] = True
        result[0] = intersectDist
        return result

    def get_normal(self, point):
        return self.normal
