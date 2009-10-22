from math import sqrt

from numpy import dot, cross, array

class Vector3(object):
    def __init__(self, *params, **kargs):
        super(Vector3, self).__init__()
        if kargs.has_key('components'):
                    self.components = array( \
                            kargs.get('components'))
        elif params:
            if len(params) == 3:
                self.components = array([0, 1, 2])
                for i,p in enumerate(params):
                    self.components[i] = p
            else:
                raise Exception("Too many parameters")
        else:
            raise AttributeError

        self.set_magnitude()

    def set_magnitude(self):
        self.magnitude = sqrt(self.components[0] ** 2 +\
                self.components[1] ** 2 + \
                self.components[2] ** 2)
    
    def get_x(self):
        return self.components[0]

    def set_x(self, x):
        self.components[0] = x
        self.set_magnitude()

    x = property(get_x, set_x)

    def get_y(self):
        return self.components[1]

    def set_y(self, y):
        self.components[1] = y
        self.set_magnitude()

    y = property(get_y, set_y)
    
    
    def get_z(self):
        return self.components[2]

    def set_z(self, z):
        self.components[2] = z
        self.set_magnitude()

    z = property(get_z, set_z)

    def normalise(self):
        self.components[0] = self.components[0] / self.magnitude
        self.components[1] = self.components[1] / self.magnitude
        self.components[2] = self.components[2] / self.magnitude
   
        #self.set_magnitude()
    
        #To save time
        self.magnitude = 1.0

    #Operators
    def __neg__(self):
        self.components = -self.components
        #No need to reset magnitude

    def __add__(self, other):
        return Vector3(components = (self.components +\
                other.components))

    def __sub__(self, other):
        return Vector3(components = (self.components -\
                other.components))

    def __mul__(self, other):
        #Watch out. This operation can be unsafe
        #Garbage warning
        return Vector3(components = self.components *  other)

    def __div__(self, other):
        #Watch out. This operation can be unsafe
        #Garbage warning
        return Vector3(components = self.components /  other)
    
    def __str__(self):
        return (('Magnitude:%f Components:' % \
                self.magnitude) +\
                str(self.components))


#Some nice globals
UNIT_X = Vector3(1, 0, 0)
UNIT_Y = Vector3(0, 1, 0)
UNIT_Z = Vector3(0, 0, 1)

def dot_product(v1, v2):
    return dot(v1.components, v2.components)

def cross_product(v1, v2):
    res = cross(v1.components, v2.components)
    return Vector3(components = res)

if __name__ == "__main__":
    v = Vector3(1, 2, 3)
    print v.components, v.magnitude
    v.z = 9 
    print v.components, v.z, v.magnitude
    v.normalise()
    print v.magnitude
    print dot_product(UNIT_X, UNIT_Y)
    print cross_product(UNIT_Y, UNIT_Z).components
    print UNIT_X / 0.1

