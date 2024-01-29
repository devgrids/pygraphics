import sys
sys.path.append('C:\\dev\\deep')
from pygraphics.config import *

CAMERA_BOUNDS = (0, 30, 0, 30)

def main(): 
    System.camera.set_projection_matrix(*CAMERA_BOUNDS)

    video = System.new_video_2d('deep/assets/mascotas.mp4')
    image = System.new_image_2d_cnn()

    obj = System.new_object_2d("deep/assets/goku-black.png")
    obj.transform.position = glm.vec3(15, 15, 0)
    obj.transform.scale = glm.vec3(20, 20, 0)

    def handle():
        pass

    System.loop(handle)

if __name__ == "__main__":
    main()

