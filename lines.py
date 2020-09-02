import numpy as np
import cv2
from mss import mss
from PIL import Image

bounding_box = {'top': 70, 'left': 0, 'width': 520, 'height': 400}

sct = mss()

while True:
    frame = np.array(sct.grab(bounding_box))
    #(image, edges, threshold1, threshold2, aperture_size=3) 
    edges = cv2.Canny(frame, 700, 4, 5, 3) 
    cv2.imshow('screen', edges)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
    
    
