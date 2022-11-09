# Motion Detection
import cv2


videos = cv2.VideoCapture('images/Walking.mp4')

# ຮັບຮູບຈາກກ້ອງ frame ຕໍ່ frame
check, frame1 = videos.read()
check, frame2 = videos.read()
while (videos.isOpened()):
    if check == True:
        motiondiff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(motiondiff, cv2.COLOR_BGR2GRAY)
        blurs = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh, result = cv2.threshold(blurs, 15, 255, cv2.THRESH_BINARY)
        dilations = cv2.dilate(result, None, iterations=3)
        contours, hierarchys = cv2.findContours(dilations, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        cv2.imshow("Output", frame1)
        frame1 = frame2
        check, frame2 = videos.read()
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break


videos.release()
cv2.destroyAllWindows()
