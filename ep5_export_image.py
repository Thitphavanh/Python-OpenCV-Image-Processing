# Export Image

import cv2

img = cv2.imread('image/cut-gril.jpg', 0)
imgresize = cv2.resize(img, (400, 600))

cv2.imshow('Cute girl', imgresize)
cv2.imwrite('output.jpg', imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
