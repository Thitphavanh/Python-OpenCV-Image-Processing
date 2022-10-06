# Face Detection
import cv2


# ອ່ານວິດີໂອ
cap = cv2.VideoCapture('images/Mark.mp4')

# ອ່ານ File ສຳຫຼັບ Classification
eye_cascade = cv2.CascadeClassifier('detect/haarcascade_eye_tree_eyeglasses.xml')

# ສະແດງຜົນວິດີໂອ
while (cap.isOpened()):
    check, frame = cap.read()
    if check == True:
        gray_vdo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # ຈຳແນກດວງຕາ
        scaleFactory = 1.2
        minNeighber = 5
        eye_detect = eye_cascade.detectMultiScale(
            gray_vdo, scaleFactory, minNeighber)
        # ສະແດງຕຳແໜ່ງທີ່ພົບເຫັນດວງຕາ
        for (x, y, w, h) in eye_detect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=5)
            cv2.imshow('Output', frame)
        if cv2.waitKey(5) & 0xFF == ord('e'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
