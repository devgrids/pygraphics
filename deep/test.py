import cv2
import numpy as np
def nothing(a):
    pass

cv2.namedWindow('Tester')
cv2.createTrackbar('HH','Tester',0,179,nothing)
cv2.createTrackbar('HL','Tester',0,179,nothing)
cv2.createTrackbar('SH','Tester',0,255,nothing)
cv2.createTrackbar('SL','Tester',0,255,nothing)
cv2.createTrackbar('VH','Tester',0,255,nothing)
cv2.createTrackbar('VL','Tester',0,255,nothing)

img = cv2.imread('deep/assets/chizu.jfif')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

key = cv2.waitKey(1)

while not key == ord('q'):

    hh = cv2.getTrackbarPos('HH','Tester')
    hl = cv2.getTrackbarPos('HL','Tester')
    sh = cv2.getTrackbarPos('SH','Tester')
    sl = cv2.getTrackbarPos('SL','Tester')
    vh = cv2.getTrackbarPos('VH','Tester')
    vl = cv2.getTrackbarPos('VL','Tester')

    lower_white = np.array([hl,sl,vl], dtype=np.uint8)
    upper_white = np.array([hh,sh,vh], dtype=np.uint8)
    
    mask = cv2.inRange(hsv, lower_white, upper_white)

    cv2.imshow("Mascara", mask)
    cv2.imshow("Imagen", img)

    key = cv2.waitKey(1)
    
cv2.destroyAllWindows()