from pygraphics.api.camera.camera import Camera

class OrthographicCamera(Camera):
     def __init__(self, left = -10, right = 10, bottom = 10, top = -10, z_near = -1.0, z_far = 1.0):
          super().__init__()
          self.set_class(OrthographicCamera)
          self.frustum(left, right, bottom, top, z_near, z_far)

     def frustum(self, left = -10, right = 10, bottom = 10, top = -10, z_near = -1.0, z_far = 1.0):
          self.left = left
          self.right = right
          self.bottom = bottom
          self.top = top
          self.z_near = z_near
          self.z_far = z_far

     def compute_projection_matrix(self):
          import glm
          projection = glm.ortho(self.left, self.right, self.bottom, self.top, self.z_near, self.z_far)
          super().set_projection_matrix(projection)

     def set_projection_matrix(self, left, right, bottom, top, z_near = -1.0, z_far = 1.0):
          self.frustum(left, right, bottom, top, z_near, z_far)
          self.compute_projection_matrix()

