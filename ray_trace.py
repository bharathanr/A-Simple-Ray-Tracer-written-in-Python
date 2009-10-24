#from sceneOrtho import objects, lights, BGCOLOR
from scene import objects, lights, BGCOLOR
from vector3 import dot_product

DEBUG = 1

def ray_trace(original_ray):
    obj, dist = get_first_intersection(original_ray)
    if obj is not None:
        point = original_ray.origin + original_ray.direction * dist
        normal = obj.get_normal(point)
        point_color = lambert_light(point, normal, obj.color)
    else:
        point_color = BGCOLOR
    
    return point_color

def get_first_intersection(ray):
   closest_intersection_distance = 100000000.0
   closest_intersected_object = None
   for obj in objects:
        result = obj.find_intersection(ray)
        if result[1] is True:
            if result[0] < closest_intersection_distance:
                closest_intersected_object = obj
                closest_intersection_distance = result[0]
   return (closest_intersected_object, closest_intersection_distance)

def lambert_light(point, normal, color):
    diffuse_coefficient = 0.8
    point_color = [0, 0, 0]
    for light in lights:
        light_vector = light.position - point
        shade = dot_product(light_vector, normal)
        if shade < 0:
            shade = 0
        for i in range(len(point_color)):
            point_color[i] += color[i] * (0.2 + diffuse_coefficient * shade)
    
    return point_color
