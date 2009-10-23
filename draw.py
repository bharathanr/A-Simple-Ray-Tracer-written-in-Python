from math import pi, tan

from numpy import array, cross

from save_image import save_bmp
from scene import IMAGE_SIZE, initialise_default_scene
from ray_trace import ray_trace
from ray import Ray
from vector3 import Vector3, UNIT_Z, UNIT_Y, cross_product


def clamp(color):
    col = list(color)
    for i in range(len(color)):
        col[i] = int(min( col[i] * 255, 255))

    return tuple(col)

    
def generate_rays():
    HRES = IMAGE_SIZE[0]
    VRES = IMAGE_SIZE[1]
    
    aspect_ratio = float(HRES) / VRES

    #Camera parameters to be abstracted away later
    fovy = 45.0 * (pi / 180.0)
    #UNIT_Y is up
    eye = Vector3(0, 0, 0)
    look_at = Vector3(0, 0, -10)
    d = 1 / tan(fovy/2)
    #End camera parameters
    
    #Calculate orthonormal basis
    l = look_at - eye
    l.normalise()
    
    v = cross_product(l, UNIT_Y)
    v.normalise()
    
    #Note that u is a unit vector!
    u = cross_product(v, l)
    #Note: v is right and u is up on the image plane
    
    #Find the lower left corner
    #look_at is the center of the image plane...
    ll = eye +  l * d - v * aspect_ratio   - u
    #End calculations
        
    rays = []
    v_step = 2.0 / VRES
    h_step = 2.0 * aspect_ratio / HRES
    for x in xrange(HRES):
        for y in xrange(VRES):
            p = ll + v * h_step * float(x)  + u * v_step * float(y)
            d = p - eye
            d.normalise()
            ray = Ray(eye, d)
            rays.append(ray)
    return rays


def render(ray_buffer = []):
    print "Ray Tracing Started"
    height = IMAGE_SIZE[1]
    width = IMAGE_SIZE[0]
    image_buf = []
    for x in xrange(width):
        if x == (width * 0.25): 
            print "25% complete..."
          
        if x == (width * 0.5): 
            print "50% complete..." 
        
        if x == (width * 0.75): 
            print "75% complete..."

        if x == (width - 1): 
            print "100% complete..."
           
        for y in xrange(height):
            primary_ray = ray_buffer[x * height + y]
            color = ray_trace(primary_ray)
            image_buf.append(clamp(color))
    return image_buf
            
def main():
    initialise_default_scene()
    buf = render(generate_rays())
    save_bmp("QuestWorld", buf, (1024, 768))

if __name__== '__main__':
    main()
