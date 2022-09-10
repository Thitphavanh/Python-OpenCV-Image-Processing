# Opencv Video

import cv2


vdo = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

result = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

while (vdo.isOpened()):
    check, frame = vdo.read()  # ຮັບພາບຈາກກ້ອງ frame ຕໍ່ frame

    if check == True:
        cv2.imshow('Output', frame)
        result.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

result.release()
vdo.release()
cv2.destroyAllWindows()
