import sys
sys.path.append('C:\\dev\\deep')
from pygraphics.config import *
import cv2

CAMERA_BOUNDS = (0, 30, 0, 30)

captura = cv2.VideoCapture('deep/assets/sex.mp4')

from PIL import Image
from OpenGL.GL import *
import numpy as np

def load_texture(file_path):
    img = Image.open(file_path)
    # img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = img.convert("RGBA").tobytes()
    width, height = img.size

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glBindTexture(GL_TEXTURE_2D, 0)

    return texture_id, width, height

def main(): 
    System.camera.set_projection_matrix(*CAMERA_BOUNDS)

    obj2 = System.new_object_2d()
    obj2.transform.position = glm.vec3(2, 10, 0)
    obj2.transform.scale = glm.vec3(5, 5, 1)

    obj = System.new_object_2d("deep/assets/rusa.jpg")
    obj.transform.position = glm.vec3(15, 15, 0)
    obj.transform.scale = glm.vec3(20, 20, 0)

    texT,wT,hT = load_texture("deep/assets/rusa.jpg")

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



        System.gui.set_image("TTT", texT,wT,hT)
        System.gui.set_file("Te2st","Fdww")


        


    System.loop(handle)
    captura.release()

if __name__ == "__main__":
    main()

