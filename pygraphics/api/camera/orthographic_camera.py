from pygraphics.api.camera.camera import Camera

class OrthographicCamera(Camera):
     def __init__(self):
          super().__init__()
          self.set_class(OrthographicCamera)

