# Display Image

import cv2

img = cv2.imread('image/cat.jpg')

cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
