# Function Threshold in Matplotlib
import cv2
import matplotlib.pyplot as plt

gray_img = cv2.imread('images/gradient.png')

thresh, result1 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
thresh, result2 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY_INV)
thresh, result3 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TRUNC)
thresh, result4 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO)
thresh, result5 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO_INV)


images = [gray_img, result1, result2, result3, result4, result5]
title = ['Original', 'Binary', 'Binary_INV',
         'Binary_Trunc', 'Binary_Tozero', 'Binary_Tozero_INV']

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()
