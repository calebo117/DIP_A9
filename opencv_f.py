import cv2
import numpy as np
def eroder(img):
	#img = cv2.imread('j.png',0)
	kernel = np.ones((5,5),np.uint8)
	erosion = cv2.erode(img,kernel,iterations = 1)
	return(erosion)