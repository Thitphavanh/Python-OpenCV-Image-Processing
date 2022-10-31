# Convolution Filter 2D
import cv2
from cv2 import medianBlur
import matplotlib.pyplot as plt
import numpy as np


# Original
img = cv2.imread('images/Noise.png')

# Filter
filter_2d = cv2.filter2D(img, -1, np.ones((5, 5), np.float32)/25)

# Blur
blurs = cv2.blur(img, (5, 5))

# Median
medianBlurs = cv2.medianBlur(img, 5)


titles = ['Original', 'Filter2D 5x5', "Blurs", "MedianBlurs"]
images = [img, filter_2d, blurs, medianBlurs]

for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()
