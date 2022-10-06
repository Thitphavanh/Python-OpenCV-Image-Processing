# Face Detection
import cv2


# ອ່ານຮູບພາບ
img = cv2.imread('images/boy-girl.jpg')

# ອ່ານ File ສຳຫຼັບ Classification
eye_cascade = cv2.CascadeClassifier('detect/haarcascade_eye_tree_eyeglasses.xml')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ຈຳແນກດວງຕາ
scaleFactory = 1.1
minNeighber = 3
eye_detect = eye_cascade.detectMultiScale(gray_img, scaleFactory, minNeighber)

# ສະແດງຕຳແໜ່ງທີ່ພົບເຫັນດວງຕາ
for (x, y, w, h) in eye_detect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=5)


# ສະແດງຮູບພາບ
cv2.imshow('Orginal', img)
cv2.imshow('Result', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
