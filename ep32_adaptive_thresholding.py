# Function Adaptive Thresholding
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('images/boy-girl.jpg', 0)

thresh, result1 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
result2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)
result3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 1)


cv2.imshow('THRESH', result1)
cv2.imshow('MEAN', result2)
cv2.imshow('GAUSSIAN', result3)


cv2.waitKey(0)
cv2.destroyAllWindows()
