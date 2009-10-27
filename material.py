
class Material(object):
    def __init__(self, diffuse_color, specular_color = (1, 1, 1), specular_power = 70.0,\
            reflect = 1.0):
        super(Material, self).__init__()
        self.diffuse_color = diffuse_color
        self.specular_color = specular_color
        #n shiny
        self.specular_power = specular_power
        self.reflect = reflect
