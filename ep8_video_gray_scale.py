# Opencv Video

import cv2


vdo = cv2.VideoCapture('images/Video.mp4')

while (vdo.isOpened()):
    check, frame = vdo.read()  # ຮັບພາບຈາກກ້ອງ frame ຕໍ່ frame

    if check == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Output', gray)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    else:
        break

vdo.release()
cv2.destroyAllWindows()
