# Opencv Video

import cv2


# ອ່ານຮູບ
img = cv2.imread('images/cat.jpg')

# ກຳນົດຂະໜາດ
imgresize = cv2.resize(img, (700, 700))

# ແຕ້ມເສັ້ນຊື່
# line (ຮູບ, ຈຸດເລີ່ມຕົ້ນ (x,y), ຈຸດສຸດທ້າຍ (x,y), ສີ (BGR), ຄວາມໜາ)
cv2.arrowedLine(imgresize, (100, 100), (500, 200), (255, 0, 0), 10)
cv2.arrowedLine(imgresize, (20, 100), (400, 400), (0, 255, 0), 10)
cv2.arrowedLine(imgresize, (0, 0), (600, 400), (0, 0, 255), 10)

cv2.imshow('Output', imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
