from primitive import Primitive

class Sphere(Primitive):
    def __init__(self, center, radius, color):
        super(Sphere, self).__init__(color)
        self.center = center
        self.radius = radius

    def intersection(ray):
        #From : http://www.cs.unc.edu/~rademach/xroads-RT/RTarticle.html
        result = (0, false)
        #Ray to sphere direction
        eo = self.center - ray.origin
        #Ray to sphere length
        rts_length = dot(eo, eo)
        #Distance to the sphere along the ray
        v = dot(eo, ray.direction)
        if v < 0:
            return result
        discriminant = (self.radius * self.radius) - (rts_length - v*v)
        if discriminant < 0:
            return result
        else:
          result[1] = True
          result[0] = sqrt(discriminant)
          return result

