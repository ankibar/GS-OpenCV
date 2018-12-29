import cv2
import numpy as np

img = cv2.imread('apple.jpg')

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscale, 12 , 255, cv2.THRESH_BINARY)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()	