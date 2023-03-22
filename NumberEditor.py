import cv2
import numpy as np

img = cv2.imread('checkscreen.png')
img = np.array(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Computer Vision', img)
cv2.imwrite("TempSa\Test.png", img)