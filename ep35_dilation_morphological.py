# Dialation Morphological
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('images/CoinNoise.png', 0)
Thresh, result = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((2, 2), np.uint8)

dilation = cv2.dilate(result, kernel, iterations=2)

titles = ['ORIGINAL', 'THRESH', 'DILATION']
images = [img, result, dilation]


for i in range(len(images)):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
