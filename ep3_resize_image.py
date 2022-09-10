# Resize Image

import cv2

img = cv2.imread('image/cut-gril.jpg')
imgresize = cv2.resize(img, (400, 600))

cv2.imshow('Output', imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
