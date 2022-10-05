# Face Detection
import cv2


# ອ່ານຮູບພາບ
img = cv2.imread('images/boy-girl.jpg')

# ອ່ານ File ສຳຫຼັບ Classification
face_cascade = cv2.CascadeClassifier('detect/haarcascade_frontalface_default.xml')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ຈຳແນກໃບໜ້າ
scaleFactory = 1.1
minNeighber = 3
face_detect = face_cascade.detectMultiScale(
    gray_img, scaleFactory, minNeighber)

# ສະແດງຕຳແໜ່ງທີ່ພົບໃບໜ້າ
for (x, y, w, h) in face_detect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=5)


# ສະແດງຮູບພາບ
cv2.imshow('Orginal', img)
cv2.imshow('Result', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
