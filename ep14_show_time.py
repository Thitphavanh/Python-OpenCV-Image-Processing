# Show time On Camera/VDO
import cv2
import datetime

# cap = cv2.VideoCapture('images/Video.mp4') # ສະແດງຜົນຜ່ານວິດີໂອ
cap = cv2.VideoCapture(0) # ສະແດງຜົນຜ່ານກ້ອງ
while (cap.isOpened()):
    check, frame = cap.read()  # ຮັບພາບຈາກກ້ອງ frame ຕໍ່ frame

    if check == True:
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame, currentDate, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0),cv2.LINE_4)
        cv2.imshow("Output", frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break
        


cv2.release()
cv2.destroyAllWindows()
