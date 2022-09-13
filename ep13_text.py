# Opencv Video

import cv2


# ອ່ານຮູບ
img = cv2.imread('images/cat.jpg')

# ກຳນົດຂະໜາດ
imgresize = cv2.resize(img, (700, 650))

# ແຕ້ມຂໍ້ຄວາມເທິງຮູບ
# circle (ຮູບ, ຂໍ້ຄວາມ, ພິກັດທີ່ຈະສະແດງຂໍ້ຄວາມ(x, y), font, ຂະໜາດຂໍ້ຄວາມ, ສີ, ຄວາມໜາ)
cv2.putText(imgresize, "HERY", (250, 550), cv2.FONT_HERSHEY_COMPLEX, 1.8, (0, 0, 255),cv2.LINE_8)


cv2.imshow('Output', imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
