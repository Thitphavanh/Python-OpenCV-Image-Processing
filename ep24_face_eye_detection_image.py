# Face Detection
import cv2


# ອ່ານຮູບພາບ
img = cv2.imread('images/boy-girl.jpg')

# ອ່ານ File xml ສຳຫຼັບ Classification
face_cascade = cv2.CascadeClassifier('detect/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('detect/haarcascade_eye_tree_eyeglasses.xml')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


scaleFactory = 1.1
minNeighber = 3
# ກວດຈັບໃບໜ້າ
face_detect = face_cascade.detectMultiScale(gray_img, scaleFactory, minNeighber)

# ກວດຈັບດວງຕາ
eye_detect = eye_cascade.detectMultiScale(gray_img, scaleFactory, minNeighber)

# ສະແດງຕຳແໜ່ງທີ່ພົບເຫັນດວງຕາ
for (fx, fy, fw, fh) in face_detect:
    cv2.rectangle(img, (fx, fy), (fx+fw, fy+fh), (0, 255, 0), thickness=5)
    for (ex, ey, ew, eh) in eye_detect:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 255), thickness=5)


# ສະແດງຮູບພາບ
cv2.imshow('Orginal', img)
cv2.imshow('Result', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
