# Function Adaptive Thresholding
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('images/boy-girl.jpg', 0)

# ກຳນົດຂະໜາດ Block
size = [3, 5, 9, 17, 33]
plt.subplot(231, xticks=[], yticks=[])
plt.imshow(img, cmap='gray')

for i in range(len(size)):
    result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, size[i], 1)
    plt.subplot(232+i)
    plt.title('%d' % size[i])
    plt.imshow(result, cmap='gray')
    plt.xticks([]), plt.yticks([])


plt.show()
