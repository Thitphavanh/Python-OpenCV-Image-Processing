# Dialation Morphological
import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('images/CoinNoise.png', 0)
Thresh, result = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((2, 2), np.uint8)


# ການຂະຫຍາຍຮູບພາບ
dilation = cv2.dilate(result, kernel, iterations=2)
# ການກັ້ນຕອງຮູບພາບ
erosion = cv2.erode(dilation, kernel, iterations=7)
# ການເປີດ
opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel, iterations=7)
# ການປິດ
closing = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel, iterations=5)

titles = ['ORIGINAL', 'THRESH', 'DILATION', 'EROSION', 'OPENING', 'CLOSING']
images = [img, result, dilation, erosion, opening, closing]


for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
