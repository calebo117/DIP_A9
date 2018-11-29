import cv2 as cv
import copy
import numpy as np
#import

def boundary_extract(sample, window):
    #image is first argument
    #structuring element is the second argument
    img = sample.copy()

    erodeimage = cv.erode(img, window)

    finalimage = img - erodeimage

    return finalimage

'''if __name__ == "__main__":
    image = cv.imread('binary_1.png')
    struc = cv.getStructuringElement(cv.MORPH_RECT,(2,2))
    boundary_extract(image, struc)'''

