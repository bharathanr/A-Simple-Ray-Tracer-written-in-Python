from math import fabs, pow

#from sceneOrtho import objects, lights, BGCOLOR
from scene import objects, lights, BGCOLOR
from vector3 import dot_product

def ray_trace(original_ray):
    obj, dist = get_first_intersection(original_ray)
    if obj is not None:
        point = original_ray.origin + original_ray.direction * dist
        normal = obj.get_normal(point)
        point_color = phong_light(point, normal, original_ray.origin, obj.material)
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

def lambert_light(point, normal, material):
    diffuse_coefficient = 1 
    ambient_coefficient = 0.2
    point_color = [0, 0, 0]
    color = material.diffuse_color
    normal.normalise()
    for light in lights:
        light_vector = light.position - point
        light_vector.normalise()
        shade = dot_product(light_vector, normal)
        if shade < 0:
            shade = 0
        for i in range(len(point_color)):
            point_color[i] += light.color[i] * color[i] * diffuse_coefficient *\
                    shade + color[i] * ambient_coefficient
    return point_color

def phong_light(point, normal, eye, material):
    normal.normalise()
    point_color = [0, 0, 0]
    a_color = material.diffuse_color
    color = material.diffuse_color
    s_color = material.specular_color
    ambient_coefficient = 0.2
    for light in lights:
        light_vector = light.position - point
        view_vector = eye - point
        light_vector.normalise()
        view_vector.normalise()
        #Diffuse coefficient Kd 
        k_d = 1.0
        diffuse = dot_product(normal, light_vector)
        if diffuse < 0:
            diffuse = 0
        #Specular coefficient Ks
        k_s = 1.0
        reflect= normal * 2.0 * diffuse - light_vector
        reflect.normalise()
        dp = max(dot_product(view_vector, light_vector), 0.0)
        specular = pow(dp, material.specular_power)
        i = 0 
        while i < 3:
            point_color[i] += ambient_coefficient * a_color[i] + k_d * color[i] * diffuse\
                    + k_s * s_color[i] * specular
            i += 1
    return point_color
