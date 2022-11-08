# Contours
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('images/ant.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, result = cv2.threshold(gray, 215, 255, cv2.THRESH_BINARY)

contours, hierarchys = cv2.findContours(
    result, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

print(len(contours))

cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
