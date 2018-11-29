import cv2 
import numpy as np
import binary_image as bi

def skeletonizer(img):
  skel = np.zeros(img.shape, dtype=np.uint8)
  size = np.size(img)

  bin_img = bi.binary_image()
  binary_img = bin_img.binarize(img)

  kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
  maxThin = False

  while not maxThin:
    # OPEN
    eroded = cv2.erode(binary_img, kernel)
    opened = cv2.dilate(eroded, kernel)
    tmp = cv2.subtract(binary_img, opened)
    skel = cv2.bitwise_or(skel, tmp)
    binary_img = eroded.copy()

    emptySet = size - cv2.countNonZero(binary_img)
    if emptySet == size:
      maxThin = True

  return(skel)


# for testing purposes only
def main():
  img = cv2.imread('binary_4.png', 0)
  skel = skeletonizer(img)
  cv2.imwrite("output.jpg", skel)


if __name__ == "__main__":
    main()