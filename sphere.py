from math import sqrt

from primitive import Primitive
from vector3 import dot_product

class Sphere(Primitive):
    def __init__(self, center, radius, color):
        super(Sphere, self).__init__(color)
        self.center = center
        self.radius = float(radius)
    
    def find_intersection(self, ray):
        pass

    def find_intersectionOld(self, ray):
        result = [0, False]
        eo = self.center - ray.origin
        v = dot_product(eo, ray.direction)
        discriminant = (self.radius * self.radius) - (dot_product(eo, eo) - v * v)
        if discriminant < 0:
            return result
        else:
            d = sqrt(discriminant)
            result[1] = True
            result[0] = d
            return result

    def find_intersectionLesson1(self, ray):
        result = [0, False]
        #Ray to sphere direction
        oc = self.center - ray.origin
        #Ray to sphere length squared
        oc2 = dot_product(oc, oc)
        #Distance to the sphere along the ray
        #In other words, the point on the ray closest to the center
        tca = float(dot_product(oc, ray.direction))
     
        #Is the ray origin outside the sphere?
        outside = oc2 > (self.radius ** 2)
       
        if tca < 0.0 and outside:
            return result
        d2 = oc2 - tca * tca
        thc = (self.radius * self.radius) - d2
        if thc < 0.0:
            return result
        else:
            if outside:
                temp = tca - sqrt(thc)
            else:
                temp = tca + sqrt(thc)

            if temp < 0.0:
                return result
            
            result[1] = True
            result[0] = sqrt(thc)
            return result
    
    def __str__(self):
        return 'S' + ' ' + str(self.center) + ' ' + str(self.radius)

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
    ray_direction = (Vector3(0, 4, -10) - origin)
    #print ray_direction
    r1 = Ray(ray_origin, ray_direction)
    print sph1.find_intersection(r1)
