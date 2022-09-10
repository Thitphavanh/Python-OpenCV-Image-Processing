# Opencv Video

import cv2


vdo = cv2.VideoCapture('images/Video.mp4')

while (vdo.isOpened()):
    check, frame = vdo.read()  # ຮັບພາບຈາກກ້ອງ frame ຕໍ່ frame

    if check == True:
        
        cv2.imshow('Output', frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    else:
        break

vdo.release()
cv2.destroyAllWindows()
