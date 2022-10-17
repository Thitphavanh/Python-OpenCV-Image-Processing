# Function Threshold in OpenCV
import cv2
import matplotlib.pyplot as plt

gray_img = cv2.imread('images/gradient.png')

thresh, result1 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
thresh, result2 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY_INV)
thresh, result3 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TRUNC)
thresh, result4 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO)
thresh, result5 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Original', gray_img)
cv2.imshow('Binary', result1)
cv2.imshow('Binary_INV', result2)
cv2.imshow('Binary_Trunc', result3)
cv2.imshow('Binary_Tozero', result4)
cv2.imshow('Binary_Tozero_INV', result5)

# img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
