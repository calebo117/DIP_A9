import cv2
import numpy as np

def eroder(img, window, size):
	#img = cv2.imread('j.png',0)
	if (size == "3-cross"):
		kernel = np.array([ [0,1,0],
							[1,1,1],
							[0,1,0]], dtype=np.uint8)
	elif(size == "5-cross"):
		kernel = np.array([	[0,0,1,0,0],
							[0,1,1,1,0],
							[1,1,1,1,1],
							[0,1,1,1,0],
							[0,0,1,0,0]], dtype=np.uint8)
	else:
		kernel = np.ones((size,size),np.uint8)
	erosion = cv2.erode(img,kernel,iterations = 1)
	return(erosion)

def dilater(img, window, size):
	if (size == "3-cross"):
		kernel = np.array([ [0,1,0],
							[1,1,1],
							[0,1,0]], dtype=np.uint8)
	elif(size == "5-cross"):
		kernel = np.array([	[0,0,1,0,0],
							[0,1,1,1,0],
							[1,1,1,1,1],
							[0,1,1,1,0],
							[0,0,1,0,0]], dtype=np.uint8)
	else:
		kernel = np.ones((size,size),np.uint8)
	dilation = cv2.dilate(img,kernel,iterations = 1)
	return(dilation)

def opener(img, window, size):
	if (size == "3-cross"):
		kernel = np.array([ [0,1,0],
							[1,1,1],
							[0,1,0]], dtype=np.uint8)
	elif(size == "5-cross"):
		kernel = np.array([	[0,0,1,0,0],
							[0,1,1,1,0],
							[1,1,1,1,1],
							[0,1,1,1,0],
							[0,0,1,0,0]], dtype=np.uint8)
	else:
		kernel = np.ones((size,size),np.uint8)
	opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	return(opening)

def closer(img, window, size):
	if (size == "3-cross"):
		kernel = np.array([ [0,1,0],
							[1,1,1],
							[0,1,0]], dtype=np.uint8)
	elif(size == "5-cross"):
		kernel = np.array([	[0,0,1,0,0],
							[0,1,1,1,0],
							[1,1,1,1,1],
							[0,1,1,1,0],
							[0,0,1,0,0]], dtype=np.uint8)
	else:
		kernel = np.ones((size,size),np.uint8)
	closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	return(closing)

def ocer(img,size):
	if (size == "3-cross"):
		kernel = np.array([ [0,1,0],
							[1,1,1],
							[0,1,0]], dtype=np.uint8)
	elif(size == "5-cross"):
		kernel = np.array([	[0,0,1,0,0],
							[0,1,1,1,0],
							[1,1,1,1,1],
							[0,1,1,1,0],
							[0,0,1,0,0]], dtype=np.uint8)
	else:
		kernel = np.ones((size,size),np.uint8)
	closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

	return(opening)

def coer(img,size):
	if (size == "3-cross"):
		kernel = np.array([ [0,1,0],
							[1,1,1],
							[0,1,0]], dtype=np.uint8)
	elif(size == "5-cross"):
		kernel = np.array([	[0,0,1,0,0],
							[0,1,1,1,0],
							[1,1,1,1,1],
							[0,1,1,1,0],
							[0,0,1,0,0]], dtype=np.uint8)
	else:
		kernel = np.ones((size,size),np.uint8)
	closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

	return(opening)

def boundary(img):
	kernel = np.ones((2,1),np.uint8)
	bounds = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
	return(bounds)

def blobber(img):
	#img = cv2.imread("binary_1.png", cv2.IMREAD_GRAYSCALE)
	params = cv2.SimpleBlobDetector_Params()
	params.filterByInertia = False
	params.filterByConvexity = False
	params.filterByColor = True
	params.blobColor = 255
	params.filterByArea = True
	params.minArea = 20

	detector = cv2.SimpleBlobDetector_create(params)
	keypoints = detector.detect(img)
	blobby = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	return(blobby)

def different(img, newimg):
	diff = cv2.absdiff(img,newimg)
	return(diff)