import sys
sys.path.append('C:\\dev\\deep')
from pygraphics.config import *
import cv2

CAMERA_BOUNDS = (0, 30, 0, 30)

def main(): 
    System.camera.set_projection_matrix(*CAMERA_BOUNDS)

    obj = System.new_game_object_2d("deep/assets/chizu.jfif")
    obj.transform.position = glm.vec3(15, 15, 0)
    obj.transform.scale = glm.vec3(20, 20, 0)

    data  = obj.sprite_renderer.texture.get_data()
    hsv = cv2.cvtColor(data, cv2.COLOR_BGR2HSV) 
    mask = cv2.inRange(hsv, (15,0,0), (30,255,255))
    cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2:]
    for contour in cnts:
        cv2.drawContours(data, contour, -1, (0, 255, 0), 2)  

    obj.sprite_renderer.texture.load_data(data)

    def handle():
        delta_time = System.time_manager.get_delta_time()

    System.loop(handle)

if __name__ == "__main__":
    main()

