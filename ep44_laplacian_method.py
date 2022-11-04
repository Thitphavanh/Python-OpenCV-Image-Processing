# Laplacian Method
import cv2
from cv2 import medianBlur
import matplotlib.pyplot as plt
import numpy as np


# Original
img = cv2.imread('images/currency.jpg', 0)

lap = cv2.Laplacian(img, 1)

cv2.imshow('Original', img)
cv2.imshow('Laplacian', lap)


cv2.waitKey(0)
cv2.destroyAllWindows()
