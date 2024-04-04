import glm
from pygraphics.helpers.class_type import ClassType

class Camera(ClassType):
    def __init__(self):
        self.set_class(Camera)
        self.projection_matrix = glm.mat4(1.0);
        self.view_matrix = glm.mat4(1.0);
        self.view_projection_matrix = glm.mat4(1.0);
    
    def get_projection_matrix(self):
        return self.projection_matrix
    
    def get_view_matrix(self):
        return self.view_matrix
    
    def get_view_projection_matrix(self):
        return self.view_projection_matrix
    
    def set_projection_matrix(self, projection):
        self.projection_matrix = projection
    
    def set_view_matrix(self, view):
        self.view_matrix = view
    
    def set_view_projection_matrix(self, matrix):
        self.view_projection_matrix = matrix

    def compute_projection_matrix(self):
        pass



    

