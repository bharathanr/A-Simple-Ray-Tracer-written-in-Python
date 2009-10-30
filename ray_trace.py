from math import fabs, pow, sqrt

#from sceneOrtho import objects, lights, BGCOLOR
from scene import objects, lights, BGCOLOR
from vector3 import dot_product
from ray import Ray

def ray_trace(original_ray, r_level = 4):
    obj, dist = get_first_intersection(original_ray)
    reflect_color = [0, 0, 0]
    refract_color = [0, 0, 0]
    if obj is not None:
        point = original_ray.origin + original_ray.direction * dist
        normal = obj.get_normal(point)
        point_color = phong_light(point, normal, original_ray.origin, obj.material)
        if r_level > 0:
            #if the object is reflective
            if obj.material.reflect != 0:
               #Recursively ray-trace
                reflect_color = ray_trace(get_reflected_ray(original_ray,\
                        point, normal), r_level - 1)
            if obj.material.refract != 0.0:
                refract_color = ray_trace(get_refracted_ray(original_ray,\
                        point, normal, obj), r_level - 1)
        #Combine colors
        kr = obj.material.reflect
        i = 0
        while i < 3:
            point_color[i] += kr * reflect_color[i] + refract_color[i]
            i += 1
    else:
        point_color = BGCOLOR

    return point_color

def get_refracted_ray(ray, point, normal, obj):
    #n = n1 / n2 and n1 = ref_index
    cost1 = dot_product(ray.direction, normal)
    if cost1 < 0.0:
        n = 1.0 / obj.material.refract
        cost1 = -cost1
    else:
        normal = -normal
        n = obj.material.refract
    cost2 = sqrt(1.0 - ((n * n) * (1.0 - (cost1 * cost1))))
    refract_direction = ray.direction * n + normal * (n * cost1 - cost2)
    refract_direction.normalise()
    refracted_ray = Ray(point + refract_direction * 0.0001, refract_direction)
    return refracted_ray

def get_reflected_ray(original_ray, point, normal):
    #Calculate the reflected ray
    normal.normalise()
    reflect_direction = original_ray.direction - normal * 2.0 * \
    dot_product(original_ray.direction, normal)
    reflect_direction.normalise()
    reflected_ray = Ray(point + reflect_direction * 0.0001, reflect_direction)
    return reflected_ray

def get_first_intersection(ray, closest_intersection_distance = 100000000.0):
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
                    shade
    return point_color

def phong_light(point, normal, eye, material):
    #A variable to store the final color
    point_color = [0, 0, 0]
    #The ambient, diffuse and specular color of the material
    a_color = material.diffuse_color
    color = material.diffuse_color
    s_color = material.specular_color
    #Ensure that the normal is normalised
    normal.normalise()
    #The ambient coefficient ka
    ambient_coefficient = 0.2
    #Diffuse coefficient Kd 
    k_d = 1
    #Specular coefficient Ks
    k_s = 1
    #Perform ambient lighting
    i =0 
    while i < 3:
        point_color[i] = ambient_coefficient * a_color[i]
        i += 1
    #For each light, compute the contribution to color
    for light in lights:
        #Calculate the light vector
        light_vector = light.position - point
        #Calculate the distance to the light
        dist = light_vector.magnitude
        #Then normalise it
        light_vector.normalise()

        #Calculate the view vector
        view_vector = eye - point
        view_vector.normalise()
        
        #Compute the shadow ray
        shadow_ray = Ray(point + light_vector * 0.001, light_vector)
        #Check if there is an object in the way of the shadow ray
        obj = get_first_intersection(shadow_ray, dist)
        #If there is an object, this lights contribution isn't added
        if obj[0] is not None:
            continue;

        #Else, light it up!
        #Calculate the diffuse lighting
        diffuse = max(dot_product(normal, light_vector), 0.0)
        #Calculate the reflected ray
        reflect= normal * 2.0 * diffuse - light_vector
        reflect.normalise()
        #Calculate the specular lighting
        dp = max(dot_product(view_vector, light_vector), 0.0)
        specular = pow(dp, material.specular_power)
        #Add this lights contribution to each component of the color
        i = 0 
        while i < 3:
            point_color[i] += k_d * color[i] * diffuse\
                    + k_s * s_color[i] * specular
            i += 1
    return point_color
