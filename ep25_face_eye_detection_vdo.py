# Face Detection
import cv2


# ອ່ານວິດີໂອ
cap = cv2.VideoCapture('images/Mark.mp4')

# ອ່ານ File xml ສຳຫຼັບ Classification
face_cascade = cv2.CascadeClassifier('detect/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('detect/haarcascade_eye_tree_eyeglasses.xml')

# ສະແດງຜົນວິດີໂອ
while (cap.isOpened()):
    check, frame = cap.read()
    if check == True:
        gray_vdo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # ຈຳແນກດວງຕາ
        scaleFactory = 1.2
        minNeighber = 5
        # ກວດຈັບໃບໜ້າ
        face_detect = face_cascade.detectMultiScale(gray_vdo, scaleFactory, minNeighber)
        # ກວດຈັບດວງຕາ
        eye_detect = eye_cascade.detectMultiScale(gray_vdo, scaleFactory, minNeighber)
        # ສະແດງຕຳແໜ່ງທີ່ພົບເຫັນດວງຕາ
        for (ex, ey, ew, eh) in face_detect:
            cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), thickness=5)
            for (fx, fy, fw, fh) in eye_detect:
                cv2.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (0, 0, 255), thickness=5)
            
        cv2.imshow('Output', frame)
        if cv2.waitKey(5) & 0xFF == ord('e'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
