# Opencv Video

import cv2


# ອ່ານຮູບ
img = cv2.imread('images/cat.jpg')

# ກຳນົດຂະໜາດ
imgresize = cv2.resize(img, (700, 650))

# ແຕ້ມສີ່ຫຼ່ຽມ
# rectangle (ຮູບ, ມຸມທີ 1 (ເບິ່ງຊ້າຍ), ມຸມທີ 2 (ລູ່ມຊວາ), ສີ, ຄວາມໜາ)
cv2.rectangle(imgresize, (100, 100), (500, 500), (0, 0, 255), -1)


cv2.imshow('Output', imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
