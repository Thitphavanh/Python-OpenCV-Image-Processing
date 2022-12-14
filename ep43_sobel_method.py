# Sobel Method
import cv2
from cv2 import medianBlur
import matplotlib.pyplot as plt
import numpy as np


# Original
img = cv2.imread('images/currency.jpg', 0)
sobelX = cv2.Sobel(img, -1, 1, 0)
sobelY = cv2.Sobel(img, -1, 0, 1)
sobelXY = cv2.bitwise_or(sobelX, sobelY)

images = [img, sobelX, sobelY, sobelXY]
titles = ['Original', 'SobelX', "SobelY", "SobelXY"]


for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()
