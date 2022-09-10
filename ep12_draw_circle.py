# Opencv Video

import cv2


# ອ່ານຮູບ
img = cv2.imread('images/cat.jpg')

# ກຳນົດຂະໜາດ
imgresize = cv2.resize(img, (700, 650))

# ແຕ້ມວົງມົນ
# circle (ຮູບ, ຕຳແໜ່ງຈຸດສູນກາງວົງມົນ(x, y), ລັດສະໝີ, ສີ, ຄວາມໜາ)
cv2.circle(imgresize, (200, 200), 75,  (0, 0, 255), 5)


cv2.imshow('Output', imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
