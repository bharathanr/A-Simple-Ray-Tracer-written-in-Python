from numpy import array, cross

from save_image import save_bmp
from scene import IMAGE_SIZE, initialise_default_scene
from ray_trace import ray_trace
from ray import Ray
from vector3 import Vector3, UNIT_Z



def clamp(color):
    col = list(color)
    for i in range(len(color)):
        col[i] = int(min( col[i] * 255, 255))

    return tuple(col)

    
def generate_rays():
    rays = []
    direct = -UNIT_Z
    for x in range(IMAGE_SIZE[0]):
        for y in range(IMAGE_SIZE[1]):
            org = Vector3(x, y, 1000.0)
            ray = Ray(org, direct)
            rays.append(ray)
    return rays


def render(ray_buffer = []):
    print "Ray Tracing Started"
    height = IMAGE_SIZE[1]
    width = IMAGE_SIZE[0]
    image_buf = []
    for x in range(width):
        if x == (width * 0.4): 
            print "25% complete..."
          
        if x == (width * 0.5): 
            print "50% complete..." 
        
        if x == (width * 0.75): 
            print "75% complete..."

        if x == (width - 1): 
            print "100% complete..."
           
        for y in range(height):
            primary_ray = Ray(Vector3(x, y, 0), -UNIT_Z)
            #primary_ray = ray_buffer[x * height + y]
            color = ray_trace(primary_ray)
            image_buf.append(clamp(color))
    return image_buf
            
def main():
    initialise_default_scene()
    #buf = render(generate_rays())
    buf = render()
    save_bmp("QuestWorld", buf, (1024, 768))

if __name__== '__main__':
    main()
