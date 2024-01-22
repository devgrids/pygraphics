import sys
sys.path.append('C:\\dev\\deep')
from pygraphics.config import *
import cv2

CAMERA_BOUNDS = (0, 30, 0, 30)

captura = cv2.VideoCapture('deep/assets/sex.mp4')

def main(): 
    System.camera.set_projection_matrix(*CAMERA_BOUNDS)

    obj2 = System.new_object_2d()
    obj2.transform.position = glm.vec3(2, 10, 0)
    obj2.transform.scale = glm.vec3(5, 5, 1)

    obj = System.new_object_2d("deep/assets/rusa.jpg")
    obj.transform.position = glm.vec3(15, 15, 0)
    obj.transform.scale = glm.vec3(20, 20, 0)

    data  = obj2.sprite_renderer.texture.get_data()
    hsv = cv2.cvtColor(data, cv2.COLOR_BGR2HSV) 
    mask = cv2.inRange(hsv, (15,0,0), (30,255,255))
    cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[-2:]
    for contour in cnts:
        cv2.drawContours(data, contour, -1, (0, 255, 0), 2)  

    obj2.sprite_renderer.texture.load_data(data)

    def handle():

        ret, frame = captura.read()
        if not ret:
            captura.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Vuelve al inicio del video
            return
        
        frame = cv2.flip(frame, 0)  # Vertical flip
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, _ = frame.shape

        obj.sprite_renderer.texture.load_texture(w,h,frame)


    System.loop(handle)
    captura.release()

if __name__ == "__main__":
    main()

