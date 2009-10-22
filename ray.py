from vector3 import Vector3, UNIT_X

class Ray(object):
    def __init__(self, origin, direction):
        super(Ray, self).__init__()
        self.origin = origin
        self.direction = direction
        self.direction.normalise()
    def __str__(self):
        return 'Ray Data\n' + 'Origin: '+ str(self.origin)+ '\nDirection: ' + str(self.direction)


if __name__ == "__main__":
    r = Ray(Vector3(0,0,0), UNIT_X)
    print r
