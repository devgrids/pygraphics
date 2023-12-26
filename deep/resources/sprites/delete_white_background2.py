import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

i=0
for fname in glob.glob('jiren/base/punch/*.png'):
    frame = cv2.imread(fname)
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame[np.all(frame == [255, 255, 255, 255], axis=2)] = [0, 0, 0, 0]
    #frame[np.all(np.isclose(frame, [255, 255, 255, 255], atol=200), axis=2)] = [0, 0, 0, 0]
    cv2.imwrite("jiren/base/punch/"+str(i)+".png", frame)
    i=i+1

